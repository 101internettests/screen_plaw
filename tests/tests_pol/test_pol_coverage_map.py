import os
import time

import allure
from playwright.sync_api import sync_playwright
from pages.mol_pages.map_coverage_page import MapCoveragePage
from pages.pol_main_page import SearchFromMain, TariffsSection, OpenPopUpAddress
from pages.pol_main_page import BlockProviders, MainPage
from pages.orders_tohome_page import TohomePage
from pages.select_region_page import SelectRegionPage
from pages.tariff_page import WindowPopUp
from pages.tariff_page import TariffPage
from config import pol_url
HEADLESS = True if os.getenv("HEADLESS") == "True" else False


class TestMolMainWithRegion:
    @allure.title("Выбор района из блока перелинковки")
    def test_choose_region_perelinkovka(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_page.choose_gatchina()

    @allure.title("Выбор улицы из блока перелинковки")
    def test_choose_street_perelinkovka(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_page.choose_gatchina()
            search_page.choose_marks_street()

    @allure.title("Заявка через компонент перелинковки (квиз)")
    def test_perelinkovka_quiz(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_page.choose_vasil_area()
            search_page.choose_shev_street()
            search_page.choose_three_house()
            search_page.check_quiz()
            time.sleep(3)
            search_page.quiz_send_appl()
            time.sleep(3)
            search_page.close_quiz()

    @allure.title("Заявка через компонент перелинковки (адрес-тариф-подключить, фильтрация по провайдеру, сортировка по цене без учёта акций)")
    def test_application_perelinkovka_with_filters(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_home = SearchFromMain(page=page)
            search_page.choose_vasil_area()
            search_page.choose_shev_street()
            search_page.choose_three_house()
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.choose_filter_house_providers()
            tariff_page.choose_filter_bilain_providers()
            tariff_page.choose_filter_rostel_providers()
            tariff_page.use_sorting_button()
            tariff_page.accept_button_show_filters()
            tariff_page.show_more10_from30_button()
            tariff_page.show_more10_from30_button()
            time.sleep(4)
            tariff_page.click_on_lat_prov()
            tariff_page.quiz_send_appl()
            time.sleep(4)
            search_page.close_quiz()

    @allure.title("Переход по разным районам и улицам в перелинковке (без заявок)")
    def test_perelinkovka_without_application(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
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
    #
    @allure.title("Заявка через компонент поиска по адресу в блоке провайдеров (адрес-тариф-подключить, без фильтрации)")
    def test_application_from_search_without_filtres(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            prov_page = BlockProviders(page=page)
            prov_page.click_search_sat()
            popup_page = OpenPopUpAddress(page=page)
            popup_page.check_popup_window()
            popup_page.choose_in_business()
            popup_page.choose_in_sat()
            popup_page.choose_in_flat()
            time.sleep(7)
            popup_page.fill_the_application_with_address()
            main_page = MainPage(page=page)
            time.sleep(2)
            search_page = SearchFromMain(page=page)
            search_page.quiz_send_appl()
            time.sleep(3)
            main_page.close_popup_wait_for_call()
            tariff_page = TariffPage(page=page)
            tariff_page.check_tag_home_internet()
            tariff_page.fill_the_application()

    @allure.title(
        "Заявка через компонент поиска по адресу под блоком провайдеров (адрес-тариф-подключить, фильтрация по провайдеру, скорости и цене)")
    def test_application_from_search_prov_block_with_filtres(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            block_page = BlockProviders(page=page)
            block_page.check_providers_block()
            block_page.click_all_providers_button()
            popup_page = OpenPopUpAddress(page=page)
            popup_page.check_popup_window()
            popup_page.choose_in_business()
            popup_page.choose_in_sat()
            popup_page.choose_in_flat()
            popup_page.fill_the_application_with_address_second()
            search_page = SearchFromMain(page=page)
            search_page.check_quiz()
            search_page.close_quiz()
            time.sleep(5)
            tariff_page = TariffPage(page=page)
            tariff_page.check_tag_home_internet()
            tariff_page.choose_price_before_oneth()
            tariff_page.choose_filter_all_providers()
            tariff_page.choose_filter_speed_200()
            tariff_page.accept_button_show_filters()
            tariff_page.check_tag_home_internet()
            tariff_page.click_on_tariff_with_200()
            main_page = MainPage(page=page)
            time.sleep(2)
            tariff_page.send_popup_wait_for_call()
            # main_page.check_success_popups()
            main_page.close_popup_wait_for_call()

    @allure.title("Заявка через компонент поиска по адресу (квиз)")
    def test_application_from_search_quiz(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_page.search_gorokhovaya()
            search_page.quiz_send_appl()
            time.sleep(3)
            search_page.close_quiz()

    @allure.title("Заявка через компонент поиска по адресу (неудачный квиз)")
    def test_application_from_search_unsuccessful_quiz(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            map_page = MapCoveragePage(page=page)
            map_page.search_address_gor()
            map_page.put_on_search_button()
            select_page = SelectRegionPage(page=page)
            select_page.choose_saintp()
            search_page.choose_admir_area()
            search_page.choose_gorox_street()
            search_page.choose_first_house()
            time.sleep(3)
            search_page.quiz_send_appl()
            time.sleep(4)
            search_page.close_quiz()
            time.sleep(3)

    @allure.title("Переход на страницу поиска без адреса через перелинковку улиц")
    def test_appear_in_search_page(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            tohome_page = TohomePage(page=page)
            tohome_page.click_on_not_address_block()
            tohome_page.check_address_page_pol()
            time.sleep(3)