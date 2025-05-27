from datetime import datetime
from typing import Optional
import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Получаем результат выполнения теста
    outcome = yield
    result = outcome.get_result()

    # Проверяем, завершился ли тест вызовом и он провалился
    if result.when == "call" and result.failed:
        # Получаем объект страницы Playwright
        page = item.funcargs.get("page", None)
        if page:
            try:
                # Имя файла по текущему времени
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                # Делаем скриншот (sync)
                screenshot_bytes = page.screenshot()

                # Прикрепляем скриншот к отчету Allure
                allure.attach(
                    screenshot_bytes,
                    name=f"screenshot_{timestamp}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Ошибка при создании скриншота: {e}")