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
