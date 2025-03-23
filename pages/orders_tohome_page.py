import time
import allure
import re
import random
from locators.tohome_page_locators import OrdersTohomeLocators
from locators.pol_locators import Search, TohomeMiddlePageSearch, TariffsLocators, ProvidersPage, WindowLocators
from locators.mol_locators import TariffsInTariffPage
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

    @allure.title("Сделать поиск по заданному адресу")
    def search_gorokhovaya(self):
        with allure.step("Вставить Гороховую улицу"):
            time.sleep(5)
            self.page.locator(TohomeMiddlePageSearch.VISIBLE_TEXT).click()
            self.page.locator(TohomeMiddlePageSearch.PLACEHOLDER_STREET).fill("Горохов")
            time.sleep(5)
            self.page.locator(TohomeMiddlePageSearch.GOROXOWAYA_STREET).click()
        with allure.step("Вставить дом 22"):
            self.page.locator(TohomeMiddlePageSearch.PLACEHOLDER_HOUSE).fill("22")
            self.page.locator(Search.STREET_TWENTYTWO).click()
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(TohomeMiddlePageSearch.BUTTON_FIND_TARIFFS_UP).click()
            time.sleep(4)


class TohomePolPage(BasePage):
    @allure.title("Проверить заголовок Тарифы в Санкт-Петербурге")
    def check_header_pol(self):
        expect(self.page.locator(TohomeMiddlePageSearch.VISIBLE_TEXT)).to_be_visible()

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_vesn(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(TohomeMiddlePageSearch.INPUT_HOME_ADDRESS).fill("Весенняя")
            time.sleep(3)
            self.page.locator(TohomeMiddlePageSearch.SECOND_STREET).click()
            time.sleep(5)
            self.page.locator(TohomeMiddlePageSearch.HOME_INPUT_UP).fill("42")
            time.sleep(3)
            self.page.locator(TariffsLocators.GUS_STREET).click()
        with allure.step("Отправить заявку"):
            self.page.locator(WindowLocators.FIND_TARIFFS).click()

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_vesn_second(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsLocators.PHONE_INPUT).type("1111111111")
            self.page.locator(TohomeMiddlePageSearch.INPUT_HOME_ADDRESS).fill("Весенняя")
            time.sleep(3)
            self.page.locator(TohomeMiddlePageSearch.SECOND_STREET).click()
            time.sleep(5)
            self.page.locator(TohomeMiddlePageSearch.HOME_INPUT_UP).fill("42")
            time.sleep(3)
            self.page.locator(TariffsLocators.GUS_STREET).click()
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()


class TohomeMol(BasePage):
    @allure.title("Проверить заголовок Тарифы в Москве")
    def check_header_mol(self):
        expect(self.page.locator(TohomeMiddlePageSearch.VISIBLE_TEXT_MSK)).to_be_visible()


    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_gag(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(TohomeMiddlePageSearch.INPUT_HOME_ADDRESS).fill("Гагарина")
            time.sleep(3)
            self.page.locator(TohomeMiddlePageSearch.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(TohomeMiddlePageSearch.HOME_INPUT_UP).fill("9")
            time.sleep(3)
            self.page.locator(TariffsLocators.GUS_STREET).click()
        with allure.step("Отправить заявку"):
            self.page.locator(WindowLocators.FIND_TARIFFS).click()

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_vesn_second(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsLocators.PHONE_INPUT).type("1111111111")
            self.page.locator(TohomeMiddlePageSearch.INPUT_HOME_ADDRESS).fill("Текстильщиков")
            time.sleep(3)
            self.page.locator(TariffsLocators.ENG_STREET).click()
            time.sleep(5)
            self.page.locator(TohomeMiddlePageSearch.HOME_INPUT_UP).fill("1")
            time.sleep(3)
            self.page.locator(TariffsLocators.SIX_STREET).click()
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_mol(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsInTariffPage.PHONE_NUMBER_INPUT).type("1111111111")
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()