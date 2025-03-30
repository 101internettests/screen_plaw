import time
import allure
from locators.mol_locators import PopUpFilltheAddress, MapCoverage
from pages.base_page import BasePage


class MapCoveragePage(BasePage):
    @allure.title("Сделать поиск по заданному адресу")
    def search_address(self):
        with allure.step("Вставить Шарикоподшипниковская улицу"):
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.STREET_INPUT).fill("Шарикоподшипниковская")
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
        with allure.step("Вставить дом 1"):
            self.page.locator(PopUpFilltheAddress.HOME_INPUT).fill("1")
            self.page.locator(PopUpFilltheAddress.CHOOSE_SECOND).click()
            time.sleep(4)
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу с главного поиска")
    def search_address_arbat(self):
        with allure.step("Вставить Шарикоподшипниковская улицу"):
            time.sleep(5)
            self.page.locator(MapCoverage.STREET_INPUT).fill("Арбат")
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
        with allure.step("Вставить дом 1"):
            self.page.locator(MapCoverage.HOME_INPUT).fill("111")
            self.page.locator(PopUpFilltheAddress.CHOOSE_NEGATIVE_HOUSE).click()
            time.sleep(4)
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(MapCoverage.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу с главного поиска")
    def search_address_eng(self):
        with allure.step("Вставить Шарикоподшипниковская улицу"):
            time.sleep(5)
            self.page.locator(MapCoverage.STREET_INPUT).fill("Английский")
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
        with allure.step("Вставить дом 1"):
            self.page.locator(MapCoverage.HOME_INPUT).fill("7")
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
            time.sleep(4)
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(MapCoverage.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу с главного поиска")
    def search_address_gor(self):
        with allure.step("Вставить Гороховую улицу"):
            time.sleep(5)
            self.page.locator(MapCoverage.STREET_INPUT).fill("Гороховая")
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
        with allure.step("Вставить дом 222"):
            self.page.locator(MapCoverage.HOME_INPUT).fill("222")
            self.page.locator(PopUpFilltheAddress.CHOOSE_NEGATIVE_HOUSE_SECOND).click()
            time.sleep(4)
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(MapCoverage.FIND_TARIFFS).click()

    @allure.title("В неудачном попапе нажать на кнопку Найти")
    def put_on_search_button(self):
        self.page.locator(MapCoverage.SEARCH_BUTTON).click()