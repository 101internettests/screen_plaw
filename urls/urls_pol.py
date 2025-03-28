from config import host_stage

urls = [
    "https://piter-online.net/nalichie-provayderov-po-adresu",
    "https://piter-online.net/select-region",
    "https://piter-online.net/leningradskaya-oblast",
    "https://piter-online.net/orders/tohome",
    "https://piter-online.net/address",
    "https://piter-online.net/address/%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA-id1250",
    "https://piter-online.net/address/%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA-id1250/%D1%83%D0%BB-2-%D1%8F-%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%84%D0%BB%D0%BE%D1%82%D1%81%D0%BA%D0%B0%D1%8F-id295159",
    "https://piter-online.net/leningradskaya-oblast/doma-nzl?house_id=4270758",
    "https://piter-online.net/all-districts",
    "https://piter-online.net/leningradskaya-oblast/site-map",
    "https://piter-online.net/all-regions",
    "https://piter-online.net/rating",
    "https://piter-online.net/reviews",
    "https://piter-online.net/rating/mts",
    "https://piter-online.net/feedback",
    "https://piter-online.net/providers",
    "https://piter-online.net/providers/dom-ru",
    "https://piter-online.net/providers/awanti",
    "https://piter-online.net/providers/dom-ru/rates",
    "https://piter-online.net/providers/dom-ru/rates/domashnij-internet",
    "https://piter-online.net/providers/dom-ru/rates/internet-i-tv",
    "https://piter-online.net/providers/rostelecom/rates/internet-tv-mobile",
    "https://piter-online.net/providers/rostelecom/rates/internet-i-mobilnaya-svyaz",
    "https://piter-online.net/providers/dom-ru/rates/nedorogoj-domashnij-internet",
    "https://piter-online.net/rates",
    "https://piter-online.net/rates/domashnij-internet",
    "https://piter-online.net/rates/internet-i-tv",
    "https://piter-online.net/rates/internet-tv-mobile",
    "https://piter-online.net/rates/internet-i-mobilnaya-svyaz",
    "https://piter-online.net/rates/nedorogoj-domashnij-internet",
    "https://piter-online.net/rates/internet-100-mbit",
    "https://piter-online.net/rates/internet-300-mbit",
    "https://piter-online.net/rates/internet-500-mbit",
    "https://piter-online.net/orders/office",
    "https://piter-online.net/orders/sat",
    "https://piter-online.net/about/partners",
    "https://piter-online.net/about/company",
    "https://piter-online.net/about/oplata-i-garantii",
    "https://piter-online.net/about/contacts",
    "https://piter-online.net/about/personal-data",
    "https://piter-online.net/articles",
    "https://piter-online.net/articles/luchshaya-simkarta-dlya-interneta",
    "https://piter-online.net/experts",
    "https://piter-online.net/experts/alisa-zhukova-id8",
    "https://piter-online.net/help",
    "https://piter-online.net/help/section-domashnij-internet",
    "https://piter-online.net/help/kak-vybrat-luchshij-internet-tarif",
    "https://piter-online.net/operatory",
    "https://piter-online.net/operatory/mts",
    "https://piter-online.net/operatory/mts/ratesmobile#tags#tags",
    "https://piter-online.net/operatory/tele-2/ratesmobile/dlja-modema#tags ",
    "https://piter-online.net/operatory/beeline/ratesmobile/dlja-noutbuka#tags",
    "https://piter-online.net/operatory/tele-2/ratesmobile/bezlimitnyj-internet#tags",
    "https://piter-online.net/operatory/tele-2/ratesmobile/vygodnye#tags",
    "https://piter-online.net/operatory/beeline/ratesmobile/bez-abonentskoj-platy#tags",
    "https://piter-online.net/operatory/beeline/ratesmobile/semeinye#tags",
    "https://piter-online.net/operatory/beeline/ratesmobile/detskie#tags",
    "https://piter-online.net/operatory/tele-2/ratesmobile/mezhdunarodnye#tags",
    "https://piter-online.net/operatory/tele-2/ratesmobile/po-rossii#tags",
    "https://piter-online.net/operatory/mts/ratesmobile/esim#tags",
    "https://piter-online.net/operatory/mts/ratesmobile/perenos_nomera#tags",
    "https://piter-online.net/ratesmobile",
    "https://piter-online.net/operatory/mts/nomera",
    "https://piter-online.net/nomera"
]

