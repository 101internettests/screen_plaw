import os
import allure
import uuid
from playwright.sync_api import sync_playwright
from urls.urls_pol import urls, names, urls_stage, names_stage
from pages.screen_page import ScreenPage

HEADLESS = True if os.getenv("HEADLESS") == "True" else False


@allure.title("Скриншоты Санкт-Петербурга")
class TestSearchChrome:
    @allure.title("Скриншоты Санкт-Петербурга прод")
    def test_screenshot_prod_pol(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS)
            context = browser.new_context()
            page = context.new_page()

            for screen, name in zip(urls, names):
                try:
                    uuid4 = uuid.uuid4()
                    page.goto(screen)
                    screen = ScreenPage(page=page)
                    screen.open_read_more_buttons()
                    screen.open_read_full_buttons()
                    screen.click_all_faq_buttons()
                    page.wait_for_timeout(2000)
                    page.set_viewport_size({"width": 1920, "height": 8000})

                    screenshot_path = f'{os.getenv("BASE_SAVING_PATH")}/screens/pol_prod/{name}.png'
                    page.screenshot(path=screenshot_path)
                    print(f"Скриншот сохранен: {screenshot_path}")

                except Exception as e:
                    print(f"Ошибка при работе с {screen}: {e}")

    @allure.title("Скриншоты Санкт-Петербурга стэйдж")
    def test_screenshot_stage_pol(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS)
            context = browser.new_context()
            page = context.new_page()

            for screen, name in zip(urls_stage, names_stage):
                try:
                    uuid4 = uuid.uuid4()
                    page.goto(screen)
                    screen = ScreenPage(page=page)
                    screen.open_read_more_buttons()
                    screen.open_read_full_buttons()
                    screen.click_all_faq_buttons()
                    page.wait_for_timeout(2000)
                    page.set_viewport_size({"width": 1920, "height": 8000})

                    screenshot_path = f'{os.getenv("BASE_SAVING_PATH")}/screens/pol_stage/{name}.png'
                    page.screenshot(path=screenshot_path)
                    print(f"Скриншот сохранен: {screenshot_path}")

                except Exception as e:
                    print(f"Ошибка при работе с {screen}: {e}")
