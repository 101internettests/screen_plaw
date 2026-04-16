# screen_plaw

## Telegram notifications

The project supports two transports for notifications sent from pytest hooks:

- `proxy` (recommended for CI): set `USE_TELEGRAM_PROXY=true` and provide proxy credentials.
- `direct` (fallback): use `BOT_TOKEN` and `CHAT_ID`.

### Proxy env contract

- `USE_TELEGRAM_PROXY=true`
- `TELEGRAM_PROXY_URL`
- `TELEGRAM_PROXY_AUTH_SECRET`
- `TELEGRAM_PROXY_CREDS`
- `TELEGRAM_PROXY_TIMEOUT_SEC=15` (optional)

When proxy mode is enabled, `BOT_TOKEN` and `CHAT_ID` are not required.
