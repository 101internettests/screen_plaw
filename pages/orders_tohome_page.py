import time
import allure
import re
import random
from locators.tohome_page_locators import OrdersTohomeLocators
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class TohomePage(BasePage):
    @allure.title("Нажать на кнопку Не нашли свой регион")
    def click_on_not_address_block(self):
        self.page.locator(OrdersTohomeLocators.NOT_FOUND_YOUR_ADDRESS_BUTTON).click()

    @allure.title("Пол проверить переход на выбор адреса")
    def check_address_page_pol(self):
        expect(self.page.locator(OrdersTohomeLocators.ADDRESS_NOT_IN_BASE)).to_be_visible()

    @allure.title("Пол проверить переход на выбор адреса")
    def check_address_page_mol(self):
        expect(self.page.locator(OrdersTohomeLocators.ADDRESS_NOT_IN_BASE_MOL)).to_be_visible()