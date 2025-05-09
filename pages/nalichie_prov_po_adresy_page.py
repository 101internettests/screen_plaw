import time
import allure
from locators.general_locators import UnsuccessfulLocators
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class UnsuccessfulPage(BasePage):

    @allure.title("Нажать на кнопку Повторить поиск по адресу")
    def click_button_repeat_search(self):
        self.page.locator(UnsuccessfulLocators.REPEAT_SEARCH).click()