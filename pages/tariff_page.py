import time
import allure
import re
import random
from locators.mol_locators import ProvidersPage, Filters, TariffsInTariffPage
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class TariffPage(BasePage):
    @allure.title("Проверить наличие тега Домашний интернет")
    def check_tag_home_internet(self):
        expect(self.page.locator(ProvidersPage.TAG_HOME_INTERNET)).to_be_visible()
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(ProvidersPage.TAG_HOME_INTERNET).screenshot()
            allure.attach(screenshot, name="Tariff details Section Screenshot",
                          attachment_type=allure.attachment_type.PNG)

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

    @allure.title("Выбрать фильтр Цена до 1000 руб.")
    def choose_price_before_oneth(self):
        self.page.locator(Filters.PRICE_BEFORE_ONETH).click()

    @allure.title("Выбрать фильтр Выбрать все провайдеры")
    def choose_filter_all_providers(self):
        self.page.locator(Filters.CHOOSE_ALL_PROVIDERS).click()

    @allure.title("Выбрать фильтр Скорость интернета 200-500 мб")
    def choose_filter_speed_200(self):
        self.page.locator(Filters.SPEED_INTERNET_200_500).click()

    @allure.title("Нажать на кнопку Показать тарифы")
    def accept_button_show_filters(self):
        self.page.locator(Filters.BUTTON_SHOW_ALL_TARIFFS).click()

    @allure.title("Проверить, что фильтры применились")
    def check_accepted_filters(self):
        expect(self.page.locator(Filters.CHECK_FILTERS)).to_be_visible()

    @allure.title("Клинкуть по тарифу со скоростью 500 мб\с")
    def click_on_tariff_with_500(self):
        self.page.locator(TariffsInTariffPage.TARIFF_WITH_SPEED_500).click()

    @allure.title("Отправить заявку в попап")
    def send_popup_wait_for_call(self):
        time.sleep(3)
        self.page.locator(TariffsInTariffPage.PHONE_NUMBER_INPUT).fill("1111111111")
        self.page.locator(TariffsInTariffPage.BUTTON_SEND).click(timeout=5000)
