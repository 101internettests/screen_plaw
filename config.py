import os
import html
import logging
from typing import Optional, Union

import requests
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

host_stage = os.getenv("URL_STAGE")
host_stage_second = os.getenv("URL_STAGE_SECOND")
host_prod = os.getenv("URL_PROD")
pol_url = os.getenv("POL_PROD_URL")
mol_url = os.getenv("MOL_PROD_URL")
review_url = os.getenv("REVIEW_URL")
chat_id = os.getenv("CHAT_ID")


def _env_bool(name: str, default: bool = False) -> bool:
    raw_value = os.getenv(name)
    if raw_value is None:
        return default
    return raw_value.strip().lower() in ("1", "true", "yes", "y", "on")


class TelegramNotifier:
    """Совместимый транспорт Telegram уведомлений (proxy/direct)."""

    def __init__(self):
        self.bot_token = (os.getenv("BOT_TOKEN") or "").strip()
        self.default_chat_id = (os.getenv("CHAT_ID") or "").strip()
        self.use_telegram_proxy = _env_bool("USE_TELEGRAM_PROXY", False)
        self.telegram_proxy_url = (os.getenv("TELEGRAM_PROXY_URL") or "").strip()
        self.telegram_proxy_auth_secret = (os.getenv("TELEGRAM_PROXY_AUTH_SECRET") or "").strip()
        self.telegram_proxy_creds = (os.getenv("TELEGRAM_PROXY_CREDS") or "").strip()
        try:
            self.telegram_proxy_timeout_sec = float(os.getenv("TELEGRAM_PROXY_TIMEOUT_SEC", "15"))
        except Exception:
            self.telegram_proxy_timeout_sec = 15.0
        self._proxy_missing_env_logged = False

    def _missing_proxy_env(self):
        missing = []
        if not self.telegram_proxy_url:
            missing.append("TELEGRAM_PROXY_URL")
        if not self.telegram_proxy_auth_secret:
            missing.append("TELEGRAM_PROXY_AUTH_SECRET")
        if not self.telegram_proxy_creds:
            missing.append("TELEGRAM_PROXY_CREDS")
        return missing

    def is_configured(self) -> bool:
        if self.use_telegram_proxy:
            return len(self._missing_proxy_env()) == 0
        return bool(self.bot_token and self.default_chat_id)

    def send_message(self, chat_id: Optional[Union[str, int]], text: str) -> bool:
        """Совместимость с telebot.send_message(chat_id, text)."""
        message = str(text or "")

        if self.use_telegram_proxy:
            missing = self._missing_proxy_env()
            if missing:
                if not self._proxy_missing_env_logged:
                    logger.error(
                        "Telegram proxy missing required env vars: %s",
                        ", ".join(missing),
                    )
                    self._proxy_missing_env_logged = True
                return False
            try:
                response = requests.post(
                    self.telegram_proxy_url,
                    headers={
                        "Content-Type": "application/json",
                        "X-Authentication": self.telegram_proxy_auth_secret,
                    },
                    json={
                        "title": html.escape("screen_plaw tests"),
                        "text": html.escape(message),
                        "creds": self.telegram_proxy_creds,
                        "parse_mode": "HTML",
                        "disable_notification": False,
                    },
                    timeout=self.telegram_proxy_timeout_sec,
                )
                if response.status_code >= 400:
                    logger.error(
                        "Telegram proxy error: status=%s body=%s",
                        response.status_code,
                        (response.text or "")[:180],
                    )
                    return False
                return True
            except requests.Timeout:
                logger.error("Telegram proxy timeout after %ss", self.telegram_proxy_timeout_sec)
                return False
            except requests.RequestException as exc:
                logger.error("Telegram proxy transport error: %s", exc)
                return False
            except Exception as exc:
                logger.error("Telegram proxy unexpected error: %s", exc)
                return False

        target_chat_id = str(chat_id or self.default_chat_id or "").strip()
        if not self.bot_token or not target_chat_id:
            logger.warning("Telegram direct transport is not configured: BOT_TOKEN/CHAT_ID missing")
            return False
        try:
            response = requests.post(
                f"https://api.telegram.org/bot{self.bot_token}/sendMessage",
                data={"chat_id": target_chat_id, "text": message},
                timeout=10,
            )
            if not response.ok:
                logger.error(
                    "Telegram API error: status=%s body=%s",
                    response.status_code,
                    (response.text or "")[:180],
                )
                return False
            return True
        except requests.RequestException as exc:
            logger.error("Telegram direct transport error: %s", exc)
            return False
        except Exception as exc:
            logger.error("Telegram direct unexpected error: %s", exc)
            return False


bot = TelegramNotifier()
