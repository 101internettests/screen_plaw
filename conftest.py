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


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page: Optional[Page] = None):
    """
    Автоматически делает скриншот при падении теста и добавляет в Allure отчёт.
    Работает для всех тестов, где доступна фикстура page.
    """
    yield

    # Проверяем, что тест упал и есть доступ к page
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed and page:
        # Генерируем имя файла
        test_name = request.node.name
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"{test_name}_FAILED_{timestamp}.png"

        # Делаем скриншот
        screenshot_bytes = page.screenshot(full_page=True)

        # Добавляем в Allure отчёт
        allure.attach(
            screenshot_bytes,
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )


# Хук для сохранения результатов теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)