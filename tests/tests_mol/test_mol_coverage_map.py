import os
import time
import allure
from playwright.sync_api import sync_playwright
from pages.mol_pages.map_coverage_page import MapCoveragePage
from pages.mol_main_page import SearchFromMain, OpenPopUpAddress
from pages.mol_main_page import BlockProviders
from pages.orders_tohome_page import TohomePage
from pages.tariff_page import TariffPage
from config import mol_url
HEADLESS = True if os.getenv("HEADLESS") == "True" else False


class TestMolMainWithRegion:
    @allure.title("Выбор района и улицы из блока перелинковки")
    def test_choose_region_steet_perelinkovka(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_home = SearchFromMain(page=page)
            search_page.choose_akad_area()
            search_home.choose_grem_street()

    @allure.title("Заявка через компонент перелинковки (квиз)")
    def test_perelinkovka_quiz(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_home = SearchFromMain(page=page)
            search_page.choose_akad_area()
            search_home.choose_fersm_street()
            search_page.choose_three_house()
            # search_page.check_quiz()
            time.sleep(3)
            search_page.quiz_send_appl()
            time.sleep(3)
            search_page.close_quiz()
            time.sleep(55)

    @allure.title("Заявка через компонент перелинковки (адрес-тариф-подключить, фильтрация по провайдеру, сортировка по цене без учёта акций)")
    def test_application_perelinkovka_with_filters(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_home = SearchFromMain(page=page)
            search_page.choose_akad_area()
            search_home.choose_fersm_street()
            search_page.choose_three_house()
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.choose_filter_almatel_providers()
            tariff_page.choose_filter_mts_providers()
            tariff_page.choose_filter_megafone_providers()
            tariff_page.use_sorting_button()
            tariff_page.accept_button_show_filters()
            time.sleep(4)
            tariff_page.click_on_lat_prov()
            time.sleep(4)
            tariff_page.quiz_send_appl()
            time.sleep(55)

    @allure.title("Переход по разным районам и улицам в перелинковке + дом (без заявок)")
    def test_perelinkovka_without_application(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_page.choose_aero_area()
            search_page.choose_u_letter()
            time.sleep(3)
            search_page.choose_eldore_street()
            time.sleep(3)
            search_page.choose_aero_breadcrumps()
            time.sleep(3)
            search_page.choose_eight_letter()
            search_page.choose_type_search_flat()
            time.sleep(3)
            search_page.choose_uu_letter()
            search_page.choose_butovo_area()
            search_page.choose_brusilov_street()
            search_page.choose_fifteen_house()
            search_page.close_quiz()

    @allure.title("Заявка через компонент поиска по адресу в блоке провайдеров (адрес-тариф-подключить, без фильтрации)")
    def test_application_from_search_without_filtres(self):
        full_url = f"{mol_url}"
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
            time.sleep(2)
            map_page = MapCoveragePage(page=page)
            map_page.search_address()
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.fill_the_application_with_address_second()
            search_page.close_quiz()
            time.sleep(55)

    @allure.title(
        "Заявка через компонент поиска по адресу под блоком провайдеров (адрес-тариф-подключить, фильтрация по "
        "провайдеру, скорости и цене)")
    def test_application_from_search_prov_block_with_filtres(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            prov_page = BlockProviders(page=page)
            prov_page.click_all_providers_button()
            popup_page = OpenPopUpAddress(page=page)
            popup_page.check_popup_window()
            popup_page.choose_in_business()
            popup_page.choose_in_sat()
            popup_page.choose_in_flat()
            time.sleep(2)
            map_page = MapCoveragePage(page=page)
            map_page.search_address()
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.choose_price_before_oneth()
            tariff_page.choose_filter_megafone_providers()
            tariff_page.choose_filter_speed_200()
            tariff_page.accept_button_show_filters()
            time.sleep(4)
            tariff_page.click_on_lat_prov()
            time.sleep(4)
            tariff_page.quiz_send_appl()
            time.sleep(55)
            # search_page.close_quiz()

    @allure.title("Заявка через компонент поиска по адресу (квиз)")
    def test_application_from_search_quiz(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            search_page.search_purple()
            search_page.quiz_send_appl()
            time.sleep(3)
            search_page.close_quiz()
            time.sleep(60)

    @allure.title("Заявка через компонент поиска по адресу (неудачный квиз)")
    def test_application_from_search_unsuccessful_quiz(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            map_page = MapCoveragePage(page=page)
            map_page.search_address_arbat()
            # map_page.put_on_search_button()
            # select_page = SelectRegionPage(page=page)
            # select_page.choose_moscow()
            # search_page.choose_altuf()
            # search_page.choose_standart_street()
            # search_page.choose_first_house()
            # search_page.quiz_send_appl()
            # time.sleep(4)
            # search_page.close_quiz()

    @allure.title("Переход на страницу поиска без адреса через перелинковку улиц")
    def test_appear_in_search_page(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_coverage_map()
            tohome_page = TohomePage(page=page)
            tohome_page.click_on_not_address_block()
            tohome_page.check_address_page_mol()