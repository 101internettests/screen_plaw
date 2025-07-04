class MainPageLocators:
    RegionConfirmPopup = "xpath=//div[@data-sentry-element='RegionSelector']"
    # RegionConfirnPopupText = "xpath=//div[@data-sentry-element='RegionConfirmPopup']//a//span"
    HEADER = "xpath=//h1"
    PIN_SEARCH_CITY = "xpath=(//a[@href='/select-region'][text()])[1]"
    SEO_HEADER_CITY = "xpath=//div[@class='SeoBlock_header-wrapper__5OALy']//h2"
    FUTER_CITY = "xpath=(//span[@data-sentry-source-file='FooterRegionName.tsx'][text()])[2]"
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
    SECOND_INPUT = "xpath=//input[@id='ph_input']"
    INPUT_HOME_ADDRESS = "xpath=(//input[@placeholder='Введите улицу'])[2]"
    INPUT_HOME_IN_TARIFF_ADDRESS = "xpath=(//input[@placeholder='Введите улицу'])[3]"
    HOME_IN_TARIFF_SECOND = "xpath=(//input[@placeholder='Дом'])[2]"
    HOME_IN_TARIFF_INPUT = "xpath=(//input[@placeholder='Дом'])[3]"
    GUS_STREET = "xpath=(//em[text()])[1]"
    PURPLE_STREET = "xpath=(//em[text()])[3]"
    NEW_ARBAT_STREET = "xpath=(//em[text()])[4]"
    HOME_INPUT_UP = "xpath=(//em[text()='Новый'])[1]"
    STREET_TEN= "xpath=(//div[@aria-selected='false'])[1]"
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
    COVERAGE_MAP = "xpath=(//a[@aria-label='Карта покрытия'])[2]"
    IN_BUSINESS_BUTTON = "xpath=//span[text()='Для бизнеса']"
    START_TENDER_BUTTON = "xpath=//button[text()='Запустить тендер на подключение']"
    IN_GARDEN_BUTTON = "xpath=//span[text()='На дачу']"
    GARDEN_TENDER_BUTTON = "xpath=//button[text()='Все тарифы для дачи']"


