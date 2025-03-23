import time
import allure
import re
import random
from locators.mol_locators import ProvidersPage, Filters, TariffsInTariffPage
from locators.pol_locators import WindowLocators
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

    @allure.title("Выбрать билайн")
    def choose_filter_bilain_providers(self):
        self.page.locator(Filters.BILAIN_PROV).click()

    @allure.title("Выбрать Дом.ру")
    def choose_filter_house_providers(self):
        self.page.locator(Filters.HOUSE_RU_PROV).click()

    @allure.title("Выбрать Ростелеком")
    def choose_filter_rostel_providers(self):
        self.page.locator(Filters.ROSTELEKOM_PROV).click()

    @allure.title("Выбрать Мегафон")
    def choose_filter_megafone_providers(self):
        self.page.locator(Filters.MEGAFONE_PROV).click()

    @allure.title("Выбрать фильтр Скорость интернета 200-500 мб")
    def choose_filter_speed_200(self):
        self.page.locator(Filters.SPEED_INTERNET_200_500).click()

    @allure.title("Нажать на кнопку Показать тарифы")
    def accept_button_show_filters(self):
        self.page.locator(Filters.BUTTON_SHOW_ALL_TARIFFS).click()

    @allure.title("Нажать на кнопку Сортировка")
    def use_sorting_button(self):
        with allure.step("Открыть окно сортировки"):
            self.page.locator(Filters.SORTING_BUTTON).click()
        with allure.step("Выбрать По цене без учёта акций"):
            self.page.locator(Filters.BUTTON_PRISE_WITHOUT_SALE).click()

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

    @allure.title("Нажать на кнопку Показать еще")
    def show_more_button(self):
        self.page.locator(Filters.BUTTON_SHOW_MORE).click()

    @allure.title("Нажать на кнопку Показать еще 8 ")
    def show_more8_button(self):
        self.page.locator(Filters.BUTTON_SHOW_MORE_EIGHT).click()

    @allure.title("Кликнуть на кнопку на последнем тарифе")
    def click_on_lat_prov(self):
        elements = self.page.query_selector_all(Filters.LAST_LOCATOR)
        if not elements:
            raise Exception(f"Элементы с локатором не найдены")
        last_element = elements[-1]
        last_element.click()

    @allure.title("Отправить заявку в квиз")
    def quiz_send_appl(self):
        self.page.locator(Filters.QUIZ_INPUT).fill("1111111111")
        self.page.locator(Filters.BUTTON_SHOW_RESULT).click()


class WindowPopUp(BasePage):
    @allure.title("Выбрать В квартиру")
    def choose_in_flat(self):
        with allure.step("Нажать на кнопку В квартиру"):
            self.page.locator(WindowLocators.IN_FLAT_BUTTON).click()

    @allure.title("Выбрать Для бизнеса")
    def choose_in_business(self):
        with allure.step("Нажать на кнопку Для бизнеса"):
            self.page.locator(WindowLocators.IN_BUSINESS_BUTTON).click()
        with allure.step("Проверить кнопку поиска по тендеру"):
            expect(self.page.locator(WindowLocators.START_TENDER_BUTTON)).to_be_visible()

    @allure.title("Выбрать На дачу")
    def choose_in_sat(self):
        with allure.step("Нажать на кнопку На дачу"):
            self.page.locator(WindowLocators.IN_SAT_BUTTON).click()
        with allure.step("Проверить кнопку Все тарифы для дачи"):
            expect(self.page.locator(WindowLocators.ALL_TARIFFS_BUTTON)).to_be_visible()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(WindowLocators.INPUT_HOME_ADDRESS).fill("Английский")
            time.sleep(3)
            self.page.locator(WindowLocators.ENG_STREET).click()
            time.sleep(5)
            self.page.locator(WindowLocators.HOME_INPUT_UP).fill("7")
            time.sleep(3)
            self.page.locator(WindowLocators.STREET_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(WindowLocators.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_second(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(WindowLocators.INPUT_HOME_ADDRESS).fill("Солдата Корзуна")
            # time.sleep(3)
            self.page.locator(WindowLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(WindowLocators.HOME_INPUT_UP).fill("17")
            time.sleep(3)
            self.page.locator(WindowLocators.STREET_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(WindowLocators.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_shar(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(WindowLocators.INPUT_HOME_ADDRESS).fill("Шарикоподшипниковская")
            time.sleep(3)
            self.page.locator(WindowLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(WindowLocators.HOME_INPUT_UP).fill("1")
            time.sleep(3)
            self.page.locator(WindowLocators.STREET_REALLY_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(WindowLocators.FIND_TARIFFS).click()

