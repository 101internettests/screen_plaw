import os
import time
import allure
from playwright.sync_api import sync_playwright
from pages.mol_main_page import MainPage, SelectRegionPage, SearchFromMain, BlockProviders, OpenPopUpAddress, TariffsSection
from pages.tariff_page import WindowPopUp, TariffPage
from pages.orders_tohome_page import TohomePage, TohomeMol
from config import mol_url
HEADLESS = True if os.getenv("HEADLESS") == "True" else False


class TestMolSearch:
    @allure.title("Выбрать район из блока перелинковки")
    def test_choose_region(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_akad_area()
            search_page.choose_grem_street()

    @allure.title("Перейти на страницу поиска без адреса через перелинковку")
    def test_without_address(self):
        full_url = f"{mol_url}orders/tohome"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tohome_page = TohomePage(page=page)
            tohome_page.click_on_not_address_block()
            tohome_page.check_address_page_mol()
            time.sleep(3)

    @allure.title("Отправить заявку через компонент перелинковки (квиз)")
    def test_perelinkovka_quiz(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_akad_area()
            search_page.choose_fersm_street()
            search_page.choose_three_house()
            search_page.check_quiz()
            time.sleep(3)
            search_page.quiz_send_appl()
            time.sleep(3)
            search_page.close_quiz()

    @allure.title(
        "Отправить заявку через компонент поиска по адресу в блоке провайдеров (адрес-тариф-подключить, без фильтрации)")
    def test_application_in_prov_block(self):
        full_url = f"{mol_url}"
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
            window_popup.fill_the_application_with_address_shar()
            search_page.close_quiz()
            tariff_page = TariffsSection(page=page)
            tariff_page.fill_the_application_with_address_second()
            search_page.close_quiz()
            time.sleep(3)

    @allure.title(
        "Отправить заявку через компонент поиска по адресу под блоком провайдеров (адрес-фильтр-подключить, фильтрация по провайдеру, скорости и цене)")
    def test_application_below_prov_block(self):
        full_url = f"{mol_url}"
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
            window_popup.fill_the_application_with_address_shar()
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
            time.sleep(4)
            search_page.close_quiz()
            time.sleep(3)

    @allure.title("Посмотреть детали тарифа")
    def test_check_tariff_details(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            tariff_page = TariffsSection(page=page)
            tariff_page.click_on_tariff_details()

    @allure.title(
        "Отправить заявку через компонент поиска по адресу под блоком тарифы (адрес-тариф-подключить, без фильтрации)")
    def test_application_search_tariffs_without_filters(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            tariff_page = TariffsSection(page=page)
            tariff_page.click_on_button_find_tariffs()
            tohome_pol = TohomeMol(page=page)
            tohome_pol.fill_the_application_with_address_gag()
            search_page.close_quiz()
            tohome_pol.fill_the_application_with_address_mol()

    @allure.title("Отправить заявку через компонент с тарифами")
    def test_send_application_from_tariff_component(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            tohome_mol = TohomeMol(page=page)
            tohome_mol.check_header_mol()
            tariff_page = TariffsSection(page=page)
            tohome_mol.fill_the_application_with_address_vesn_second()
            time.sleep(4)

    @allure.title("Отправить заявку через компонент поиска по адресу (квиз)")
    def test_perelinkovka_quiz(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.search_purple()
            search_page.quiz_send_appl()
            time.sleep(3)
            search_page.close_quiz()

    @allure.title(
        "Отправить заявку через компонент перелинковки (адрес-тариф-подключить, фильтрация по провайдеру, сортировка по цене без учёта акций)")
    def test_perelinkovka_second_quiz(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_akad_area()
            search_page.choose_fersm_street()
            search_page.choose_three_house()
            search_page.check_quiz()
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.choose_filter_almatel_providers()
            tariff_page.choose_filter_mts_providers()
            tariff_page.choose_filter_megafone_providers()
            tariff_page.accept_button_show_filters()
            tariff_page.check_accepted_filters()
            tariff_page.use_sorting_button()
            tariff_page.show_more10_button()
            tariff_page.show_more2_button()
            time.sleep(4)
            tariff_page.click_on_lat_prov()
            tariff_page.quiz_send_appl()
            time.sleep(4)
            search_page.close_quiz()

    @allure.title("Проверить переход по разным районам и улицам в перелинковке (без заявок)")
    def test_check_transfer(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page.choose_aero_area()
            search_page.choose_u_letter()
            search_page.choose_eldore_street()
            search_page.choose_aero_breadcrumps()
            search_page.choose_eight_letter()
            search_page.choose_type_search_flat()
            search_page.choose_uu_letter()
            search_page.choose_butovo_area()
            search_page.choose_brusilov_street()
            search_page.choose_fifteen_house()
            search_page.close_quiz()
            time.sleep(3)

    @allure.title(
        "Отправить заявку через компонент поиска по адресу в середине страницы (адрес-тариф-подключить, без фильтрации)")
    def test_application_in_the_middle_page(self):
        full_url = f"{mol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.check_if_is_choose_area_block()
            search_page = SearchFromMain(page=page)
            search_page.search_purple()
            search_page.check_quiz()
            search_page.quiz_send_appl()
            search_page.close_quiz()
            time.sleep(3)
