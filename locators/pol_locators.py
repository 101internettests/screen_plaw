class MainPageLocators:
    RegionConfirmPopup = "xpath=//div[@data-sentry-element='RegionConfirmPopup']"
    # RegionConfirnPopupText = "xpath=//div[@data-sentry-element='RegionConfirmPopup']//a//span"
    HEADER = "xpath=//h1"
    PIN_SEARCH_CITY = "xpath=//div[@data-sentry-component='SearchBanner']//a[@href='/select-region'][text()]"
    SEO_HEADER_CITY = "xpath=//div[@class='SeoBlock_header-wrapper__5OALy']//h2"
    FUTER_CITY = "xpath=//div[@class='BottomFooterPart_desktop-bottom-part-1__9fIIN']//span[@data-sentry-source-file='FooterRegionName.tsx']"
    SERTOLOVO_HEADER = "xpath=//h1[text()='Подключить домашний интернет в г. Сертолово (Ленинградская область)']"
    WAIT_FOR_CALL_BUTTON_OPEN = "xpath=(//button[@aria-label='Бесплатная консультация'])[1]"
    WAIT_FOR_CALL_BUTTON_OPEN_FOOTER = "xpath=(//button[@aria-label='Бесплатная консультация'])[3]"
    PHONE_NUMBER_INPUT = "xpath=//input[@id='phoneInput']"
    WAIT_FOR_CALL_BUTTON_SEND = "xpath=//button[text()='Жду звонка']"
    POPUP_HEADER_LAST = "xpath=//span[text()='Заявка в работе!']"
    POPUP_HEADER_SECOND = "xpath=//span[text()='Заявка отправляется']"
    CLOSE_POPUP_BUTTON = "xpath=//div[@aria-label]//button[@aria-label='Закрыть']"


class TariffsLocators:
    TARIFF_LIST = "xpath=//section[@data-sentry-component='TariffList']"
    TARIFF_CARD = "xpath=(//div[@data-sentry-component='TariffCard'])"
    PRICE_IN_TARIFFS = "xpath=(//div[@itemprop='offers']//p[text()])"
    DETAILS_OF_TARIFF_BUTTON = "xpath=(//button[text()='Детали тарифа'])[1]"
    CONNECTION_INFO = "xpath=//p[text()='Подключение']"
    ROUTER_INF0 = "xpath=//p[text()='Роутер']"
    MORE_ABOUT_TARIFF_BUTTON = "xpath=//button[text()='Больше о тарифе']"
    POPUP_MORE_ABOUT_TARIFF = "xpath=//div[@data-sentry-element='DialogPanel']"

class SelectRegion:
    INPUT_SELECT_REGION = "xpath=//input[@placeholder='Введите город или регион']"
    MAIN_LETTERS_SELECT = "xpath=//span[@class='SelectRegion_letter__7dXQv']"
    CITIES_LOCATOR = "xpath=//li[@class='SelectRegion_region__rRrPG']"
    LENINGRADSKAYA_OBLAST = "xpath=//span[text()='Ленинградская область']"
    SERTOLOVO = "xpath=//span[text()='Сертолово']"
    CLOSE_BUTTON_ELEMENT = "xpath=//button[@aria-label='Закрыть модальное окно']"


class AIPopUp:
    BANNER_WITH_CAT = "xpath=//div[@data-sentry-component='BannerWithCat']"
    CAT_HEADER = "xpath=//p[text()='Подобрать интернет с помощью искусственного интеллекта']"
    HELP_BUTTON = "xpath=//button[text()='Автоматический подбор тарифов']"
    UNSUCCESSFUL_ALLERT = "xpath=//span[text()='Спасибо! Скоро эта функция заработает']"
    CLOSE_BUTTON = "xpath=//button[@aria-label='Закрыть']"


class Header:
    IN_FLAT_BUTTON = "xpath=//a[text()='В квартиру']"
    IN_BUSINESS_BUTTON = "xpath=//span[text()='Для бизнеса']"
    START_TENDER_BUTTON = "xpath=//button[text()='Запустить тендер на подключение']"
    IN_GARDEN_BUTTON = "xpath=//span[text()='На дачу']"
    GARDEN_TENDER_BUTTON = "xpath=//button[text()='Все тарифы для дачи']"


class Search:
    STREET_INPUT_UP = "xpath=(//input[@placeholder='Введите улицу'])[1]"
    HOME_INPUT_UP = "xpath=(//input[@placeholder='Дом'])[1]"
    GOROXOWAYA_STREET = "xpath=//em[text()]"
    STREET_TWENTYTWO = "xpath=//em[text()='22']"
    BUTTON_FIND_TARIFFS_UP = "xpath=(//button[text()='Найти тарифы'])[1]"


class PopUpAfterSearch:
    TEXT_IN_POPUP = "xpath=//span[@class='QuizFormContent_title__RknGT']"
    CLOSE_QUIZ = "xpath=(//button[@aria-label='Закрыть'])[2]"
    INPUT_QUIZ_TEXT = "xpath=//input[@id='phone_input']"
    BUTTON_SHOW_RESULT = "xpath=//button[@data-sentry-source-file='PhoneInputWithDownButton.tsx']"


class InternetForBusiness:
    BREADCRUMBS_INTERNET_FOR_BUSINESS = "xpath=//span[text()='Интернет для бизнеса']"
    BREADCRUMBS_CONNECT_INTERNET = "xpath=//a[text()='Подключить интернет']"


class OrdersSatPage:
    BREADCRUMBS_INTERNET_FOR_SAT = "xpath=//span[text()='Интернет на дачу']"
    BREADCRUMBS_CONNECT_INTERNET = "xpath=//a[text()='Подключить интернет']"