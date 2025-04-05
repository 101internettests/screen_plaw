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
    CHECK_PHONE = "xpath=//input[@value='+7 (111) 111-11-11']"
    WAIT_FOR_CALL_BUTTON_SEND = "xpath=//button[text()='Жду звонка']"
    POPUP_HEADER_LAST = "xpath=//span[text()='Заявка в работе!']"
    POPUP_HEADER_SECOND = "xpath=//span[text()='Заявка отправляется']"
    CLOSE_POPUP_BUTTON = "xpath=//div[@aria-label]//button[@aria-label='Закрыть']"
    HEADER_PAGE_CATBUTTON = "xpath=//p[text()='Вы долистали до конца!']"
    BUTTON_GO_UP = "xpath=//button[text()='Подняться наверх ']"


class TariffsLocators:
    TARIFF_LIST = "xpath=//section[@data-sentry-component='TariffList']"
    DETAILS_OF_TARIFF_BUTTON_new = "xpath=(//button[text()='Детали тарифа'])"
    TARIFF_CARD = "xpath=(//div[@data-sentry-component='TariffCard'])"
    PRICE_IN_TARIFFS = "xpath=(//div[@itemprop='offers']//p[text()])"
    DETAILS_OF_TARIFF_BUTTON = "xpath=(//button[text()='Детали тарифа'])[1]"
    CONNECTION_INFO = "xpath=//p[text()='Подключение']"
    ROUTER_INF0 = "xpath=//p[text()='Роутер']"
    MORE_ABOUT_TARIFF_BUTTON = "xpath=//button[text()='Больше о тарифе']"
    POPUP_MORE_ABOUT_TARIFF = "xpath=//button[text()='Закрыть детали']"
    PHONE_INPUT = "xpath=//input[@id='phone_input']"
    INPUT_HOME_ADDRESS = "xpath=(//input[@placeholder='Введите улицу'])[2]"
    GUS_STREET = "xpath=(//em[text()])[1]"
    HOME_INPUT_UP = "xpath=(//input[@placeholder='Дом'])[2]"
    ENG_STREET = "xpath=(//em[text()])[3]"
    SIX_STREET = "xpath=(//em[text()])[6]"
    STREET_FIRST = "xpath=(//div[@aria-selected='false'])[2]"
    STREET_SECOND = "xpath=(//div[@aria-selected='false'])[2]"
    BUTTON_FIND_TARIFFS = "xpath=//button[text()='Найти все тарифы по адресу']"
    INPUT_HOME_IN_TARIFF_ADDRESS = "xpath=(//input[@placeholder='Введите улицу'])[3]"
    HOME_IN_TARIFF_INPUT = "xpath=(//input[@placeholder='Дом'])[3]"
    STREET_TEN = "xpath=(//div[@aria-selected='false'])[1]"


class SelectRegion:
    INPUT_SELECT_REGION = "xpath=//input[@placeholder='Введите город или регион']"
    MAIN_LETTERS_SELECT = "xpath=//span[@class='SelectRegion_letter__7dXQv']"
    CITIES_LOCATOR = "xpath=//li[@class='SelectRegion_region__rRrPG']"
    LENINGRADSKAYA_OBLAST = "xpath=(//span[text()='Ленинградская область'])[1]"
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
    COVERAGE_MAP = "xpath=(//a[@aria-label='Карта покрытия'])[2]"


