import time
import random
import allure
import re
from locators.screen_locators import ScreenLocators
from locators.pol_locators import TariffsLocators, MainPageLocators, SelectRegion, AIPopUp, Header, Search, PopUpAfterSearch, ProvidersPage, ReviewWebSiteCat, ProvidersPage, PopUpFilltheAddress, ProvidersBlock, ReviewBlock
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
        time.sleep(2)
        self.page.locator(MainPageLocators.PHONE_NUMBER_INPUT).fill("1111111111")
        # with allure.step("Проверить ввелся ли номер"):
        #     expect(self.page.locator(MainPageLocators.CHECK_PHONE)).to_be_visible()
        self.page.locator(MainPageLocators.WAIT_FOR_CALL_BUTTON_SEND).click(timeout=5000)

    @allure.title("Проверить попапа после ввода данных")
    def check_success_popups(self):
        # expect(self.page.locator(MainPageLocators.POPUP_HEADER_SECOND)).to_be_visible()
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
            screenshot = self.page.screenshot()
            allure.attach(screenshot, name="Скриншот",
                      attachment_type=allure.attachment_type.PNG)

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

    @allure.title("Нажать на кнопку 'Больше о тарифе' на первом тарифе")
    def click_on_more_about_tariff_second(self):
        max_attempts = 6  # Максимальное количество попыток
        attempt = 0

        while attempt < max_attempts:
            try:
                # Проверяем, есть ли локатор MORE_ABOUT_TARIFF_BUTTON
                if self.page.locator(TariffsLocators.MORE_ABOUT_TARIFF_BUTTON).is_visible():
                    self.page.locator(TariffsLocators.MORE_ABOUT_TARIFF_BUTTON).click()
                    allure.attach("Успешно нажали на кнопку 'Больше о тарифе'", name="Успех")
                    return  # Выход из функции после успешного клика
                else:
                    allure.attach(f"Локатор 'Больше о тарифе' не найден. Попытка {attempt + 1}", name="Попытка")
            except Exception as e:
                allure.attach(f"Ошибка при поиске локатора 'Больше о тарифе': {e}", name="Ошибка")

            # Если локатор MORE_ABOUT_TARIFF_BUTTON не найден, перебираем нечётные индексы DETAILS_OF_TARIFF_BUTTON_new
            for index in range(1, 6, 2):  # Индексы 1, 3, 5 (нечётные)
                try:
                    # Формируем локатор с текущим индексом
                    details_locator = f"{TariffsLocators.DETAILS_OF_TARIFF_BUTTON_new}[{index}]"
                    if self.page.locator(details_locator).is_visible():
                        self.page.locator(details_locator).click()
                        allure.attach(f"Нажали на DETAILS_OF_TARIFF_BUTTON с индексом {index}. Попытка {attempt + 1}",
                                      name="Нажатие на DETAILS_OF_TARIFF_BUTTON")
                        # После клика снова проверяем MORE_ABOUT_TARIFF_BUTTON
                        break  # Выход из цикла for, чтобы вернуться к проверке MORE_ABOUT_TARIFF_BUTTON
                except Exception as e:
                    allure.attach(f"Ошибка при нажатии на DETAILS_OF_TARIFF_BUTTON с индексом {index}: {e}",
                                  name="Ошибка DETAILS_OF_TARIFF_BUTTON")

            attempt += 1

        allure.attach("Не удалось нажать на кнопку 'Больше о тарифе' после 6 попыток", name="Неудача")


    @allure.title("Проверить модальное окно больше о тарифе")
    def check_modal_window_more_about_tariffs(self):
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(TariffsLocators.DETAILS_OF_TARIFF_BUTTON).screenshot()
            allure.attach(screenshot, name="Tariff details Section Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.title("Закрыть модальное окно Больше о тарифе")
    def close_more_about_tariff(self):
        self.page.locator(TariffsLocators.POPUP_MORE_ABOUT_TARIFF).click()

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_first_tariff(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsLocators.PHONE_INPUT).type("1111111111")
        with allure.step("Заполнить адрес"):
            self.page.locator(TariffsLocators.INPUT_HOME_ADDRESS).fill("Энгельса")
            time.sleep(3)
            self.page.locator(TariffsLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(TariffsLocators.HOME_INPUT_UP).fill("7")
            time.sleep(3)
            self.page.locator(TariffsLocators.STREET_FIRST).click()
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address_second(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsLocators.PHONE_INPUT).type("1111111111")
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()

    @allure.title("Нажать на кнопку Найти все тарифы по адресу")
    def click_on_button_find_tariffs(self):
        self.page.locator(TariffsLocators.BUTTON_FIND_TARIFFS).click()

    @allure.title("Заполнить заявку на первом тарифе Гагарина 10")
    def fill_the_application_with_address_gagarina(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsLocators.PHONE_INPUT).type("1111111111")
            time.sleep(3)
        with allure.step("Заполнить адрес"):
            self.page.locator(TariffsLocators.INPUT_HOME_IN_TARIFF_ADDRESS).fill("Гагарина")
            time.sleep(3)
            self.page.locator(TariffsLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(TariffsLocators.HOME_IN_TARIFF_INPUT).fill("10")
            time.sleep(3)
            self.page.locator(TariffsLocators.STREET_TEN).click()
        with allure.step("Отправить заявку"):
            self.page.locator(ProvidersPage.SEND_APPLICATION_BUTTON).click()


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

    @allure.title("Выбрать тип поиска В квартиру - Карта покрытия")
    def choose_coverage_map(self):
        self.page.locator(Header.COVERAGE_MAP).click()

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

    @allure.title("Сделать поиск по заданному адресу")
    def search_vesennya(self):
        with allure.step("Вставить Весеннюю улицу"):
            time.sleep(5)
            self.page.locator(Search.STREET_INPUT_UP_THIRD).fill("Весенняя")
            time.sleep(5)
            self.page.locator(Search.SECOND_STREET).click()
        with allure.step("Вставить дом 42"):
            self.page.locator(Search.HOME_INPUT_UP_THIRD).fill("42")
            self.page.locator(Search.FIRST_STREET).click()
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(Search.BUTTON_FIND_TARIFFS_UP_THIRD).click()
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

    @allure.title("Проверить, что появился блок Выбрать свой район")
    def check_if_is_choose_area_block(self):
        expect(self.page.locator(Search.HEADER_CHOOSE_REGION)).to_be_visible()

    @allure.title("Выбрать Адмиралтейский район")
    def choose_admir_area(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.ADMIRALTEYSKIE_AREA).click()
        with allure.step("Проверить, что район выбрался"):
            expect(self.page.locator(Search.ADM_HEADER)).to_be_visible()
            expect(self.page.locator(Search.ADM_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать Юго-западный район")
    def choose_ugo_zapad_area(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.UGO_ZAPAD_AREA).click()
        with allure.step("Проверить, что район выбрался"):
            expect(self.page.locator(Search.UGO_ZAPAD_HEADER)).to_be_visible()

    @allure.title("Выбрать Адмиралтейский в хлебных крошках")
    def choose_admir_breadcrumps(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.ADM_BREADCRUMPS_STREET).click()

    @allure.title("Выбрать район Гатчина")
    def choose_gatchina(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.GATCHINA_AREA).click()
        with allure.step("Проверить, что район выбрался"):
            expect(self.page.locator(Search.GATCHINA_HEADER)).to_be_visible()

    @allure.title("Выбрать название улиц 1-13")
    def choose_more_streets(self):
        with allure.step("Выбрать"):
            self.page.locator(Search.LETTER_NUMS).click()
        with allure.step("Выбрать еще"):
            self.page.locator(Search.SHOW_MORE_BUTTON).click()

    @allure.title("Выбрать название улиц 1-27")
    def choose_more_27streets(self):
        with allure.step("Выбрать"):
            self.page.locator(Search.LETTER_NEW_NUMS).click()
        with allure.step("Выбрать еще"):
            self.page.locator(Search.SHOW_MORE_BUTTON).click()

    @allure.title("Выбрать Василеостровский район")
    def choose_vasil_area(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.VASILEOSTRV_AREA).click()
        with allure.step("Проверить, что район выбрался"):
            expect(self.page.locator(Search.VAS_HEADER)).to_be_visible()
            expect(self.page.locator(Search.VAS_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать улицу Английский пр-кт")
    def choose_eng_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.ENGLISH_PROSP_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.ENGLISH_HEADER)).to_be_visible()
            expect(self.page.locator(Search.ENGLISH_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать улицу Гороховая")
    def choose_gorox_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.GOROX_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.GOROX_HEADER)).to_be_visible()
            expect(self.page.locator(Search.GOROX_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать улицу Репина")
    def choose_repina_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.REPINA_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.REPINA_HEADER)).to_be_visible()
            expect(self.page.locator(Search.REPINA_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать улицу К.Маркса")
    def choose_marks_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.KARL_MARKS_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.MARKS_HEADER)).to_be_visible()
            expect(self.page.locator(Search.MARKS_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать улицу Щевченко")
    def choose_shev_street(self):
        with allure.step("Выбрать Щ"):
            self.page.locator(Search.SHOW_MORE_BUTTON).click()
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.SHEVCHENKO_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.SHEV_HEADER)).to_be_visible()
            expect(self.page.locator(Search.SHEVCHENKO_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать букву я")
    def choose_ya_letter(self):
        with allure.step("Выбрать букву Я"):
            self.page.locator(Search.LETTER_YA).click()

    @allure.title("Выбрать букву ю")
    def choose_u_letter(self):
        with allure.step("Выбрать букву Я"):
            self.page.locator(Search.LETTER_U).click()

    @allure.title("Выбрать букву Р")
    def choose_r_letter(self):
        with allure.step("Выбрать букву Я"):
            self.page.locator(Search.LETTER_R).click()

    @allure.title("Выбрать улицу Якубовича")
    def choose_ya_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.YAKUBOVICH_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.YAKU_HEADER)).to_be_visible()
            expect(self.page.locator(Search.YAKUBOVICH_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать улицу Петергофское ш")
    def choose_peter_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.PETERGOF_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.PETER_HEADER)).to_be_visible()

    @allure.title("Выбрать улицу Красноармейская")
    def choose_krasn_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.KRASN_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.KRASN_HEADER)).to_be_visible()

    @allure.title("Выбрать дом 33")
    def choose_three_house(self):
        with allure.step("Выбрать промежуток 24-38"):
            self.page.locator(Search.HOUSE_BUTTON).click()
        with allure.step("Выбрать дом 33"):
            self.page.locator(Search.THIRTY_THREE_HOUSE).click()

    @allure.title("Выбрать дом 55к1")
    def choose_five_house(self):
        with allure.step("Выбрать промежуток 19-78к"):
            self.page.locator(Search.HOUSE_1978_BUTTON).click()
        with allure.step("Выбрать дом 33"):
            self.page.locator(Search.FIFTY_FIVE_HOUSE).click()

    @allure.title("Выбрать дом 1")
    def choose_first_house(self):
        self.page.locator(Search.FIRST_HOUSE_BUTTON).click()

    @allure.title("Выбрать дом 27")
    def choose_twenty_seven_house(self):
        self.page.locator(Search.TWENTY_SEVEN_HOUSE_BUTTON).click()


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


class OpenPopUpAddress(BasePage):
    @allure.title("Проверить, что открылся попап по поиску")
    def check_popup_window(self):
        expect(self.page.locator(PopUpFilltheAddress.HEADER_WINDOW)).to_be_visible()

    @allure.title("Выбрать В квартиру")
    def choose_in_flat(self):
        with allure.step("Нажать на кнопку В квартиру"):
            self.page.locator(PopUpFilltheAddress.IN_FLAT_BUTTON).click()

    @allure.title("Выбрать Для бизнеса")
    def choose_in_business(self):
        with allure.step("Нажать на кнопку Для бизнеса"):
            self.page.locator(PopUpFilltheAddress.IN_BUSINESS_BUTTON).click()
        with allure.step("Проверить кнопку поиска по тендеру"):
            expect(self.page.locator(PopUpFilltheAddress.START_TENDER_BUTTON)).to_be_visible()

    @allure.title("Выбрать На дачу")
    def choose_in_sat(self):
        with allure.step("Нажать на кнопку На дачу"):
            self.page.locator(PopUpFilltheAddress.IN_SAT_BUTTON).click()
        with allure.step("Проверить кнопку Все тарифы для дачи"):
            expect(self.page.locator(PopUpFilltheAddress.ALL_TARIFFS_BUTTON)).to_be_visible()

    @allure.title("Сделать поиск по заданному адресу")
    def search_address(self):
        with allure.step("Вставить Весенняя улицу"):
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.STREET_INPUT).fill("Весенняя")
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.CHOOSE_SECOND).click()
        with allure.step("Вставить дом 12"):
            self.page.locator(PopUpFilltheAddress.HOME_INPUT).fill("1")
            self.page.locator(PopUpFilltheAddress.CHOOSE_FOUR).click()
        with allure.step("Удалить дом 12, выбрать 42"):
            self.page.locator(PopUpFilltheAddress.DELETE_HOUSE).click()
            self.page.locator(PopUpFilltheAddress.HOME_INPUT).fill("42")
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
            time.sleep(4)
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(TariffsLocators.INPUT_HOME_ADDRESS).fill("Английский")
            time.sleep(3)
            self.page.locator(TariffsLocators.ENG_STREET).click()
            time.sleep(5)
            self.page.locator(TariffsLocators.HOME_INPUT_UP).fill("7")
            time.sleep(3)
            self.page.locator(TariffsLocators.STREET_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_second(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(TariffsLocators.INPUT_HOME_ADDRESS).fill("Солдата Корзуна")
            # time.sleep(3)
            self.page.locator(TariffsLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(TariffsLocators.HOME_INPUT_UP).fill("17")
            time.sleep(3)
            self.page.locator(TariffsLocators.STREET_FIRST).click()
        with allure.step("Отправить заявку"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()


class BlockProviders(BasePage):
    @allure.title("Проверить блок Топ провайдеров интернета в СПБ")
    def check_providers_block(self):
        with allure.step("Проверить наличие блока"):
            expect(self.page.locator(ProvidersBlock.PROVIDERS_BLOCK)).to_be_visible()
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(ProvidersBlock.PROVIDERS_BLOCK).screenshot()
            allure.attach(screenshot, name="Providers block  Screenshot",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Открыть попап поиска по адресу с СатНет (третий тариф)")
    def click_search_sat(self):
        self.page.locator(ProvidersBlock.BUTTON_TARIFFS_ADDRESS).click()

    @allure.title("Нажать на кнопку Все провайдеры по адресу")
    def click_all_providers_button(self):
        self.page.locator(ProvidersBlock.ALL_PROVIDERS_BUTTON).click()

    @allure.title("Открыть попап поиска по адресу с Дом ру (Третий тариф)")
    def click_search_domru(self):
        self.page.locator(ProvidersBlock.BUTTON_TARIFFS_ADDRESS).click()


class ReviewBlockPage(BasePage):
    @allure.title("Проверить наличие блока отзывов")
    def check_review_block(self):
        with allure.step("Проверить, что заголовок есть на странице"):
            expect(self.page.locator(ReviewBlock.REVIEW_HEADER)).to_be_visible()
        with allure.step("Проверить, что выведен один отзыв"):
            review_num = self.page.locator(ReviewBlock.NUBER_OF_REVIEW).count()
            if review_num == 1:
                print("Локатор указывает ровно на один элемент.")
            else:
                print(f"Локатор указывает на {review_num} элементов.")

    @allure.title("Нажать на кнопку Еще отзывы")
    def click_button_more_reviews(self):
        self.page.locator(ReviewBlock.BUTTON_MORE_REVIEWS).click()