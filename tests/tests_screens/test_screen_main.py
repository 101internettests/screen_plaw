import os
import allure
import uuid
import sys
import time
import logging
from playwright.sync_api import sync_playwright
from urls.url_main import urls, names, urls_prod, names_stage
from pages.screen_page import ScreenPage
HEADLESS = True if os.getenv("HEADLESS") == "True" else False


@allure.title("Скриншоты 101")
class TestSearchChrome:
    @allure.title("Скриншоты 101 стэйдж")
    def test_screenshot_stage_main(self):
        # Настройка логирования для realtime вывода в консоль Jenkins/pytest
        logger = logging.getLogger("test_screenshot_stage_main")
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%H:%M:%S")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            logger.propagate = False

        total = len(names_stage)
        logger.info(f"Старт теста: всего страниц {total}")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS)
            context = browser.new_context(ignore_https_errors=True)
            page = context.new_page()

            for idx, (screen, name) in enumerate(zip(urls, names_stage), start=1):
                start_ts = time.time()
                logger.info(f"[{idx}/{total}] Открываю URL: {screen}")
                try:
                    uuid4 = uuid.uuid4()
                    page.goto(screen)
                    open_ts = time.time()
                    logger.info(f"[{idx}/{total}] Страница загружена за {open_ts - start_ts:.2f} c. Обрабатываю контент…")

                    screen_page = ScreenPage(page=page)
                    screen_page.open_read_more_buttons()
                    screen_page.open_read_full_buttons()
                    screen_page.click_all_faq_buttons()
                    page.wait_for_timeout(2000)

                    page.set_viewport_size({"width": 1920, "height": 8000})
                    screenshot_path = f'{os.getenv("BASE_SAVING_PATH")}/screens/main_stage/{name}.png'
                    page.screenshot(path=screenshot_path)

                    end_ts = time.time()
                    logger.info(
                        f"[{idx}/{total}] Скриншот сохранён: {screenshot_path}. Время шага: {end_ts - start_ts:.2f} c"
                    )

                except Exception as e:
                    logger.error(f"[{idx}/{total}] Ошибка при обработке {screen}: {e}")

    @allure.title("Скриншоты 101 прод")
    def test_screenshot_prod_main(self):
        logger = logging.getLogger("test_screenshot_prod_main")
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", "%H:%M:%S")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            logger.propagate = False

        total = len(names)
        logger.info(f"Старт теста: всего страниц {total}")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS)
            context = browser.new_context(ignore_https_errors=True)
            page = context.new_page()

            for idx, (screen, name) in enumerate(zip(urls_prod, names), start=1):
                start_ts = time.time()
                logger.info(f"[{idx}/{total}] Открываю URL: {screen}")
                try:
                    uuid4 = uuid.uuid4()
                    page.goto(screen)
                    open_ts = time.time()
                    logger.info(f"[{idx}/{total}] Страница загружена за {open_ts - start_ts:.2f} c. Обрабатываю контент…")

                    screen = ScreenPage(page=page)
                    screen.open_read_more_buttons()
                    screen.open_read_full_buttons()
                    screen.click_all_faq_buttons()
                    page.wait_for_timeout(2000)
                    page.set_viewport_size({"width": 1920, "height": 8000})

                    screenshot_path = f'{os.getenv("BASE_SAVING_PATH")}/screens/main_prod/{name}.png'
                    page.screenshot(path=screenshot_path)

                    end_ts = time.time()
                    logger.info(
                        f"[{idx}/{total}] Скриншот сохранён: {screenshot_path}. Время шага: {end_ts - start_ts:.2f} c"
                    )

                except Exception as e:
                    logger.error(f"[{idx}/{total}] Ошибка при работе с {screen}: {e}")