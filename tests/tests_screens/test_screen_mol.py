import allure
import uuid
from playwright.sync_api import sync_playwright
from urls.urls_msk import urls, names, urls_prod
from pages.screen_page import ScreenPage
HEADLESS = False


@allure.title("Скриншоты Москва")
class TestSearchChrome:
    @allure.title("Скриншоты Москва стэйдж")
    def test_screenshot_stage_mol(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS)
            context = browser.new_context(ignore_https_errors=True)
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

                    screenshot_path = f'C:/Users/Katerina/Desktop/screens/{name}.png'
                    page.screenshot(path=screenshot_path)
                    print(f"Скриншот сохранен: {screenshot_path}")

                except Exception as e:
                    print(f"Ошибка при работе с {screen}: {e}")

    @allure.title("Скриншоты Москва прод")
    def test_screenshot_prod_mol(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS)
            context = browser.new_context(ignore_https_errors=True)
            page = context.new_page()

            for screen, name in zip(urls_prod, names):
                try:
                    uuid4 = uuid.uuid4()
                    page.goto(screen)
                    screen = ScreenPage(page=page)
                    screen.open_read_more_buttons()
                    screen.open_read_full_buttons()
                    screen.click_all_faq_buttons()
                    page.wait_for_timeout(2000)
                    page.set_viewport_size({"width": 1920, "height": 8000})

                    screenshot_path = f'C:/Users/Katerina/Desktop/screens/{name}.png'
                    page.screenshot(path=screenshot_path)
                    print(f"Скриншот сохранен: {screenshot_path}")

                except Exception as e:
                    print(f"Ошибка при работе с {screen}: {e}")