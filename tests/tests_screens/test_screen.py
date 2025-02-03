import allure
import uuid
from playwright.sync_api import Page, expect, sync_playwright
from pages.urls_page import urls, names
from pages.screen_page import ScreenPage
HEADLESS = False


@allure.title("Скриншоты Санкт-Петербурга прод")
class TestSearchChrome:
    def test_screenschot(self):
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

                    screenshot_path = f'C:/Users/Katerina/Desktop/screens/{name}.png'
                    page.screenshot(path=screenshot_path)
                    print(f"Скриншот сохранен: {screenshot_path}")

                except Exception as e:
                    print(f"Ошибка при работе с {screen}: {e}")