class Search:
    STREET_INPUT_UP = "xpath=(//input[@placeholder='Введите улицу'])[1]"
    STREET_INPUT_UP_THIRD = "xpath=(//input[@placeholder='Введите улицу'])[3]"
    FIRST_HOUSE_BUTTON = "xpath=//a[text()='1']"
    TWENTY_SEVEN_HOUSE_BUTTON = "xpath=//a[text()='27']"
    HOME_INPUT_UP = "xpath=(//input[@placeholder='Дом'])[1]"
    HOME_INPUT_UP_THIRD = "xpath=(//input[@placeholder='Дом'])[3]"
    GOROXOWAYA_STREET = "xpath=//em[text()]"
    FIRST_STREET = "xpath=(//em[text()])[1]"
    SECOND_STREET = "xpath=(//em[text()])[2]"
    STREET_TWENTYTWO = "xpath=//em[text()='22']"
    BUTTON_FIND_TARIFFS_UP = "xpath=(//button[text()='Найти тарифы'])[1]"
    BUTTON_FIND_TARIFFS_UP_THIRD = "xpath=(//button[text()='Найти тарифы'])[3]"
    HEADER_CHOOSE_REGION = "xpath=//h2[text()='Выберите свой район']"
    ADMIRALTEYSKIE_AREA = "xpath=//a[text()='Адмиралтейский']"
    VASILEOSTRV_AREA = "xpath=//a[text()='Василеостровский']"
    UGO_ZAPAD_AREA = "xpath=//a[text()='Юго-Запад']"
    GATCHINA_AREA = "xpath=//a[text()='Гатчина']"
    ADM_HEADER = "xpath=//h1[text()='Подключить домашний интернет в р. Адмиралтейский (Санкт-Петербург)']"
    VAS_HEADER = "xpath=//h1[text()='Подключить домашний интернет в р. Василеостровский (Санкт-Петербург)']"
    UGO_ZAPAD_HEADER = "xpath=//h1[text()='Подключить домашний интернет в р. Юго-Запад (Санкт-Петербург)']"
    GATCHINA_HEADER = "xpath=//h1[text()='Подключить домашний интернет в г. Гатчина (Санкт-Петербург)']"
    ADM_BREADCRUMPS = "xpath=//span[text()='Адмиралтейский']"
    ADM_BREADCRUMPS_STREET = "xpath=//a[text()='Адмиралтейский']"
    VAS_BREADCRUMPS = "xpath=//span[text()='Василеостровский']"
    ENGLISH_PROSP_STREET = "xpath=//a[text()='Английский пр-кт']"
    GOROX_STREET = "xpath=//a[text()='Гороховая ул']"
    REPINA_STREET = "xpath=//a[text()='Репина ул']"
    KARL_MARKS_STREET = "xpath=//a[text()='К.Маркса ул']"
    SHEVCHENKO_STREET = "xpath=//a[text()='Шевченко ул']"
    ENGLISH_HEADER = "xpath=//h1[text()='Интернет-провайдеры на пр-кт Английский, Санкт-Петербург']"
    GOROX_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул Гороховая, Санкт-Петербург']"
    REPINA_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул Репина, Василеостровский, Санкт-Петербург']"
    MARKS_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул К.Маркса, Санкт-Петербург']"
    SHEV_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул Шевченко, Василеостровский, Санкт-Петербург']"
    YAKU_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул Якубовича, Санкт-Петербург']"
    KRASN_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул 13-я Красноармейская, Санкт-Петербург']"
    PETER_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ш Петергофское, Юго-Запад, Санкт-Петербург']"
    ENGLISH_BREADCRUMPS = "xpath=//span[text()='пр-кт Английский']"
    GOROX_BREADCRUMPS = "xpath=//span[text()='ул Гороховая']"
    REPINA_BREADCRUMPS = "xpath=//span[text()='ул Репина']"
    MARKS_BREADCRUMPS = "xpath=//span[text()='ул К.Маркса']"
    SHEVCHENKO_BREADCRUMPS = "xpath=//span[text()='ул Шевченко']"
    YAKUBOVICH_BREADCRUMPS = "xpath=//span[text()='ул Якубовича']"
    SHOW_MORE_BUTTON = "xpath=//button[text()='Показать ещё']"
    HOUSE_BUTTON = "xpath=//span[text()='24-38']"
    HOUSE_1978_BUTTON = "xpath=//span[text()='19-78 к5']"
    THIRTY_THREE_HOUSE = "xpath=//a[@aria-label='33']"
    FIFTY_FIVE_HOUSE = "xpath=//a[@aria-label='55 к1']"
    LETTER_YA = "xpath=//span[text()='Я']"
    LETTER_U = "xpath=//span[text()='Ю']"
    LETTER_R = "xpath=//span[text()='Р']"
    LETTER_NUMS = "xpath=//span[text()='1-13']"
    LETTER_NEW_NUMS = "xpath=//span[text()='1-27']"
    YAKUBOVICH_STREET = "xpath=//a[text()='Якубовича ул']"
    KRASN_STREET = "xpath=//a[text()='13-я Красноармейская ул']"
    PETERGOF_STREET = "xpath=//a[text()='Петергофское ш']"


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


class ReviewBlock:
    REVIEW_HEADER = "xpath=//h2[text()='Отзывы о провайдерах домашнего интернета в Санкт-Петербурге']"
    # посчитать эти локаторы
    NUBER_OF_REVIEW = "xpath=(//div[@data-sentry-component='ReviewCard'])"
    BUTTON_MORE_REVIEWS = "xpath=//a[text()='Ещё отзывы']"


class ReviewWebSiteCat:
    CLICK_ON_LOGO = "xpath=//button[@aria-label='Виджет оценки сайта']"
    # один из пяти котов
    CLICK_ON_RANDOM_CAT = "xpath=(//label[@for])"
    TEXTAREA_IN_REVIEW = "xpath=//textarea[@placeholder='Расскажите, если что-то не так - мы постараемся исправить']"
    BUTTON_SEND = "xpath=//button[text()='Отправить']"
    TEXT_IN_POPUP = "xpath=//h2[text()='Спасибо, что помогаете нам стать лучше!']"


