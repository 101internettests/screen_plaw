import os
import time

import allure
from playwright.sync_api import sync_playwright
from pages.orders_tohome_page import TohomePage
from pages.pol_main_page import MainPage, SearchFromMain, TariffsSection
from pages.pol_main_page import BlockProviders
from pages.tariff_page import WindowPopUp, TariffPage, MiddlePage
HEADLESS = True if os.getenv("HEADLESS") == "True" else False


class TestPolRegionPage:
    @allure.title("Заявка через компонент поиска по адресу (квиз)")
    def test_application_search_for_address_quiz(self):
        full_url = "https://piter-online.net/vasileostrovskii-id1193"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = SearchFromMain(page=page)
            main_page.search_gorokhovaya()
            main_page.check_quiz()
            time.sleep(3)
            main_page.quiz_send_appl()
            time.sleep(3)
            main_page.close_quiz()
            time.sleep(59)

    @allure.title("Заявка через компонент перелинковки (квиз)")
    def test_application_perelinkovki_quiz(self):
        full_url = "https://piter-online.net/ulicy/internet-provaydery-ul-repina-id272648"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = SearchFromMain(page=page)
            # main_page.choose_r_letter()
            # time.sleep(3)
            # main_page.choose_repina_street()
            main_page.choose_twenty_seven_house()
            # main_page.check_quiz()
            time.sleep(3)
            main_page.quiz_send_appl()
            time.sleep(3)
            main_page.close_quiz()
            time.sleep(59)

    @allure.title("Переход на страницу поиска без адреса через перелинковку района")
    def test_transition_search_page_from_perelinkovka(self):
        full_url = "https://piter-online.net/vasileostrovskii-id1193"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tohome_page = TohomePage(page=page)
            tohome_page.click_on_not_address_block()
            tohome_page.check_address_page_pol()

    @allure.title("Кнопка Показать ещё в перелинковке работает")
    def test_check_button(self):
        full_url = "https://piter-online.net/vasileostrovskii-id1193"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = SearchFromMain(page=page)
            main_page.choose_more_27streets()
            main_page_screen = MainPage(page=page)
            main_page_screen.make_screenshot()
            time.sleep(4)

    @allure.title("Заявка через компонент поиска по адресу в блоке провайдеров (квиз)")
    def test_application_search_providers_quiz(self):
        full_url = "https://piter-online.net/vasileostrovskii-id1193"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            block_page = BlockProviders(page=page)
            block_page.click_search_domru()
            popup_page = WindowPopUp(page=page)
            popup_page.choose_in_business()
            popup_page.choose_in_sat()
            popup_page.choose_in_flat()
            popup_page.fill_the_application_with_address_vasil()
            main_page = SearchFromMain(page=page)
            time.sleep(4)
            main_page.check_quiz()
            main_page.quiz_send_appl()
            time.sleep(3)
            main_page.close_quiz()
            time.sleep(59)

    @allure.title("Заявка через компонент поиска по адресу под блоком провайдеров (адрес-тариф-подключить, "
                  "без фильтрации и сортировки)")
    def test_application_search_providers_withoutfilters(self):
        full_url = "https://piter-online.net/vasileostrovskii-id1193"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            block_page = BlockProviders(page=page)
            block_page.click_all_providers_button()
            popup_page = WindowPopUp(page=page)
            popup_page.choose_in_business()
            popup_page.choose_in_sat()
            popup_page.choose_in_flat()
            popup_page.fill_the_application_with_address_second()
            main_page = SearchFromMain(page=page)
            main_page.close_quiz()
            time.sleep(3)
            tariff_page = TariffPage(page=page)
            tariff_page.fill_the_application()
            time.sleep(59)

    @allure.title("Заявка через компонент поиска по адресу в середине страницы (адрес-тариф-подключить, "
                  "без фильтрации).")
    def test_application_in_middle_page(self):
        full_url = "https://piter-online.net/vasileostrovskii-id1193"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            middle_page = MiddlePage(page=page)
            middle_page.fill_the_application_with_address_new_gorox()
            time.sleep(3)
            main_page = SearchFromMain(page=page)
            main_page.close_quiz()
            time.sleep(3)
            tariff_page = TariffPage(page=page)
            tariff_page.fill_the_application()
            time.sleep(59)

    @allure.title("Заявка через компонент с тарифами (с просмотром деталей тарифа)")
    def test_application_tariff_with_details(self):
        full_url = "https://piter-online.net/vasileostrovskii-id1193"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tariff_section = TariffsSection(page=page)
            tariff_section.click_on_more_about_tariff_second()
            tariff_section.check_modal_window_more_about_tariffs()
            tariff_section.close_more_about_tariff()
            time.sleep(4)
            tariff_section.fill_the_application_with_address_gagarina()
            time.sleep(59)

    @allure.title("Заявка через компонент поиска по адресу под блоком тарифы (адрес-тариф-подключить, без фильтрации)")
    def test_application_search_from_tariffs_without_filters(self):
        full_url = "https://piter-online.net/vasileostrovskii-id1193"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tariff_section = TariffsSection(page=page)
            tariff_section.click_on_button_find_tariffs()
            main_page = SearchFromMain(page=page)
            main_page.search_vesennya()
            main_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.fill_the_application_second_tariff()
            time.sleep(59)