class Search:
    STREET_INPUT_UP = "xpath=(//input[@placeholder='Введите улицу'])[1]"
    STREET_INPUT_UP_THIRD = "xpath=(//input[@placeholder='Введите улицу'])[3]"
    HOME_INPUT_UP = "xpath=(//input[@placeholder='Дом'])[1]"
    HOME_INPUT_SECOND = "xpath=(//input[@placeholder='Дом'])[2]"
    HOME_INPUT_UP_THIRD = "xpath=(//input[@placeholder='Дом'])[3]"
    SHARIK_STREET = "xpath=//em[text()]"
    STREET_FIRST = "xpath=(//em[text()])[1]"
    PURPLE_STREET = "xpath=(//em[text()])[3]"
    SECOND_STREET = "xpath=(//em[text()])[2]"
    STREET_ELEVEN = "xpath=(//em[text()='11'])[1]"
    BUTTON_FIND_TARIFFS_UP = "xpath=(//button[text()='Найти тарифы'])[1]"
    BUTTON_FIND_TARIFFS_SECOND = "xpath=(//button[text()='Найти тарифы'])[2]"
    BUTTON_FIND_TARIFFS_UP_SECOND = "xpath=(//button[text()='Найти тарифы'])[3]"
    HEADER_CHOOSE_REGION = "xpath=//h2[text()='Проверка провайдеров по адресу в Москве']"
    AKADEM_AREA = "xpath=//a[text()='Академический']"
    ALTUF_AREA = "xpath=//a[text()='Алтуфьевский']"
    AIRPORT_AREA = "xpath=//a[text()='Аэропорт']"
    BUTOVO_AREA = "xpath=//a[text()='Южное Бутово']"
    AKD_HEADER = "xpath=//h1[text()='Подключить интернет в р. Академический']"
    ALTUF_HEADER = "xpath=//h1[text()='Подключить интернет в р. Алтуфьевский']"
    AIRPORT_HEADER = "xpath=//h1[text()='Подключить интернет в р. Аэропорт']"
    BUTOVO_HEADER = "xpath=//h1[text()='Подключить интернет в р. Южное Бутово']"
    AKD_BREADCRUMPS = "xpath=//span[text()='Академический']"
    ALTUF_BREADCRUMPS = "xpath=//span[text()='Алтуфьевский']"
    AIRPORT_BREADCRUMPS = "xpath=//span[text()='Аэропорт']"
    AIRPORT_BREADCRUMPS_SECOND = "xpath=//a[text()='Аэропорт']"
    BUTOVO_BREADCRUMPS = "xpath=//span[text()='Южное Бутово']"
    STANDART_STREET = "xpath=//a[text()='Стандартная ул']"
    STANDART_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул Стандартная, Москва']"
    STANDART_BREADCRUMPS = "xpath=//span[text()='ул Стандартная']"
    GREM_STREET = "xpath=//a[text()='Гримау ул']"
    GREM_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул Гримау, Москва']"
    GREM_BREADCRUMPS = "xpath=//span[text()='ул Гримау']"
    FERSM_STREET = "xpath=//a[text()='Ферсмана ул']"
    FERSM_HEADER = "xpath=//h1[text()='Интернет-провайдеры на ул Ферсмана, Москва']"
    FERSM_BREADCRUMPS = "xpath=//span[text()='ул Ферсмана']"
    FIRST_HOUSE_BUTTON = "xpath=//a[text()='1']"
    HOUSE_BUTTON = "xpath=//span[text()='9-15']"
    HOUSE15_BUTTON = "xpath=//span[text()='15 с2-23']"
    HOUSE29_BUTTON = "xpath=//span[text()='1-17 к1']"
    THIRTEEN_HOUSE = "xpath=//a[@aria-label='13']"
    FIFTEEN_HOUSE = "xpath=//a[@aria-label='15 к1']"
    FIFTEENC_HOUSE = "xpath=//a[@aria-label='15 с3']"
    LETTERS_HOUSE = "xpath=//span[text()='1-5253']"
    LETTER_NINETEEN = "xpath=//a[text()='19']"
    LETTER_B = "xpath=//span[text()='Б']"
    LETTER_A = "xpath=//span[text()='Э']"
    LETTER_U = "xpath=//span[text()='Ю']"
    LETTER_EIGHT = "xpath=//span[text()='8-8']"
    ELDOR_STREET = "xpath=//a[text()='Эльдорадовский пер']"
    BRUSILOV_STREET = "xpath=//a[text()='Брусилова ул']"
    BORISOGL_STREET = "xpath=//a[text()='Борисоглебский пер']"
    MART1_STREET = "xpath=//a[text()='8 Марта 1-я ул']"
    MART2_STREET = "xpath=//a[text()='8 Марта 4-я ул']"
    BUTTON_SHOW_MORE = "xpath=//button[text()='Показать ещё']"


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
    REVIEW_HEADER_STREET = "xpath=//h2[text()='Отзывы жителей мкр Гагарина']"
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
    FIRST_BUTTON = "xpath=(//div[@itemprop='offers'])[1]"
    FIRST_BUTTON_TARIFF = "xpath=(//button[@data-sentry-source-file='TariffCard.tsx'])[1]"
    FIRST_BUTTON_WITH_PRICE = "xpath=(//div[@itemprop='offers'])[1]"
    SECOND_BUTTON_WITH_PRICE = "xpath=(//button[@data-sentry-source-file='TariffCardVariantB.tsx'])[3]"
    TARIFF_NAME = "xpath=//span[@class='SubmitFormContent_provider-name__R1UkL']"
    TARIFF_NAME2 = "xpath=//span[@class='SubmitFormContent_tariff-name__LCZiq']"
    TELEPHONE_INPUT = "xpath=//input[@id='ph_input']"
    SEND_APPLICATION_BUTTON = "xpath=//button[text()='Отправить заявку']"
    STREET_INPUT = "xpath=(//input[@placeholder='Введите улицу'])[3]"


