import time
import random
import allure
import re
from locators.screen_locators import ScreenLocators
from locators.pol_locators import MainPageLocators, SelectRegion, AIPopUp, Header, Search, PopUpAfterSearch, TariffsLocators, ReviewWebSiteCat
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.title("Открыть окошко Селект региона")
    def open_select_region_window(self):
        with allure.step("Проверить, что кнопка есть на странице и в ней есть текст"):
            expect(self.page.locator(MainPageLocators.RegionConfirmPopup)).to_be_visible()
            # expect(self.page.locator(MainPageLocators.RegionConfirnPopupText)).to_have_text()
        with allure.step("Нажать на селект регион"):
            self.page.locator(MainPageLocators.RegionConfirmPopup).click()

    @allure.title("Проверить, что на главной странице в хедере выбрана Ленинградская область")
    def check_header_city(self):
        expect(self.page.locator(SelectRegion.LENINGRADSKAYA_OBLAST)).to_be_visible()
        expect(self.page.locator(SelectRegion.LENINGRADSKAYA_OBLAST)).to_have_text("Ленинградская область")

    @allure.title("Проверить, что на главной странице в хедере выбран г. Сертолово")
    def check_header_sertolovo(self):
        expect(self.page.locator(MainPageLocators.SERTOLOVO_HEADER)).to_be_visible()
        expect(self.page.locator(MainPageLocators.SERTOLOVO_HEADER)).to_have_text("Подключить домашний интернет в г. Сертолово (Ленинградская область)")

    @allure.title("Проверить, что регион сменился на Ленинградскую область")
    def check_main_page_has_leningrad_region(self):
        with allure.step("Проверить, что в заголовках есть Лен. область"):
            locators = [
                MainPageLocators.HEADER,
                # MainPageLocators.PIN_SEARCH_CITY,
                # MainPageLocators.FUTER_CITY
            ]
            for locator in locators:
                # Проверяем, что текст содержит 'Ленинградская область'
                expect(self.page.locator(locator)).to_have_text(re.compile(r".*Ленинградской области.*"))
        with allure.step("Проверить, что в заголовках есть Лен. область"):
            locators = [
                # MainPageLocators.HEADER,
                MainPageLocators.PIN_SEARCH_CITY,
                MainPageLocators.FUTER_CITY
            ]
            for locator in locators:
                # Проверяем, что текст содержит 'Ленинградская область'
                expect(self.page.locator(locator)).to_have_text(re.compile(r".*Ленинградская область.*"))

    @allure.title("Проверить наличие Кота переносителя наверх")
    def check_cat_upper(self):
        expect(self.page.locator(MainPageLocators.HEADER_PAGE_CATBUTTON)).to_be_visible()
        expect(self.page.locator(MainPageLocators.BUTTON_GO_UP)).to_be_visible()
        with allure.step("Перенестись наверх"):
            self.page.locator(MainPageLocators.BUTTON_GO_UP).click()
            time.sleep(5)

    @allure.title("Сделать скриншот")
    def make_screenshot(self):
        screenshot = self.page.locator(MainPageLocators.HEADER).screenshot()
        allure.attach(screenshot, name="Tariffs Section Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.title("Открыть попап для отправки заявки")
    def open_popup_wait_for_call(self):
        self.page.locator(MainPageLocators.WAIT_FOR_CALL_BUTTON_OPEN).click()

    @allure.title("Открыть попап для отправки заявки из футера")
    def open_popup_wait_for_call_footer(self):
        self.page.locator(MainPageLocators.WAIT_FOR_CALL_BUTTON_OPEN_FOOTER).click(timeout=5000)

    @allure.title("Отправить заявку в попап")
    def send_popup_wait_for_call(self):
        self.page.locator(MainPageLocators.PHONE_NUMBER_INPUT).fill("1111111111")
        self.page.locator(MainPageLocators.WAIT_FOR_CALL_BUTTON_SEND).click(timeout=5000)

    @allure.title("Проверить два попапа после ввода данных")
    def check_success_popups(self):
        expect(self.page.locator(MainPageLocators.POPUP_HEADER_SECOND)).to_be_visible()
        expect(self.page.locator(MainPageLocators.POPUP_HEADER_LAST)).to_be_visible()

    @allure.title("Закрыть попап для отправки заявки")
    def close_popup_wait_for_call(self):
        self.page.locator(MainPageLocators.CLOSE_POPUP_BUTTON).click()

    @allure.title("Проверить Котобаннер")
    def check_cat_ai(self):
        expect(self.page.locator(AIPopUp.BANNER_WITH_CAT)).to_be_visible()
        expect(self.page.locator(AIPopUp.CAT_HEADER)).to_be_visible()

    @allure.title("Нажать на кнопку помощи кота аи")
    def use_cat_ai_help(self):
        with allure.step("Проверить, что элементы есть на странице"):
            self.page.locator(AIPopUp.HELP_BUTTON).click()
        with allure.step("Проверить, что сработал негативный попап"):
            expect(self.page.locator(AIPopUp.UNSUCCESSFUL_ALLERT)).to_be_visible()

    @allure.title("Выбрать Сертолово в поиске")
    def choose_sertolovo(self):
        with allure.step("Вставить Сер в инпут"):
            self.page.locator(SelectRegion.INPUT_SELECT_REGION).fill("Сер")
        with allure.step("Проверить, что текст вставился"):
            expect(self.page.locator(SelectRegion.INPUT_SELECT_REGION)).to_have_value("Сер")
        with allure.step("Выбрать Сертолово в поиске"):
            self.page.locator(SelectRegion.SERTOLOVO).click()
            screenshot = self.page.screenshot()
            allure.attach(screenshot, name="Скриншот после выбора Сертолово",
                          attachment_type=allure.attachment_type.PNG)


class TariffsSection(BasePage):
    @allure.title("Проверить наличие блока тарифов")
    def check_tariffs_section(self):
        with allure.step("Проверить, что блок есть на странице"):
            expect(self.page.locator(TariffsLocators.TARIFF_LIST)).to_be_visible()
        with allure.step("Посчитать количество тарифов в блоке"):
            tariff_cards = self.page.locator(TariffsLocators.TARIFF_CARD)
            tariff_count = tariff_cards.count()
            allure.attach(f"Количество тарифов: {tariff_count}", name="Tariff Count",
                          attachment_type=allure.attachment_type.TEXT)
        with allure.step("Сделать скриншот блока тарифов"):
            screenshot = self.page.locator(TariffsLocators.TARIFF_LIST).screenshot()
            allure.attach(screenshot, name="Tariffs Section Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.title("Выписать цены с кнопок")
    def find_price_in_tariffs(self):
        elements = self.page.query_selector_all(TariffsLocators.PRICE_IN_TARIFFS)
        texts = [element.text_content() for element in elements]
        for text in texts:
            print(text)

    @allure.title("Нажать Детали тарифа на первом тарифе")
    def click_on_tariff_details(self):
        self.page.locator(TariffsLocators.DETAILS_OF_TARIFF_BUTTON).click()
        with allure.step("Проверить, что заголовки есть в деталях"):
            expect(self.page.locator(TariffsLocators.CONNECTION_INFO)).to_be_visible()
            expect(self.page.locator(TariffsLocators.ROUTER_INF0)).to_be_visible()
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(TariffsLocators.DETAILS_OF_TARIFF_BUTTON).screenshot()
            allure.attach(screenshot, name="Tariff details Section Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.title("Нажать на кнопку Больше о тарифе на первом тарифе")
    def click_on_more_about_tariff(self):
        self.page.locator(TariffsLocators.MORE_ABOUT_TARIFF_BUTTON).click()

    @allure.title("Проверить модальное окно больше о тарифе")
    def check_modal_window_more_about_tariffs(self):
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(TariffsLocators.DETAILS_OF_TARIFF_BUTTON).screenshot()
            allure.attach(screenshot, name="Tariff details Section Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.title("Закрыть модальное окно Больше о тарифе")
    def close_more_about_tariff(self):
        self.page.locator(TariffsLocators.POPUP_MORE_ABOUT_TARIFF).click()

class SelectRegionPage(BasePage):
    @allure.title("Проверить, что страница Селект регион загрузилась и в ней есть элементы")
    def check_select_region_page(self):
        with allure.step("Проверить, что элементы есть на странице"):
            locators = [
                SelectRegion.INPUT_SELECT_REGION,
                # SelectRegion.MAIN_LETTERS_SELECT,
                # SelectRegion.CITIES_LOCATOR,
                SelectRegion.CLOSE_BUTTON_ELEMENT
            ]
            for locator in locators:
                expect(self.page.locator(locator)).to_be_visible()

        # with allure.step("Проверить, что в элементах есть текст"):
        #     new_locators = [
        #         SelectRegion.CITIES_LOCATOR,
        #         SelectRegion.CLOSE_BUTTON_ELEMENT
        #     ]
        #     for news in new_locators:
        #         text = self.page.locator(news).text_content()
        #         assert text is not None and text.strip(), f"Локатор {news} не содержит текста"

    @allure.title("Выбрать Ленинградскую область в поиске")
    def choose_leningrad_region(self):
        with allure.step("Вставить Ленинградскую область в инпут"):
            self.page.locator(SelectRegion.INPUT_SELECT_REGION).fill("Ленинградская область")
        with allure.step("Проверить, что текст вставился"):
            expect(self.page.locator(SelectRegion.INPUT_SELECT_REGION)).to_have_value("Ленинградская область")
        with allure.step("Выбрать Ленинградскую область в поиске"):
            self.page.locator(SelectRegion.LENINGRADSKAYA_OBLAST).click()


class SearchFromMain(BasePage):
    @allure.title("Выбрать тип поиска В квартиру")
    def choose_type_search_flat(self):
        self.page.locator(Header.IN_FLAT_BUTTON).click()

    @allure.title("Выбрать тип поиска Для бизнеса")
    def choose_type_search_business(self):
        self.page.locator(Header.IN_BUSINESS_BUTTON).click()

    @allure.title("Нажать на кнопку Запустить тендер на поиск")
    def click_tender_button(self):
        self.page.locator(Header.START_TENDER_BUTTON).click()

    @allure.title("Выбрать тип поиска На дачу")
    def choose_type_search_garden(self):
        self.page.locator(Header.IN_GARDEN_BUTTON).click()

    @allure.title("Нажать на кнопку Запустить тендер на по Даче")
    def click_all_garden_tariffs(self):
        self.page.locator(Header.GARDEN_TENDER_BUTTON).click()

    @allure.title("Сделать поиск по заданному адресу")
    def search_gorokhovaya(self):
        with allure.step("Вставить Гороховую улицу"):
            time.sleep(5)
            self.page.locator(Search.STREET_INPUT_UP).fill("Горохов")
            time.sleep(5)
            self.page.locator(Search.GOROXOWAYA_STREET).click()
        with allure.step("Вставить дом 22"):
            self.page.locator(Search.HOME_INPUT_UP).fill("22")
            self.page.locator(Search.STREET_TWENTYTWO).click()
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(Search.BUTTON_FIND_TARIFFS_UP).click()
            time.sleep(4)

    @allure.title("Проверить, что появился квиз")
    def check_quiz(self):
        with allure.step("Проверить наличие текста"):
            expect(self.page.locator(PopUpAfterSearch.TEXT_IN_POPUP)).to_be_visible()

    @allure.title("Закрыть квиз")
    def close_quiz(self):
        self.page.locator(PopUpAfterSearch.CLOSE_QUIZ).click()

    @allure.title("Отправить заявку в квиз")
    def quiz_send_appl(self):
        self.page.locator(PopUpAfterSearch.INPUT_QUIZ_TEXT).fill("1111111111")
        self.page.locator(PopUpAfterSearch.BUTTON_SHOW_RESULT).click()


class ReviewCatPopup(BasePage):
    @allure.title("Открыт попап Как вам наш сайта?")
    def open_popup_cat_website(self):
        self.page.locator(ReviewWebSiteCat.CLICK_ON_LOGO).click()

    @allure.title("Нажать на одного из пяти котиков и оставить отзыв")
    def leave_feedback_cat(self):
        with allure.step("Нажать на одного из двух котиков"):
            cats_empji = self.page.locator(ReviewWebSiteCat.CLICK_ON_RANDOM_CAT)
            count = cats_empji.count()
            if count == 0:
                print("Нет доступных элементов для клика.")
                return
            random_index = random.randint(0, count - 1)
            cats_empji.nth(random_index).click()
        with allure.step("Вставить тестовый текст"):
            self.page.locator(ReviewWebSiteCat.TEXTAREA_IN_REVIEW).fill("Тестовая обратная связь")
        with allure.step("Нажать на кнопку Отправить"):
            self.page.locator(ReviewWebSiteCat.BUTTON_SEND).click()
        with allure.step("Проверить окно обратной связи"):
            expect(self.page.locator(ReviewWebSiteCat.TEXT_IN_POPUP)).to_be_visible()
        with allure.step("Проверить, что окно обратной связи исчезло"):
            time.sleep(7)
            expect(self.page.locator(ReviewWebSiteCat.TEXT_IN_POPUP)).not_to_be_visible()