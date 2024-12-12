# import allure
from typing import Optional
from playwright.sync_api import expect, Request, Page


class BasePage:
    def __init__(self, page: Optional[Page] = None):
        self.page = page
