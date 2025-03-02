class MainPageLocators:
    RegionConfirmPopup = "xpath=//div[@data-sentry-element='RegionConfirmPopup']"
    # RegionConfirnPopupText = "xpath=//div[@data-sentry-element='RegionConfirmPopup']//a//span"
    HEADER = "xpath=//h1"
    PIN_SEARCH_CITY = "xpath=//div[@data-sentry-component='SearchBanner']//a[@href='/select-region'][text()]"
    SEO_HEADER_CITY = "xpath=//div[@class='SeoBlock_header-wrapper__5OALy']//h2"
    FUTER_CITY = "xpath=//div[@class='BottomFooterPart_desktop-bottom-part-1__9fIIN']//span[@data-sentry-source-file='FooterRegionName.tsx']"
    MITISHI_HEADER = "xpath=//h1[text()='Подключить интернет в г. Мытищи']"
    WAIT_FOR_CALL_BUTTON_OPEN = "xpath=(//button[@aria-label='Бесплатная консультация'])[1]"
    WAIT_FOR_CALL_BUTTON_OPEN_FOOTER = "xpath=(//button[@aria-label='Бесплатная консультация'])[3]"
    PHONE_NUMBER_INPUT = "xpath=//input[@id='phoneInput']"
    WAIT_FOR_CALL_BUTTON_SEND = "xpath=//button[text()='Жду звонка']"
    POPUP_HEADER_LAST = "xpath=//span[text()='Заявка в работе!']"
    POPUP_HEADER_SECOND = "xpath=//span[text()='Заявка отправляется']"
    CLOSE_POPUP_BUTTON = "xpath=//div[@aria-label]//button[@aria-label='Закрыть']"
    HEADER_PAGE_CATBUTTON = "xpath=//p[text()='Вы долистали до конца!']"
    BUTTON_GO_UP = "xpath=//button[text()='Подняться наверх ']"


class TariffsLocators:
    TARIFF_LIST = "xpath=//section[@data-sentry-component='TariffList']"
    TARIFF_CARD = "xpath=(//div[@data-sentry-component='TariffCard'])"
    PRICE_IN_TARIFFS = "xpath=(//div[@itemprop='offers']//p[text()])"
    DETAILS_OF_TARIFF_BUTTON = "xpath=(//button[text()='Детали тарифа'])[1]"
    DETAILS_OF_TARIFF_BUTTON_new = "xpath=(//button[text()='Детали тарифа'])"
    CONNECTION_INFO = "xpath=//p[text()='Подключение']"
    ROUTER_INF0 = "xpath=//p[text()='Роутер']"
    MORE_ABOUT_TARIFF_BUTTON = "xpath=//button[text()='Больше о тарифе']"
    POPUP_MORE_ABOUT_TARIFF = "xpath=//button[text()='Закрыть детали']"
    PHONE_INPUT = "xpath=//input[@id='phone_input']"
    INPUT_HOME_ADDRESS = "xpath=(//input[@placeholder='Введите улицу'])[2]"
    GUS_STREET = "xpath=(//em[text()])[1]"
    PURPLE_STREET = "xpath=(//em[text()])[3]"
    HOME_INPUT_UP = "xpath=(//input[@placeholder='Дом'])[2]"
    STREET_FIRST = "xpath=(//div[@aria-selected='false'])[4]"
    STREET_SECOND = "xpath=(//div[@aria-selected='false'])[2]"
    BUTTON_FIND_TARIFFS = "xpath=//button[text()='Найти все тарифы по адресу']"


