import os
import allure
import uuid
import sys
import time
import logging
from playwright.sync_api import sync_playwright
from urls.urls_pol import urls, names, urls_stage, names_stage
from pages.screen_page import ScreenPage

HEADLESS = True if os.getenv("HEADLESS") == "True" else False


@allure.title("Скриншоты Санкт-Петербурга")
class TestSearchChrome:
    @allure.title("Скриншоты Санкт-Петербурга прод")
    def test_screenshot_prod_pol(self):
        logger = logging.getLogger("test_screenshot_prod_pol")
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%H:%M:%S")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            logger.propagate = False

        total = len(names)
        logger.info(f"Старт теста (prod): всего страниц {total}")

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=HEADLESS,
                args=['--no-sandbox', '--disable-dev-shm-usage']
            )
            context = browser.new_context(ignore_https_errors=True)
            page = context.new_page()

            for idx, (screen, name) in enumerate(zip(urls, names), start=1):
                start_ts = time.time()
                logger.info(f"[{idx}/{total}] Открываю URL: {screen}")
                try:
                    uuid4 = uuid.uuid4()
                    page.goto(screen, wait_until='networkidle', timeout=15000)
                    open_ts = time.time()
                    logger.info(f"[{idx}/{total}] Загружено за {open_ts - start_ts:.2f} c. Обрабатываю контент…")

                    screen_obj = ScreenPage(page=page)
                    screen_obj.open_read_more_buttons()
                    screen_obj.open_read_full_buttons()
                    screen_obj.click_all_faq_buttons()
                    page.wait_for_timeout(2000)
                    page.set_viewport_size({"width": 1920, "height": 8000})

                    screenshot_path = f'{os.getenv("BASE_SAVING_PATH")}/screens/pol_prod/{name}.png'
                    page.screenshot(path=screenshot_path, full_page=True)

                    end_ts = time.time()
                    logger.info(f"[{idx}/{total}] Скриншот сохранён: {screenshot_path}. Время шага: {end_ts - start_ts:.2f} c")
                except Exception as e:
                    logger.error(f"[{idx}/{total}] Ошибка при обработке {screen}: {e}")

    @allure.title("Скриншоты Санкт-Петербурга стэйдж")
    def test_screenshot_stage_pol(self):
        logger = logging.getLogger("test_screenshot_stage_pol")
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%H:%M:%S")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            logger.propagate = False

        total = len(names_stage)
        logger.info(f"Старт теста (stage): всего страниц {total}")

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=HEADLESS,
                args=['--no-sandbox', '--disable-dev-shm-usage']
            )
            context = browser.new_context(ignore_https_errors=True)
            page = context.new_page()

            for idx, (screen, name) in enumerate(zip(urls_stage, names_stage), start=1):
                start_ts = time.time()
                logger.info(f"[{idx}/{total}] Открываю URL: {screen}")
                try:
                    uuid4 = uuid.uuid4()
                    page.goto(screen, wait_until='networkidle', timeout=15000)
                    open_ts = time.time()
                    logger.info(f"[{idx}/{total}] Загружено за {open_ts - start_ts:.2f} c. Обрабатываю контент…")

                    screen_obj = ScreenPage(page=page)
                    screen_obj.open_read_more_buttons()
                    screen_obj.open_read_full_buttons()
                    screen_obj.click_all_faq_buttons()
                    page.wait_for_timeout(2000)
                    page.set_viewport_size({"width": 1920, "height": 8000})

                    screenshot_path = f'{os.getenv("BASE_SAVING_PATH")}/screens/pol_stage/{name}.png'
                    page.screenshot(path=screenshot_path, full_page=True)

                    end_ts = time.time()
                    logger.info(f"[{idx}/{total}] Скриншот сохранён: {screenshot_path}. Время шага: {end_ts - start_ts:.2f} c")
                except Exception as e:
                    logger.error(f"[{idx}/{total}] Ошибка при обработке {screen}: {e}")
