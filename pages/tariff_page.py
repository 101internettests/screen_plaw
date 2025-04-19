import time
import allure
import re
import random
from locators.mol_locators import ProvidersPage, Filters, TariffsInTariffPage, MiddlePageLocators, ProvidersBlock
from locators.pol_locators import WindowLocators, TohomeMiddlePageSearch, PopUpFilltheAddress
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

    @allure.title("Заполнить заявку на втором тарифе на странице Тарифов")
    def fill_the_application_second_tariff(self):
        with allure.step("Кликнуть на кнопку с ценой на втором тарифе"):
            self.page.locator(ProvidersPage.SECOND_BUTTON_WITH_PRICE).click()
            time.sleep(4)
        with allure.step("Вставить номер и отправить"):
            self.page.locator(ProvidersPage.TELEPHONE_INPUT).type("1111111111")
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_second(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsInTariffPage.PHONE_NUMBER_INPUT).type("1111111111")
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_third(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_TARIFF).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsInTariffPage.PHONE_NUMBER_INPUT).type("1111111111")
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()

    @allure.title("Заполнить заявку на первом тарифе для ПОЛ")
    def fill_the_application_with_address_pol(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsInTariffPage.PHONE_NUMBER_INPUT).type("1111111111")
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()

    @allure.title("Выбрать тег Инернет и ТВ")
    def choose_tag_internet_tv(self):
        self.page.locator(Filters.TAG_INTERNET_TV).click()

    @allure.title("Выбрать фильтр Цена до 700 руб.")
    def choose_price_before_seven(self):
        self.page.locator(Filters.PRICE_BEFORE_SEVEN).click()

    @allure.title("Выбрать фильтр Цена до 1000 руб.")
    def choose_price_before_oneth(self):
        self.page.locator(Filters.PRICE_BEFORE_ONETH).click()

    @allure.title("Выбрать фильтр Выбрать все провайдеры")
    def choose_filter_all_providers(self):
        self.page.locator(Filters.CHOOSE_ALL_PROVIDERS).click()

    @allure.title("Выбрать Алмател")
    def choose_filter_almatel_providers(self):
        self.page.locator(Filters.ALMATEL_PROV).click()

    @allure.title("Выбрать МТС")
    def choose_filter_mts_providers(self):
        self.page.locator(Filters.MTS_PROV).click()

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

    @allure.title("Выбрать фильтр Скорость интернета 100-200 мб")
    def choose_filter_speed_100(self):
        self.page.locator(Filters.SPEED_INTERNET_100_200).click()

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

    @allure.title("Нажать на кнопку Сортировка")
    def use_sorting_button_speed(self):
        with allure.step("Открыть окно сортировки"):
            self.page.locator(Filters.SORTING_BUTTON).click()
        with allure.step("Выбрать По скорости"):
            self.page.locator(Filters.BUTTON_SPEED_BUTTON).click()

    @allure.title("Нажать на Детали тарифа на первом тарифе")
    def click_tariff_details_first_tariff(self):
        with allure.step("Нажать на кнопку Детали тарифа"):
            self.page.locator(Filters.TARIFF_DETAILS_BUTTON).click()
        with allure.step("Нажать на кнопку Больше о тарифе"):
            self.page.locator(Filters.MORE_ABOUT_TARIFF_BUTTON).click()
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(ProvidersBlock.PLACE_FOR_SCREEN).screenshot()
            allure.attach(screenshot, name="Providers block  Screenshot",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Нажать на кнопку Закрыть детали"):
            self.page.locator(Filters.CLOSE_DETAILS_BUTTON).click()

    @allure.title("Нажать на Детали тарифа на третьем тарифе")
    def click_tariff_details_four_tariff(self):
        with allure.step("Нажать на кнопку Детали тарифа"):
            self.page.locator(Filters.TARIFF_DETAILS_BUTTON_FOUR).click()

    @allure.title("Проверить, что фильтры применились")
    def check_accepted_filters(self):
        expect(self.page.locator(Filters.CHECK_FILTERS)).to_be_visible()

    @allure.title("Клинкуть по тарифу со скоростью 500 мб\с")
    def click_on_tariff_with_500(self):
        self.page.locator(TariffsInTariffPage.TARIFF_WITH_SPEED_500).click()

    @allure.title("Клинкуть по тарифу со скоростью 200 мб\с")
    def click_on_tariff_with_200(self):
        self.page.locator(TariffsInTariffPage.TARIFF_WITH_SPEED_200).click()

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

    @allure.title("Нажать на кнопку Показать 10 из 22")
    def show_more10_button(self):
        self.page.locator(Filters.BUTTON_SHOW_MORE_MOL).click()

    @allure.title("Нажать на кнопку Показать 2 из 22")
    def show_more2_button(self):
        self.page.locator(Filters.BUTTON_SHOW_MORE_MOL2).click()

    @allure.title("Нажать на кнопку Показать 10 из 30")
    def show_more10_from30_button(self):
        self.page.locator(Filters.BUTTON_SHOW_TEN_FROM_THIRTEEN).click()

    @allure.title("Кликнуть на кнопку на последнем тарифе")
    def click_on_lat_prov(self):
        elements = self.page.query_selector_all(Filters.LAST_LOCATOR)
        if not elements:
            raise Exception(f"Элементы с локатором не найдены")
        last_element = elements[-1]
        last_element.click()

    @allure.title("Кликнуть на кнопку на первом тарифе")
    def click_on_first_prov(self):
        self.page.locator(Filters.FIRST_LOCATOR).click()

    @allure.title("Кликнуть на кнопку на четвертом тарифе")
    def click_on_four_prov(self):
        self.page.locator(Filters.FOUR_LOCATOR).click()

    @allure.title("Отправить заявку в квиз")
    def quiz_send_appl(self):
        self.page.locator(Filters.QUIZ_INPUT).fill("1111111111")
        self.page.locator(Filters.BUTTON_SHOW_RESULT).click()

    # @allure.title("Заполнить заявку на первом тарифе на странице Тарифов c адресом")
    # def fill_the_application(self):
    #     with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
    #         self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
    #     with allure.step("Проверить наличие названий тарифа"):
    #         tariff_name = self.page.locator(ProvidersPage.TARIFF_NAME)
    #         tariff_text = tariff_name.inner_text()
    #         print(tariff_text)
    #     with allure.step("Проверить наличие названий тарифа из второй строки"):
    #         tariff_name = self.page.locator(ProvidersPage.TARIFF_NAME2)
    #         tariff_text = tariff_name.inner_text()
    #         print(tariff_text)
    #     with allure.step("Вставить номер, адрес и отправить"):
    #         self.page.locator(ProvidersPage.TELEPHONE_INPUT).type("1111111111")
    #         self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()


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

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_arbat38(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(WindowLocators.INPUT_HOME_ADDRESS).fill("Арбат")
            time.sleep(3)
            self.page.locator(WindowLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(WindowLocators.HOME_INPUT_UP).fill("38")
            time.sleep(3)
            self.page.locator(WindowLocators.STREET_REALLY_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(WindowLocators.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_only_house(self):
        with allure.step("Заполнить 19 дом"):
            self.page.locator(TohomeMiddlePageSearch.PLACEHOLDER_HOUSE).fill("19")
            time.sleep(3)
            self.page.locator(WindowLocators.STREET_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_only_house_forty_eight(self):
        with allure.step("Заполнить 48 дом"):
            self.page.locator(TohomeMiddlePageSearch.PLACEHOLDER_HOUSE).fill("48")
            time.sleep(3)
            self.page.locator(WindowLocators.STREET_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_hleb(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(WindowLocators.INPUT_HOME_ADDRESS).fill("Хлебный")
            time.sleep(3)
            self.page.locator(WindowLocators.XLEB_STREET).click()
            time.sleep(5)
            self.page.locator(WindowLocators.HOME_INPUT_UP).fill("14")
            time.sleep(3)
            self.page.locator(WindowLocators.STREET_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(WindowLocators.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_vasil(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(WindowLocators.INPUT_HOME_ADDRESS).fill("3-я В.О")
            time.sleep(3)
            self.page.locator(WindowLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(WindowLocators.HOME_INPUT_UP).fill("26")
            time.sleep(3)
            self.page.locator(WindowLocators.STREET_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(WindowLocators.FIND_TARIFFS).click()


class MiddlePage(BasePage):
    @allure.title("Сделать поиск по заданному адресу Новый Арбат")
    def fill_the_application_with_address_new_arbat(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(MiddlePageLocators.STREET_INPUT).fill("Новый Арбат")
            time.sleep(3)
            self.page.locator(MiddlePageLocators.THIRD_HOUSE).click()
            time.sleep(5)
            self.page.locator(MiddlePageLocators.HOME_INPUT).fill("6")
            time.sleep(3)
            self.page.locator(MiddlePageLocators.STREET_FIRST).click()
        with allure.step("Отправить заявку"):
            self.page.locator(MiddlePageLocators.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу Гороховая 22")
    def fill_the_application_with_address_new_gorox(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(MiddlePageLocators.STREET_INPUT).fill("Гороховая")
            time.sleep(3)
            self.page.locator(MiddlePageLocators.FIRST_HOUSE).click()
            time.sleep(5)
            self.page.locator(MiddlePageLocators.HOME_INPUT).fill("22")
            time.sleep(3)
            self.page.locator(MiddlePageLocators.STREET_FIRST).click()
        with allure.step("Отправить заявку"):
            self.page.locator(MiddlePageLocators.FIND_TARIFFS).click()
