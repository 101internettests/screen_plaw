import os
import time
import allure
from playwright.sync_api import sync_playwright
from pages.pol_main_page import MainPage, SelectRegionPage, SearchFromMain, SearchFromMain, TariffsSection, BlockProviders
from pages.tariff_page import WindowPopUp
from pages.pol_main_page import OpenPopUpAddress
from pages.orders_tohome_page import TohomePage, TohomePolPage
from pages.tariff_page import TariffPage
from config import pol_url
HEADLESS = True if os.getenv("HEADLESS") == "True" else False


class TestPolSearch:
    @allure.title("Выбрать район из блока перелинковки")
    def test_choose_region(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_admir_area()

    @allure.title("Выбрать улицу из блока перелинковки")
    def test_choose_street(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_admir_area()
            search_page.choose_eng_street()

    @allure.title("Перейти на страницу поиска без адреса через перелинковку")
    def test_without_address(self):
        full_url = f"{pol_url}orders/tohome"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tohome_page = TohomePage(page=page)
            tohome_page.click_on_not_address_block()
            tohome_page.check_address_page_pol()
            time.sleep(3)

    @allure.title("Отправить заявку через компонент перелинковки (квиз)")
    def test_perelinkovka_quiz(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_vasil_area()
            search_page.choose_shev_street()
            search_page.choose_three_house()
            search_page.check_quiz()
            time.sleep(3)
            search_page.quiz_send_appl()
            time.sleep(3)
            search_page.close_quiz()

    @allure.title("Отправить заявку через компонент перелинковки (адрес-тариф-подключить, фильтрация по провайдеру, сортировка по цене без учёта акций)")
    def test_perelinkovka_second_quiz(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_vasil_area()
            search_page.choose_shev_street()
            search_page.choose_three_house()
            search_page.check_quiz()
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.choose_filter_bilain_providers()
            tariff_page.choose_filter_house_providers()
            tariff_page.choose_filter_rostel_providers()
            tariff_page.accept_button_show_filters()
            tariff_page.check_accepted_filters()
            tariff_page.use_sorting_button()
            tariff_page.show_more_button()
            tariff_page.show_more_button()
            tariff_page.show_more8_button()
            time.sleep(4)
            tariff_page.click_on_lat_prov()
            tariff_page.quiz_send_appl()
            time.sleep(4)
            search_page.close_quiz()

    @allure.title("Проверить переход по разным районам и улицам в перелинковке (без заявок)")
    def test_check_transfer(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_admir_area()
            search_page.choose_ya_letter()
            search_page.choose_ya_street()
            search_page.choose_admir_breadcrumps()
            search_page.choose_more_streets()
            search_page.choose_krasn_street()
            search_page.choose_type_search_flat()
            search_page.choose_u_letter()
            search_page.choose_ugo_zapad_area()
            search_page.choose_peter_street()
            search_page.choose_five_house()
            search_page.close_quiz()
            time.sleep(3)

    @allure.title("Отправить заявку через компонент поиска по адресу в блоке провайдеров (адрес-тариф-подключить, без фильтрации)")
    def test_application_in_prov_block(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            prov_page = BlockProviders(page=page)
            prov_page.click_search_sat()
            popup_page = OpenPopUpAddress(page=page)
            popup_page.check_popup_window()
            window_popup = WindowPopUp(page=page)
            window_popup.choose_in_business()
            window_popup.choose_in_sat()
            window_popup.choose_in_flat()
            time.sleep(2)
            window_popup.fill_the_application_with_address()
            search_page.close_quiz()
            tariff_page = TariffsSection(page=page)
            tariff_page.fill_the_application_with_address_second()
            search_page.close_quiz()
            time.sleep(3)

    @allure.title(
        "Отправить заявку через компонент поиска по адресу под блоком провайдеров (адрес-фильтр-подключить, фильтрация по провайдеру, скорости и цене)")
    def test_application_below_prov_block(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            prov_page = BlockProviders(page=page)
            prov_page.click_all_providers_button()
            popup_page = OpenPopUpAddress(page=page)
            popup_page.check_popup_window()
            window_popup = WindowPopUp(page=page)
            window_popup.choose_in_business()
            window_popup.choose_in_sat()
            window_popup.choose_in_flat()
            time.sleep(2)
            window_popup.fill_the_application_with_address_second()
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.choose_price_before_oneth()
            tariff_page.choose_filter_house_providers()
            tariff_page.choose_filter_speed_200()
            tariff_page.accept_button_show_filters()
            time.sleep(4)
            tariff_page.click_on_lat_prov()
            tariff_page.quiz_send_appl()
            time.sleep(4)
            search_page.close_quiz()
            time.sleep(3)

    @allure.title("Отправить заявку через компонент поиска по адресу в середине страницы (адрес-тариф-подключить, без фильтрации)")
    def test_application_in_the_middle_page(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page = SearchFromMain(page=page)
            search_page.search_gorokhovaya()
            search_page.check_quiz()
            search_page.quiz_send_appl()
            search_page.close_quiz()
            time.sleep(3)

    @allure.title("Отправить заявку через компонент перелинковки (адрес-тариф-подключить, без фильтрации)")
    def test_perelinkovka_address_without_filter(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            tohome_page = TohomePage(page=page)
            tohome_page.search_gorokhovaya()
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.fill_the_application()

    @allure.title("Отправить заявку через компонент с тарифами")
    def test_send_application_from_tariff_component(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            tohome_pol = TohomePolPage(page=page)
            tohome_pol.check_header_pol()
            tariff_page = TariffsSection(page=page)
            tohome_pol.fill_the_application_with_address_vesn_second()
            time.sleep(4)

    @allure.title("Посмотреть детали тарифа")
    def test_check_tariff_details(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            tariff_page = TariffsSection(page=page)
            tariff_page.click_on_tariff_details()

    @allure.title("Отправить заявку через компонент поиска по адресу под блоком тарифы (адрес-тариф-подключить, без фильтрации)")
    def test_application_search_tariffs_without_filters(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            tariff_page = TariffsSection(page=page)
            tariff_page.click_on_button_find_tariffs()
            tohome_pol = TohomePolPage(page=page)
            tohome_pol.fill_the_application_with_address_vesn()
            search_page.close_quiz()
            tariff_page.fill_the_application_with_address_second()
            time.sleep(5)