names = [
    "Страница без адреса",
    "Селект регион",
    "Главная с регионом",
    "Поиск по адресу",
    "Карта покрытия",
    "Районы",
    "Улицы",
    "Дом",
    "Все районы",
    "Карта сайта",
    "Все регионы",
    "Рейтинг",
    "Отзывы в регионе",
    "Отзывы о провайдере",
    "Страница оставления отзыва",
    "Каталог провайдеров",
    "Страница вип-провайдера",
    "Страница провайдера Невип пров",
    "Тарифы вип-провайдера",
    "Тарифы вип-провайдера, тег Домашний интернет",
    "Тарифы вип-провайдера, тег Интернет + ТВ",
    "Тарифы вип-провайдера, тег Интернет + ТВ + мобильная связь",
    "Тарифы вип-провайдера, тег Интернет + Мобильная связь",
    "Тарифы вип-провайдера, тег Акции",
    "Тарифы в регионе",
    "Тарифы в регионе, тег Домашний интернет",
    "Тарифы в регионе, тег Интернет + ТВ",
    "Тарифы в регионе, тег Интернет+ТВ+Мобильная связь",
    "Тарифы в регионе, тег Интернет + Мобильная связь",
    "Тарифы в регионе, тег Акции",
    "Тарифы в регионе, тег 100 Мб/с",
    "Тарифы в регионе, тег 300 Мб/с",
    "Тарифы в регионе, тег 500 Мб/с",
    "Для Бизнеса (экс В офис)",
    "На дачу",
    "Сотрудничество",
    "О нас",
    "Оплата и гарантии",
    "Контакты",
    "Политика обработки персональных данных",
    "Все статьи блога",
    "Одна статья",
    "Все авторы блога",
    "Один автор",
    "Все разделы Частых вопросов",
    "Частые вопросы раздела Домашний интернет",
    "Ответ на один из частых вопросов",
    "Каталог моб операторов",
    "Карточка оператора",
    "Тарифы оператора",
    "Тарифы оператора с тегом Для модема/роутера",
    "Тарифы оператора с тегом Для ноутбука",
    "Тарифы оператора с тегом Безлимитные",
    "Тарифы оператора с тегом Выгодные",
    "Тарифы оператора с тегом Без абонентской платы",
    "Тарифы оператора с тегом Семейные",
    "Тарифы оператора с тегом Детские",
    "Тарифы оператора с тегом Роуминг за границей",
    "Тарифы оператора с тегом Связь по России",
    "Тарифы оператора с тегом eSIM",
    "Тарифы оператора с тегом Перейти со своим номером",
    "Каталог тарифов операторов",
    "Красивые номера оператора",
    "Красивые номера в регионе"
]

urls_stage = [
    host_stage + "piter-online.net/nalichie-provayderov-po-adresu",
    host_stage + "piter-online.net/select-region",
    host_stage + "piter-online.net/leningradskaya-oblast",
    host_stage + "piter-online.net/orders/tohome",
    host_stage + "piter-online.net/address",
    host_stage + "piter-online.net/address/%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA-id1250",
    host_stage + "piter-online.net/address/%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA-id1250/%D1%83%D0%BB-2-%D1%8F-%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%84%D0%BB%D0%BE%D1%82%D1%81%D0%BA%D0%B0%D1%8F-id295159",
    host_stage + "piter-online.net/leningradskaya-oblast/doma-nzl?house_id=4270758",
    host_stage + "piter-online.net/all-districts",
    host_stage + "piter-online.net/leningradskaya-oblast/site-map",
    host_stage + "piter-online.net/all-regions",
    host_stage + "piter-online.net/rating",
    host_stage + "piter-online.net/reviews",
    host_stage + "piter-online.net/rating/mts",
    host_stage + "piter-online.net/feedback",
    host_stage + "piter-online.net/providers",
    host_stage + "piter-online.net/providers/dom-ru",
    host_stage + "piter-online.net/providers/awanti",
    host_stage + "piter-online.net/providers/dom-ru/rates",
    host_stage + "piter-online.net/providers/dom-ru/rates/domashnij-internet",
    host_stage + "piter-online.net/providers/dom-ru/rates/internet-i-tv",
    host_stage + "piter-online.net/providers/rostelecom/rates/internet-tv-mobile",
    host_stage + "piter-online.net/providers/rostelecom/rates/internet-i-mobilnaya-svyaz",
    host_stage + "piter-online.net/providers/dom-ru/rates/nedorogoj-domashnij-internet",
    host_stage + "piter-online.net/rates",
    host_stage + "piter-online.net/rates/domashnij-internet",
    host_stage + "piter-online.net/rates/internet-i-tv",
    host_stage + "piter-online.net/rates/internet-tv-mobile",
    host_stage + "piter-online.net/rates/internet-i-mobilnaya-svyaz",
    host_stage + "piter-online.net/rates/nedorogoj-domashnij-internet",
    host_stage + "piter-online.net/rates/internet-100-mbit",
    host_stage + "piter-online.net/rates/internet-300-mbit",
    host_stage + "piter-online.net/rates/internet-500-mbit",
    host_stage + "piter-online.net/orders/office",
    host_stage + "piter-online.net/orders/sat",
    host_stage + "piter-online.net/about/partners",
    host_stage + "piter-online.net/about/company",
    host_stage + "piter-online.net/about/oplata-i-garantii",
    host_stage + "piter-online.net/about/contacts",
    host_stage + "piter-online.net/about/personal-data",
    host_stage + "piter-online.net/articles",
    host_stage + "piter-online.net/articles/luchshaya-simkarta-dlya-interneta",
    host_stage + "piter-online.net/experts",
    host_stage + "piter-online.net/experts/alisa-zhukova-id7",
    host_stage + "piter-online.net/help",
    host_stage + "piter-online.net/help/section-domashnij-internet",
    host_stage + "piter-online.net/help/kak-vybrat-luchshij-internet-tarif",
    host_stage + "piter-online.net/operatory",
    host_stage + "piter-online.net/operatory/mts",
    host_stage + "piter-online.net/operatory/mts/ratesmobile#tags#tags",
    host_stage + "piter-online.net/operatory/tele-2/ratesmobile/dlja-modema#tags ",
    host_stage + "piter-online.net/operatory/beeline/ratesmobile/dlja-noutbuka#tags",
    host_stage + "piter-online.net/operatory/tele-2/ratesmobile/bezlimitnyj-internet#tags",
    host_stage + "piter-online.net/operatory/tele-2/ratesmobile/vygodnye#tags",
    host_stage + "piter-online.net/operatory/beeline/ratesmobile/bez-abonentskoj-platy#tags",
    host_stage + "piter-online.net/operatory/beeline/ratesmobile/semeinye#tags",
    host_stage + "piter-online.net/operatory/beeline/ratesmobile/detskie#tags",
    host_stage + "piter-online.net/operatory/tele-2/ratesmobile/mezhdunarodnye#tags",
    host_stage + "piter-online.net/operatory/tele-2/ratesmobile/po-rossii#tags",
    host_stage + "piter-online.net/operatory/mts/ratesmobile/esim#tags",
    host_stage + "piter-online.net/operatory/mts/ratesmobile/perenos_nomera#tags",
    host_stage + "piter-online.net/ratesmobile",
    host_stage + "piter-online.net/operatory/mts/nomera",
    host_stage + "piter-online.net/nomera "
]