class ProvidersPage:
    TAG_HOME_INTERNET = "xpath=//span[text()='Домашний интернет']"
    FIRST_BUTTON_WITH_PRICE = "xpath=(//div[@class='TariffCard_button__ONu3k']//button[@data-sentry-source-file])[1]"
    TARIFF_NAME = "xpath=//span[@class='SubmitFormContent_provider-name__R1UkL']"
    TARIFF_NAME2 = "xpath=//span[@class='SubmitFormContent_tariff-name__LCZiq']"
    TELEPHONE_INPUT = "xpath=//input[@id='ph_input']"
    SEND_APPLICATION_BUTTON = "xpath=//button[text()='Отправить заявку']"


class PopUpFilltheAddress:
    HEADER_WINDOW = "xpath=//h2[text()='Введите адрес и сравните все доступные тарифы']"
    IN_FLAT_BUTTON = "xpath=(//span[text()='В квартиру'])[2]"
    IN_BUSINESS_BUTTON = "xpath=(//span[text()='Для бизнеса'])[2]"
    IN_SAT_BUTTON = "xpath=(//span[text()='На дачу'])[2]"
    START_TENDER_BUTTON = "xpath=(//button[text()='Запустить тендер на подключение'])[1]"
    ALL_TARIFFS_BUTTON = "xpath=(//button[text()='Все тарифы для дачи'])[1]"
    STREET_INPUT = "xpath=(//input[@placeholder='Введите улицу'])[2]"
    CHOOSE_FIRST = "xpath=(//em[text()])[1]"
    CHOOSE_SECOND = "xpath=(//em[text()])[2]"
    CHOOSE_FOUR = "xpath=(//em[text()])[4]"
    HOME_INPUT = "xpath=(//input[@placeholder='Дом'])[2]"
    FIND_TARIFFS = "xpath=(//button[text()='Найти тарифы'])[2]"
    DELETE_HOUSE = "xpath=(//div[@data-headlessui-state]//button[@data-sentry-component='IconButton'])[4]"


class ProvidersBlock:
    PROVIDERS_BLOCK = "xpath=//div[@class='MainPage_provs-reviews-block__QNvrv']"
    BUTTON_TARIFFS_ADDRESS = "xpath=(//button[text()='Тарифы по вашему адресу'])[3]"
    ALL_PROVIDERS_BUTTON = "xpath=//button[text()='Все провайдеры по адресу']"


class WindowLocators:
    HEADER_WINDOW = "xpath=//h2[text()='Введите адрес и сравните все доступные тарифы']"
    IN_FLAT_BUTTON = "xpath=(//span[text()='В квартиру'])[3]"
    IN_BUSINESS_BUTTON = "xpath=(//span[text()='Для бизнеса'])[3]"
    IN_SAT_BUTTON = "xpath=(//span[text()='На дачу'])[3]"
    START_TENDER_BUTTON = "xpath=(//button[text()='Запустить тендер на подключение'])[1]"
    ALL_TARIFFS_BUTTON = "xpath=(//button[text()='Все тарифы для дачи'])[1]"
    STREET_INPUT = "xpath=(//input[@placeholder='Введите улицу'])[2]"
    INPUT_HOME_ADDRESS = "xpath=(//input[@placeholder='Введите улицу'])[3]"
    ENG_STREET = "xpath=(//em[text()])[3]"
    HOME_INPUT_UP = "xpath=(//input[@placeholder='Дом'])[3]"
    STREET_SECOND = "xpath=(//div[@aria-selected='false'])[1]"
    STREET_REALLY_SECOND = "xpath=(//div[@aria-selected='false'])[2]"
    FIND_TARIFFS = "xpath=(//button[text()='Найти тарифы'])[3]"
    GUS_STREET = "xpath=(//em[text()])[1]"
    XLEB_STREET = "xpath=(//em[text()])[2]"


class TohomeMiddlePageSearch:
    PLACEHOLDER_STREET = "xpath=(//input[@placeholder='Введите улицу'])[2]"
    PLACEHOLDER_HOUSE = "xpath=(//input[@placeholder='Дом'])[2]"
    BUTTON_FIND_TARIFFS_UP = "xpath=(//button[text()='Найти тарифы'])[2]"
    VISIBLE_TEXT = "xpath=//h2[text()='Тарифы в Санкт-Петербурге']"
    VISIBLE_TEXT_MSK = "xpath=//h2[text()='Лучшие интернет тарифы в Москве']"
    GOROXOWAYA_STREET = "xpath=//div[@role='option']"
    INPUT_HOME_ADDRESS = "xpath=(//input[@placeholder='Введите улицу'])[3]"
    GUS_STREET = "xpath=(//em[text()])[1]"
    SECOND_STREET = "xpath=(//em[text()])[2]"
    HOME_INPUT_UP = "xpath=(//input[@placeholder='Дом'])[3]"