class PopUpFilltheAddress:
    HEADER_WINDOW = "xpath=//h2[text()='Введите адрес и сравните все доступные тарифы']"
    IN_FLAT_BUTTON = "xpath=(//span[text()='В квартиру'])[2]"
    IN_BUSINESS_BUTTON = "xpath=(//span[text()='Для бизнеса'])[2]"
    IN_SAT_BUTTON = "xpath=(//span[text()='На дачу'])[2]"
    START_TENDER_BUTTON = "xpath=(//button[text()='Запустить тендер на подключение'])[1]"
    ALL_TARIFFS_BUTTON = "xpath=(//button[text()='Все тарифы для дачи'])[1]"
    STREET_INPUT = "xpath=(//input[@placeholder='Введите улицу'])[2]"
    CHOOSE_FIRST = "xpath=(//em[text()])[1]"
    CHOOSE_NEGATIVE_HOUSE = "xpath=//div[text()='111']"
    CHOOSE_NEGATIVE_HOUSE_SECOND = "xpath=//div[text()='222']"
    CHOOSE_SECOND = "xpath=(//em[text()])[2]"
    HOME_INPUT = "xpath=(//input[@placeholder='Дом'])[2]"
    FIND_TARIFFS = "xpath=(//button[text()='Найти тарифы'])[2]"
    DELETE_HOUSE = "xpath=(//div[@data-headlessui-state]//button[@data-sentry-component='IconButton'])[4]"


class ProvidersBlock:
    PROVIDERS_BLOCK = "xpath=//div[@class='MainPage_provs-reviews-block__QNvrv']"
    BUTTON_TARIFFS_ADDRESS = "xpath=(//button[text()='Тарифы по вашему адресу'])[1]"
    BUTTON_TARIFFS_ADDRESS_SECOND = "xpath=(//button[text()='Тарифы по вашему адресу'])[2]"
    ALL_PROVIDERS_BUTTON = "xpath=//button[text()='Все провайдеры по адресу']"
    PLACE_FOR_SCREEN = "xpath=//div[@data-sentry-element='DialogPanel']"


class ReviewPage:
    BUTTON_WRITE_REVIEW = "xpath=//a[text()='Написать отзыв']"
    BUTTON_WRITE = "xpath=//a[text()='Написать']"
    CHOSE_IN_FLAT = "xpath=//span[text()='в квартире']"
    INPUT_PROVIDER = "xpath=//input[@placeholder='Введите название']"
    CHOOSE_ROSTEL = "xpath=//div[text()='Ростелеком']"
    FOUR_INTERNET = "xpath=(//div[@class='Rating_star__DZUJK'])[4]"
    FOUR_TV = "xpath=(//div[@class='Rating_star__DZUJK'])[9]"
    FOUR_MONTAZ = "xpath=(//div[@class='Rating_star__DZUJK'])[14]"
    REVIEW_TEXTAREA = "xpath=//textarea[@id='review-feedback-comment']"
    THREE_MONTH_YEAR = "xpath=//label[@for='three_month_one_year']"
    NAME_INPUT = "xpath=//input[@id='review-feedback-name']"
    SEND_REVIEW_BUTTON = "xpath=//button[text()='Отправить отзыв']"
    CHECK_THANKFORREVIEW = "xpath=//p[text()='Спасибо за отзыв!']"