names_stage = [
    "Страница без адреса",
    "Селект регион",
    "Главная с регионом",
    "Поиск по адресу",
    "Карта покрытия",
    "Районы",
    "Улицы",
    "Дом",
    "Все районы",
    "Карта сайта",
    "Все регионы",
    "Рейтинг",
    "Отзывы в регионе",
    "Отзывы о провайдере",
    "Страница оставления отзыва",
    "Каталог провайдеров",
    "Страница вип-провайдера",
    "Страница провайдера Невип пров",
    "Тарифы вип-провайдера",
    "Тарифы вип-провайдера, тег Домашний интернет",
    "Тарифы вип-провайдера, тег Интернет + ТВ",
    "Тарифы вип-провайдера, тег Интернет + ТВ + мобильная связь",
    "Тарифы вип-провайдера, тег Интернет + Мобильная связь",
    "Тарифы вип-провайдера, тег Акции",
    "Тарифы в регионе",
    "Тарифы в регионе, тег Домашний интернет",
    "Тарифы в регионе, тег Интернет + ТВ",
    "Тарифы в регионе, тег Интернет+ТВ+Мобильная связь",
    "Тарифы в регионе, тег Интернет + Мобильная связь",
    "Тарифы в регионе, тег Акции",
    "Тарифы в регионе, тег 100 Мб/с",
    "Тарифы в регионе, тег 300 Мб/с",
    "Тарифы в регионе, тег 500 Мб/с",
    "Для Бизнеса (экс В офис)",
    "На дачу",
    "Сотрудничество",
    "О нас",
    "Оплата и гарантии",
    "Контакты",
    "Политика обработки персональных данных",
    "Все статьи блога",
    "Одна статья",
    "Все авторы блога",
    "Один автор",
    "Все разделы Частых вопросов",
    "Частые вопросы раздела Домашний интернет",
    "Ответ на один из частых вопросов",
    "Каталог моб операторов",
    "Карточка оператора",
    "Тарифы оператора",
    "Тарифы оператора с тегом Для модема/роутера",
    "Тарифы оператора с тегом Для ноутбука",
    "Тарифы оператора с тегом Безлимитные",
    "Тарифы оператора с тегом Выгодные",
    "Тарифы оператора с тегом Без абонентской платы",
    "Тарифы оператора с тегом Семейные",
    "Тарифы оператора с тегом Детские",
    "Тарифы оператора с тегом Роуминг за границей",
    "Тарифы оператора с тегом Связь по России",
    "Тарифы оператора с тегом eSIM",
    "Тарифы оператора с тегом Перейти со своим номером",
    "Каталог тарифов операторов",
    "Красивые номера оператора",
    "Красивые номера в регионе"
]
