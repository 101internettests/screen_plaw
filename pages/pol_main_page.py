import allure
from locators.screen_locators import ScreenLocators
from locators.pol_locators import MainPageLocators, SelectRegion
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.title("Открыть окошко Селект региона")
    def open_select_region_window(self):
        with allure.step("Проверить, что кнопка есть на странице и в ней есть текст"):
            expect(self.page.locator(MainPageLocators.RegionConfirmPopup)).to_be_visible()
            expect(self.page.locator(MainPageLocators.RegionConfirnPopupText)).to_have_text()
        with allure.step("Нажать на селект регион"):
            self.page.locator(MainPageLocators.RegionConfirmPopup).click()

    @allure.title("Проверить, что на главной странице в хедере выбрана Ленинградская область")
    def check_header_city(self):
        expect(self.page.locator(SelectRegion.LENINGRADSKAYA_OBLAST)).to_be_visible()
        expect(self.page.locator(SelectRegion.LENINGRADSKAYA_OBLAST)).to_have_text("Ленинградская область")

    @allure.title("Проверить, что регион сменился на Ленинградскую область")
    def check_main_page_has_leningrad_region(self):
        with allure.step("Проверить, что в заголовках есть Лен. область"):
            locators = [
                MainPageLocators.HEADER,
                MainPageLocators.PIN_SEARCH_CITY,
                MainPageLocators.FUTER_CITY
            ]
            for locator in locators:
                expect(self.page.locator(locator)).to_have_text("Ленинградская область")
        with allure.step("Проверить, что в сео заголовках есть Лен. область"):
            for index in range(2):
                expect(self.page.locator(MainPageLocators.SEO_HEADER_CITY).nth(index)).to_have_text("Ленинградская область")


class SelectRegionPage(BasePage):
    @allure.title("Проверить, что страница Селект регион загрузилась и в ней есть элементы")
    def check_select_region_page(self):
        with allure.step("Проверить, что элементы есть на странице"):
            locators = [
                SelectRegion.INPUT_SELECT_REGION,
                SelectRegion.MAIN_LETTERS_SELECT,
                SelectRegion.CITIES_LOCATOR,
                SelectRegion.CLOSE_BUTTON_ELEMENT
            ]
            for locator in locators:
                expect(self.page.locator(locator)).to_be_visible()

        with allure.step("Проверить, что в элементах есть текст"):
            new_locators = [
                SelectRegion.CITIES_LOCATOR,
                SelectRegion.CLOSE_BUTTON_ELEMENT
            ]
            for news in new_locators:
                locator_with_text = expect(self.page.locator(news)).to_have_text()
                print(locator_with_text)

    @allure.title("Найти Ленинградскую область в поиске")
    def choose_leningrad_region(self):
        with allure.step("Вставить Ленинградскую область в инпут"):
            self.page.locator(SelectRegion.INPUT_SELECT_REGION).fill("Ленинградская область")
        with allure.step("Проверить, что текст вставился"):
            expect(self.page.locator(SelectRegion.INPUT_SELECT_REGION)).to_have_value("Ленинградская область")
        with allure.step("Выбрать Ленинградскую область в поиске"):
            self.page.locator(SelectRegion.LENINGRADSKAYA_OBLAST).click()