class SelectRegion:
    INPUT_SELECT_REGION = "xpath=//input[@placeholder='Введите город или регион']"
    MAIN_LETTERS_SELECT = "xpath=//span[@class='SelectRegion_letter__7dXQv']"
    CITIES_LOCATOR = "xpath=//li[@class='SelectRegion_region__rRrPG']"
    MOSKOWSKAYA_OBLAST = "xpath=(//span[text()='Московская область'])[1]"
    SERTOLOVO = "xpath=//span[text()='Мытищи']"
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
    SHARIK_STREET = "xpath=//em[text()]"
    STREET_ELEVEN = "xpath=(//em[text()='11'])[1]"
    BUTTON_FIND_TARIFFS_UP = "xpath=(//button[text()='Найти тарифы'])[1]"
    HEADER_CHOOSE_REGION = "xpath=//h2[text()='Проверка провайдеров по адресу в Москве']"
    AKADEM_AREA = "xpath=//a[text()='Академический']"
    AKD_HEADER = "xpath=//h1[text()='Подключить интернет в р. Академический']"
    AKD_BREADCRUMPS = "xpath=//span[text()='Академический']"
    GREM_STREET = "xpath=//a[text()='Гримау ул']"
    GREM_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул Гримау, Москва']"
    GREM_BREADCRUMPS = "xpath=//span[text()='ул Гримау']"


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
    REVIEW_HEADER = "xpath=//h2[text()='Отзывы о провайдерах Москвы']"
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
    HOME_INPUT = "xpath=(//input[@placeholder='Дом'])[2]"
    FIND_TARIFFS = "xpath=(//button[text()='Найти тарифы'])[2]"
    DELETE_HOUSE = "xpath=(//div[@data-headlessui-state]//button[@data-sentry-component='IconButton'])[4]"


class ProvidersBlock:
    PROVIDERS_BLOCK = "xpath=//div[@class='MainPage_provs-reviews-block__QNvrv']"
    BUTTON_TARIFFS_ADDRESS = "xpath=(//button[text()='Тарифы по вашему адресу'])[1]"
    ALL_PROVIDERS_BUTTON = "xpath=//button[text()='Все провайдеры по адресу']"


class ReviewPage:
    BUTTON_WRITE_REVIEW = "xpath=//a[text()='Написать отзыв']"
    CHOSE_IN_FLAT = "xpath=//span[text()='в квартире']"
    INPUT_PROVIDER = "xpath=//input[@placeholder='Введите название']"
    CHOOSE_ROSTEL = "xpath=//div[text()='Ростелеком']"
    FOUR_INTERNET = "xpath=(//div[@class='Rating_star__PqEKQ'])[4]"
    FOUR_TV = "xpath=(//div[@class='Rating_star__PqEKQ'])[9]"
    FOUR_MONTAZ = "xpath=(//div[@class='Rating_star__PqEKQ'])[14]"
    REVIEW_TEXTAREA = "xpath=//textarea[@id='review-feedback-comment']"
    THREE_MONTH_YEAR = "xpath=//label[@for='three_month_one_year']"
    NAME_INPUT = "xpath=//input[@id='review-feedback-name']"
    SEND_REVIEW_BUTTON = "xpath=//button[text()='Отправить отзыв']"
    CHECK_THANKFORREVIEW = "xpath=//p[text()='Спасибо за отзыв!']"


class Filters:
    PRICE_BEFORE_ONETH = "xpath=//button[text()='до 1000 ₽/мес']"
    CHOOSE_ALL_PROVIDERS = "xpath=//button[text()='Выбрать всё']"
    SPEED_INTERNET_200_500 = "xpath=//button[text()='200-500 Мб/с']"
    BUTTON_SHOW_ALL_TARIFFS = "xpath=//button[@data-sentry-source-file='TariffFilter.tsx']"
    CHECK_FILTERS = "xpath=(//div[@class='HouseNZLPage_quick-filters-container__Okssh'])[1]"


class TariffsInTariffPage:
    TARIFF_WITH_SPEED_500 = ("xpath=(//meta[@content='500 Мб/c Домашний интернет']/following::div//button["
                             "@data-sentry-element='Button'])[1]")
    PHONE_NUMBER_INPUT = "xpath=//input[@id='ph_input']"
    BUTTON_SEND = "xpath=//button[text()='Отправить заявку']"