class Filters:
    PRICE_BEFORE_SEVEN = "xpath=//button[text()='до 700 ₽/мес']"
    PRICE_BEFORE_ONETH = "xpath=//button[text()='до 1000 ₽/мес']"
    CHOOSE_ALL_PROVIDERS = "xpath=//button[text()='Выбрать всё']"
    SPEED_INTERNET_100_200 = "xpath=//button[text()='100-200 Мб/с']"
    SPEED_INTERNET_200_500 = "xpath=//button[text()='200-500 Мб/с']"
    BUTTON_SHOW_ALL_TARIFFS = "xpath=//button[@data-sentry-source-file='TariffFilter.tsx']"
    CHECK_FILTERS = "xpath=(//div[@class='HouseNZLPage_quick-filters-container__Okssh'])[1]"
    BILAIN_PROV = "xpath=//span[text()='билайн']"
    ALMATEL_PROV = "xpath=//span[text()='Алмател']"
    MTS_PROV = "xpath=//span[text()='МТС']"
    HOUSE_RU_PROV = "xpath=//span[text()='Дом.ру']"
    ROSTELEKOM_PROV = "xpath=//span[text()='Ростелеком']"
    MEGAFONE_PROV = "xpath=//span[text()='МегаФон']"
    SORTING_BUTTON = "xpath=(//button[text()='Сортировка'])[2]"
    BUTTON_PRISE_WITHOUT_SALE = "xpath=//span[text()='По цене без учёта акций']"
    BUTTON_SPEED_BUTTON = "xpath=//span[text()='По скорости']"
    BUTTON_SHOW_MORE = "xpath=//button[text()='Показать ещё 10 тарифов из 28']"
    BUTTON_SHOW_MORE_MOL = "xpath=//button[text()='Показать ещё 10 тарифов из 22']"
    BUTTON_SHOW_MORE_MOL2 = "xpath=//button[text()='Показать ещё 2 тарифа из 22']"
    BUTTON_SHOW_MORE_EIGHT = "xpath=//button[text()='Показать ещё 8 тарифов из 28']"
    BUTTON_SHOW_TEN_FROM_THIRTEEN = "xpath=//button[text()='Показать ещё 10 тарифов из 30']"
    LAST_LOCATOR = "xpath=(//div[@itemprop='offers'])"
    FIRST_LOCATOR = "xpath=(//div[@itemprop='offers'])[1]"
    FOUR_LOCATOR = "xpath=(//div[@itemprop='offers'])[4]"
    QUIZ_INPUT = "xpath=//input[@id='ph_input']"
    BUTTON_SHOW_RESULT = "xpath=//button[text()='Отправить заявку']"
    TARIFF_DETAILS_BUTTON = "xpath=(//button[text()='Детали тарифа'])[1]"
    TARIFF_DETAILS_BUTTON_FOUR = "xpath=(//button[text()='Детали тарифа'])[4]"
    MORE_ABOUT_TARIFF_BUTTON = "xpath=(//button[text()='Больше о тарифе'])[1]"
    CLOSE_DETAILS_BUTTON = "xpath=(//button[text()='Закрыть детали'])[1]"
    TAG_INTERNET_TV = "xpath=//span[text()='Интернет+ТВ']"


class TariffsInTariffPage:
    TARIFF_WITH_SPEED_500 = ("xpath=(//meta[@content='500 Мб/c Домашний интернет']/following::div//button["
                             "@data-sentry-element='Button'])[1]")
    TARIFF_WITH_SPEED_200 = ("xpath=(//meta[@content='200 Мб/c Домашний интернет']/following::div//button["
                             "@data-sentry-element='Button'])[1]")
    PHONE_NUMBER_INPUT = "xpath=//input[@id='ph_input']"
    BUTTON_SEND = "xpath=//button[text()='Отправить заявку']"


class MapCoverage:
    STREET_INPUT = "xpath=//input[@placeholder='Введите улицу']"
    SEARCH_BUTTON = "xpath=//a[text()='Искать']"
    HOME_INPUT = "xpath=//input[@placeholder='Дом']"
    FIND_TARIFFS = "xpath=//button[text()='Найти тарифы']"


class MiddlePageLocators:
    STREET_INPUT = "xpath=(//input[@placeholder='Введите улицу'])[2]"
    FIRST_HOUSE = "xpath=(//p[text()='Санкт-Петербург, Адмиралтейский'])[1]"
    THIRD_HOUSE = "xpath=(//p[text()='Москва, Арбат'])[4]"
    HOME_INPUT = "xpath=(//input[@placeholder='Дом'])[2]"
    STREET_FIRST = "xpath=(//div[@aria-selected='false'])[1]"
    FIND_TARIFFS = "xpath=(//button[text()='Найти тарифы'])[2]"


class PerelikovkaLocators:
    OPEN_OTHER_STREETS_IN_BALASHIXA = "xpath=//p[text()='Другие подключенные улицы в Балашихе']"
    GRANICHNAYA_STREET = "xpath=//a[text()='ул Граничная']"
    ENERGITICH_STREET = "xpath=//a[text()='ул Энергетическая (Русавкино-Романово)']"
    NOSOVOXH_STREET = "xpath=//a[text()='ш Носовихинское']"