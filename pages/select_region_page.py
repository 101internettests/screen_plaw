import time
import allure
from locators.select_region_page import SelectPageLocators
from pages.base_page import BasePage


class SelectRegionPage(BasePage):
    @allure.title("Выбрать город Москва")
    def choose_moscow(self):
        self.page.locator(SelectPageLocators.MOSCOW).click()

    @allure.title("Выбрать город Санкт-Петербург")
    def choose_saintp(self):
        self.page.locator(SelectPageLocators.PITER).click()