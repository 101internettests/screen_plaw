import os
import allure
import uuid
from playwright.sync_api import sync_playwright
from urls.urls_pol import urls, names, urls_stage, names_stage
from pages.screen_page import ScreenPage
from jenkins_config import get_browser_args, get_timeout, get_viewport, is_jenkins_environment

HEADLESS = True if os.getenv("HEADLESS") == "True" else False


@allure.title("Скриншоты Санкт-Петербурга")
class TestSearchChrome:
    @allure.title("Скриншоты Санкт-Петербурга прод")
    def test_screenshot_prod_pol(self):
        with sync_playwright() as p:
            # Улучшенные настройки браузера для Jenkins
            browser_args = get_browser_args()
            browser = p.chromium.launch(
                headless=HEADLESS,
                args=browser_args
            )
            viewport = get_viewport()
            context = browser.new_context(
                ignore_https_errors=True,
                viewport=viewport
            )
            page = context.new_page()

            for screen, name in zip(urls, names):
                try:
                    uuid4 = uuid.uuid4()
                    print(f"Обрабатываю страницу: {screen}")
                    
                    # Увеличенный таймаут для загрузки страницы
                    page_load_timeout = get_timeout('page_load')
                    page.goto(screen, wait_until='networkidle', timeout=page_load_timeout)
                    
                    # Ждем полной загрузки DOM
                    page.wait_for_load_state('domcontentloaded', timeout=page_load_timeout)
                    page.wait_for_load_state('networkidle', timeout=page_load_timeout)
                    
                    # Дополнительная проверка готовности страницы
                    page.wait_for_timeout(get_timeout('screenshot_wait'))
                    
                    screen_obj = ScreenPage(page=page)
                    screen_obj.open_read_more_buttons()
                    screen_obj.open_read_full_buttons()
                    screen_obj.click_all_faq_buttons()
                    
                    # Увеличенное время ожидания после кликов
                    page.wait_for_timeout(get_timeout('action_wait'))
                    
                    # Устанавливаем размер viewport перед скриншотом
                    page.set_viewport_size({"width": 1920, "height": 8000})
                    page.wait_for_timeout(2000)  # Ждем перерисовки

                    screenshot_path = f'{os.getenv("BASE_SAVING_PATH")}/screens/pol_prod/{name}.png'
                    page.screenshot(path=screenshot_path, full_page=True)
                    print(f"Скриншот сохранен: {screenshot_path}")

                except Exception as e:
                    print(f"Ошибка при работе с {screen}: {e}")
                    # Продолжаем с следующей страницей
                    continue

    @allure.title("Скриншоты Санкт-Петербурга стэйдж")
    def test_screenshot_stage_pol(self):
        with sync_playwright() as p:
            # Улучшенные настройки браузера для Jenkins
            browser_args = get_browser_args()
            browser = p.chromium.launch(
                headless=HEADLESS,
                args=browser_args
            )
            viewport = get_viewport()
            context = browser.new_context(
                ignore_https_errors=True,
                viewport=viewport
            )
            page = context.new_page()

            for screen, name in zip(urls_stage, names_stage):
                try:
                    uuid4 = uuid.uuid4()
                    print(f"Обрабатываю страницу: {screen}")
                    
                    # Увеличенный таймаут для загрузки страницы
                    page_load_timeout = get_timeout('page_load')
                    page.goto(screen, wait_until='networkidle', timeout=page_load_timeout)
                    
                    # Ждем полной загрузки DOM
                    page.wait_for_load_state('domcontentloaded', timeout=page_load_timeout)
                    page.wait_for_load_state('networkidle', timeout=page_load_timeout)
                    
                    # Дополнительная проверка готовности страницы
                    page.wait_for_timeout(get_timeout('screenshot_wait'))
                    
                    screen_obj = ScreenPage(page=page)
                    screen_obj.open_read_more_buttons()
                    screen_obj.open_read_full_buttons()
                    screen_obj.click_all_faq_buttons()
                    
                    # Увеличенное время ожидания после кликов
                    page.wait_for_timeout(get_timeout('action_wait'))
                    
                    # Устанавливаем размер viewport перед скриншотом
                    page.set_viewport_size({"width": 1920, "height": 8000})
                    page.wait_for_timeout(2000)  # Ждем перерисовки

                    screenshot_path = f'{os.getenv("BASE_SAVING_PATH")}/screens/pol_stage/{name}.png'
                    page.screenshot(path=screenshot_path, full_page=True)
                    print(f"Скриншот сохранен: {screenshot_path}")

                except Exception as e:
                    print(f"Ошибка при работе с {screen}: {e}")
                    # Продолжаем с следующей страницей
                    continue
