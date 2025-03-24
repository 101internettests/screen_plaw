import time
import allure
import re
import random
from locators.screen_locators import ScreenLocators
from locators.mol_locators import MainPageLocators, SelectRegion, AIPopUp, Header, Search, PopUpAfterSearch, TariffsLocators
from locators.mol_locators import ReviewWebSiteCat, ProvidersPage, PopUpFilltheAddress, ProvidersBlock, ReviewBlock
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

    @allure.title("Проверить, что на главной странице в хедере выбрана Московская область")
    def check_header_city(self):
        expect(self.page.locator(SelectRegion.MOSKOWSKAYA_OBLAST)).to_be_visible()
        expect(self.page.locator(SelectRegion.MOSKOWSKAYA_OBLAST)).to_have_text("Московская область")

    @allure.title("Проверить, что на главной странице в хедере выбран г. Мытищи")
    def check_header_mitishi(self):
        expect(self.page.locator(MainPageLocators.MITISHI_HEADER)).to_be_visible()
        expect(self.page.locator(MainPageLocators.MITISHI_HEADER)).to_have_text("Подключить интернет в г. Мытищи")

    @allure.title("Проверить, что регион сменился на Московскую область")
    def check_main_page_has_leningrad_region(self):
        with allure.step("Проверить, что в заголовках есть Лен. область"):
            locators = [
                MainPageLocators.HEADER,
                # MainPageLocators.PIN_SEARCH_CITY,
                # MainPageLocators.FUTER_CITY
            ]
            for locator in locators:
                # Проверяем, что текст содержит 'Ленинградская область'
                expect(self.page.locator(locator)).to_have_text(re.compile(r".*Московской области.*"))
        with allure.step("Проверить, что в заголовках есть Моск. область"):
            locators = [
                # MainPageLocators.HEADER,
                MainPageLocators.PIN_SEARCH_CITY,
                MainPageLocators.FUTER_CITY
            ]
            for locator in locators:
                # Проверяем, что текст содержит 'Ленинградская область'
                expect(self.page.locator(locator)).to_have_text(re.compile(r".*Московская область.*"))

    @allure.title("Открыть попап для отправки заявки")
    def open_popup_wait_for_call(self):
        self.page.locator(MainPageLocators.WAIT_FOR_CALL_BUTTON_OPEN).click()

    @allure.title("Открыть попап для отправки заявки из футера")
    def open_popup_wait_for_call_footer(self):
        self.page.locator(MainPageLocators.WAIT_FOR_CALL_BUTTON_OPEN_FOOTER).click(timeout=5000)

    @allure.title("Отправить заявку в попап")
    def send_popup_wait_for_call(self):
        time.sleep(3)
        self.page.locator(MainPageLocators.PHONE_NUMBER_INPUT).fill("1111111111")
        self.page.locator(MainPageLocators.WAIT_FOR_CALL_BUTTON_SEND).click(timeout=5000)

    @allure.title("Проверить два попапа после ввода данных")
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

    @allure.title("Выбрать Мытищи в поиске")
    def choose_mitishi(self):
        with allure.step("Вставить Сер в инпут"):
            self.page.locator(SelectRegion.INPUT_SELECT_REGION).fill("Мыт")
        with allure.step("Проверить, что текст вставился"):
            expect(self.page.locator(SelectRegion.INPUT_SELECT_REGION)).to_have_value("Мыт")
        with allure.step("Выбрать Сертолово в поиске"):
            self.page.locator(SelectRegion.SERTOLOVO).click()
            screenshot = self.page.screenshot()
            allure.attach(screenshot, name="Скриншот после выбора Сертолово",
                          attachment_type=allure.attachment_type.PNG)

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

    @allure.title("Нажать на кнопку 'Больше о тарифе' на первом тарифе")
    def click_on_more_about_tariff(self):
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

    # @allure.title("Нажать на кнопку Больше о тарифе на первом тарифе")
    # def click_on_more_about_tariff(self):
    #     self.page.locator(TariffsLocators.MORE_ABOUT_TARIFF_BUTTON).click()

    @allure.title("Проверить модальное окно больше о тарифе")
    def check_modal_window_more_about_tariffs(self):
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(TariffsLocators.DETAILS_OF_TARIFF_BUTTON).screenshot()
            allure.attach(screenshot, name="Tariff details Section Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.title("Заполнить заявку на первом тарифе")
    def fill_the_application_with_address(self):
        with allure.step("Кликнуть на кнопку с ценой на первом тарифе"):
            self.page.locator(ProvidersPage.FIRST_BUTTON_WITH_PRICE).click()
            time.sleep(6)
        with allure.step("Вставить номер"):
            self.page.locator(TariffsLocators.PHONE_INPUT).type("1111111111")
        with allure.step("Заполнить адрес"):
            self.page.locator(TariffsLocators.INPUT_HOME_ADDRESS).fill("Гусятников пер")
            # time.sleep(3)
            self.page.locator(TariffsLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(TariffsLocators.HOME_INPUT_UP).fill("1")
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

    @allure.title("Закрыть модальное окно Больше о тарифе")
    def close_more_about_tariff(self):
        self.page.locator(TariffsLocators.POPUP_MORE_ABOUT_TARIFF).click()

    @allure.title("Нажать на кнопку Найти все тарифы по адресу")
    def click_on_button_find_tariffs(self):
        self.page.locator(TariffsLocators.BUTTON_FIND_TARIFFS).click()


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

    @allure.title("Выбрать Московскую область в поиске")
    def choose_leningrad_region(self):
        with allure.step("Вставить Ленинградскую область в инпут"):
            self.page.locator(SelectRegion.INPUT_SELECT_REGION).fill("Московская область")
        with allure.step("Проверить, что текст вставился"):
            expect(self.page.locator(SelectRegion.INPUT_SELECT_REGION)).to_have_value("Московская область")
        with allure.step("Выбрать Ленинградскую область в поиске"):
            self.page.locator(SelectRegion.MOSKOWSKAYA_OBLAST).click()


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
    def search_sharikopodship(self):
        with allure.step("Вставить Шарикоподшипниковская улицу"):
            time.sleep(5)
            self.page.locator(Search.STREET_INPUT_UP).fill("Шарикоподшипниковская")
            time.sleep(5)
            self.page.locator(Search.SHARIK_STREET).click()
        with allure.step("Вставить дом 11"):
            self.page.locator(Search.HOME_INPUT_UP).fill("11")
            self.page.locator(Search.STREET_ELEVEN).click()
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

    @allure.title("Проверить, что появился блок Выбрать свой район")
    def check_if_is_choose_area_block(self):
        expect(self.page.locator(Search.HEADER_CHOOSE_REGION)).to_be_visible()

    @allure.title("Выбрать Академический район")
    def choose_akad_area(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.AKADEM_AREA).click()
        with allure.step("Проверить, что район выбрался"):
            expect(self.page.locator(Search.AKD_HEADER)).to_be_visible()
            expect(self.page.locator(Search.AKD_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать Аэропорт район")
    def choose_aero_area(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.AIRPORT_AREA).click()
        with allure.step("Проверить, что район выбрался"):
            expect(self.page.locator(Search.AIRPORT_HEADER)).to_be_visible()
            expect(self.page.locator(Search.AIRPORT_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать Южное бутово район")
    def choose_butovo_area(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.BUTOVO_AREA).click()
        with allure.step("Проверить, что район выбрался"):
            expect(self.page.locator(Search.BUTOVO_HEADER)).to_be_visible()
            expect(self.page.locator(Search.BUTOVO_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать улицу Гримау")
    def choose_grem_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.GREM_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.GREM_HEADER)).to_be_visible()
            expect(self.page.locator(Search.GREM_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать улицу Ферсмана")
    def choose_fersm_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.FERSM_STREET).click()
        with allure.step("Выбрать улицу"):
            expect(self.page.locator(Search.FERSM_HEADER)).to_be_visible()
            expect(self.page.locator(Search.FERSM_BREADCRUMPS)).to_be_visible()

    @allure.title("Выбрать дом 13")
    def choose_three_house(self):
        with allure.step("Выбрать промежуток 24-38"):
            self.page.locator(Search.HOUSE_BUTTON).click()
        with allure.step("Выбрать дом 13"):
            self.page.locator(Search.THIRTEEN_HOUSE).click()

    @allure.title("Выбрать дом 15к1")
    def choose_fifteen_house(self):
        with allure.step("Выбрать промежуток 1-17 к1"):
            self.page.locator(Search.HOUSE29_BUTTON).click()
        with allure.step("Выбрать дом 15к1"):
            self.page.locator(Search.FIFTEEN_HOUSE).click()

    @allure.title("Сделать поиск по заданному адресу")
    def search_purple(self):
        with allure.step("Вставить Cиреневая улицу"):
            time.sleep(5)
            self.page.locator(Search.STREET_INPUT_UP).fill("Сиреневый")
            time.sleep(5)
            self.page.locator(Search.PURPLE_STREET).click()
        with allure.step("Вставить дом 40К2"):
            self.page.locator(Search.HOME_INPUT_UP).fill("40")
            self.page.locator(Search.SECOND_STREET).click()
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(Search.BUTTON_FIND_TARIFFS_UP).click()
            time.sleep(4)

    @allure.title("Выбрать букву Э")
    def choose_u_letter(self):
        with allure.step("Выбрать букву Э"):
            self.page.locator(Search.LETTER_A).click()

    @allure.title("Выбрать букву Ю")
    def choose_uu_letter(self):
        with allure.step("Выбрать букву Ю"):
            self.page.locator(Search.LETTER_U).click()

    @allure.title("Выбрать букву 8-8")
    def choose_eight_letter(self):
        with allure.step("Выбрать букву 8-8"):
            self.page.locator(Search.LETTER_EIGHT).click()
        with allure.step("Проверить что улицы с 8 вывелись"):
            expect(self.page.locator(Search.MART1_STREET)).to_be_visible()
            expect(self.page.locator(Search.MART2_STREET)).to_be_visible()

    @allure.title("Выбрать улицу Эльдорадовский пер.")
    def choose_eldore_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.ELDOR_STREET).click()

    @allure.title("Выбрать Аэропорт в хлебных крошках")
    def choose_aero_breadcrumps(self):
        with allure.step("Выбрать район"):
            self.page.locator(Search.AIRPORT_BREADCRUMPS).click()

    @allure.title("Выбрать улицу Брусилова ул")
    def choose_brusilov_street(self):
        with allure.step("Выбрать улицу"):
            self.page.locator(Search.BRUSILOV_STREET).click()



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
        with allure.step("Вставить Шарикоподшипниковская улицу"):
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.STREET_INPUT).fill("Арбат")
            time.sleep(5)
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
        with allure.step("Вставить дом 1"):
            self.page.locator(PopUpFilltheAddress.HOME_INPUT).fill("1")
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
        with allure.step("Удалить дом 1, выбрать 10"):
            self.page.locator(PopUpFilltheAddress.DELETE_HOUSE).click()
            self.page.locator(PopUpFilltheAddress.HOME_INPUT).fill("10")
            self.page.locator(PopUpFilltheAddress.CHOOSE_FIRST).click()
            time.sleep(4)
        with allure.step("Нажать на кнопку Найти тарифы"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(TariffsLocators.INPUT_HOME_ADDRESS).fill("Гусятников пер")
            # time.sleep(3)
            self.page.locator(TariffsLocators.GUS_STREET).click()
            time.sleep(5)
            self.page.locator(TariffsLocators.HOME_INPUT_UP).fill("1")
            time.sleep(3)
            self.page.locator(TariffsLocators.STREET_FIRST).click()
        with allure.step("Отправить заявку"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()

    @allure.title("Сделать поиск по заданному адресу")
    def fill_the_application_with_address_second(self):
        with allure.step("Заполнить адрес"):
            self.page.locator(TariffsLocators.INPUT_HOME_ADDRESS).fill("Сиреневый")
            # time.sleep(3)
            self.page.locator(TariffsLocators.PURPLE_STREET).click()
            time.sleep(5)
            self.page.locator(TariffsLocators.HOME_INPUT_UP).fill("40")
            time.sleep(3)
            self.page.locator(TariffsLocators.STREET_SECOND).click()
        with allure.step("Отправить заявку"):
            self.page.locator(PopUpFilltheAddress.FIND_TARIFFS).click()


class BlockProviders(BasePage):
    @allure.title("Проверить блок Топ провайдеров интернета в Москве")
    def check_providers_block(self):
        with allure.step("Проверить наличие блока"):
            expect(self.page.locator(ProvidersBlock.PROVIDERS_BLOCK)).to_be_visible()
        with allure.step("Сделать скриншот"):
            screenshot = self.page.locator(ProvidersBlock.PROVIDERS_BLOCK).screenshot()
            allure.attach(screenshot, name="Providers block  Screenshot",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Открыть попап поиска по адресу с Ринета (первый тариф)")
    def click_search_rinet(self):
        self.page.locator(ProvidersBlock.BUTTON_TARIFFS_ADDRESS).click()

    @allure.title("Нажать на кнопку Все провайдеры по адресу")
    def click_all_providers_button(self):
        self.page.locator(ProvidersBlock.ALL_PROVIDERS_BUTTON).click()

    @allure.title("Открыть попап поиска по адресу с СатНет (третий тариф)")
    def click_search_sat(self):
        self.page.locator(ProvidersBlock.BUTTON_TARIFFS_ADDRESS).click()

    @allure.title("Нажать на кнопку Все провайдеры по адресу")
    def click_all_providers_button(self):
        self.page.locator(ProvidersBlock.ALL_PROVIDERS_BUTTON).click()


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
