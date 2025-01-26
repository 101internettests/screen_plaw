import time
import allure
import re
from locators.pol_locators import OrdersSatPage
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class SatPage(BasePage):
    @allure.title("Проверить хлебные крошки")
    def check_breadcrumbs(self):
        expect(self.page.locator(OrdersSatPage.BREADCRUMBS_INTERNET_FOR_SAT)).to_be_visible()
        expect(self.page.locator(OrdersSatPage.BREADCRUMBS_CONNECT_INTERNET)).to_be_visible()

    @allure.title("Перейти на главную страницу")
    def return_to_the_main_page(self):
        self.page.locator(OrdersSatPage.BREADCRUMBS_CONNECT_INTERNET).click()