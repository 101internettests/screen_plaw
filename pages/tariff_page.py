import time
import allure
import re
import random
from locators.mol_locators import ProvidersPage
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class TariffPage(BasePage):
    @allure.title("Проверить наличие тега Домашний интернет")
    def check_tag_home_internet(self):
        expect(self.page.locator(ProvidersPage.TAG_HOME_INTERNET)).to_be_visible()
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(ProvidersPage.TAG_HOME_INTERNET).screenshot()
            allure.attach(screenshot, name="Tariff details Section Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.title("Заполнить заявку на первом тарифе на странице Тарифов")
    def fill_the_application(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
        with allure.step("Проверить наличие названий тарифа"):
            tariff_name = self.page.locator(ProvidersPage.TARIFF_NAME)
            tariff_text = tariff_name.inner_text()
            print(tariff_text)
        with allure.step("Проверить наличие названий тарифа из второй строки"):
            tariff_name = self.page.locator(ProvidersPage.TARIFF_NAME2)
            tariff_text = tariff_name.inner_text()
            print(tariff_text)
        with allure.step("Вставить номер и отправить"):
            self.page.locator(ProvidersPage.TELEPHONE_INPUT).type("1111111111")
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()