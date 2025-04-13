import os
import time

import allure
from playwright.sync_api import sync_playwright
from pages.orders_tohome_page import TohomePage
from pages.pol_main_page import MainPage, SelectRegionPage, SearchFromMain, TariffsSection, ReviewCatPopup, OpenPopUpAddress
from pages.pol_main_page import BlockProviders, ReviewBlockPage, PerelinkovkaCheck
from pages.review_page import ReviewPageFeedback
from pages.tariff_page import WindowPopUp, TariffPage, MiddlePage
from pages.orders_office_page import OfficePage
from pages.sat_page import SatPage
HEADLESS = True if os.getenv("HEADLESS") == "True" else False


class TestMolStreetPage:
    @allure.title("Заявка через компонент поиска по адресу (квиз)")
    def test_application_search_for_address_quiz(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-verislutskoi-id295004"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = SearchFromMain(page=page)
            main_page.search_radchenko()
            main_page.check_quiz()
            main_page.quiz_send_appl()
            time.sleep(4)
            main_page.close_quiz()

    @allure.title("Заявка через компонент перелинковки (квиз)")
    def test_application_perelinkovki_quiz(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-verislutskoi-id295004"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = SearchFromMain(page=page)
            main_page.choose_fifty_four_house()
            main_page.check_quiz()
            main_page.quiz_send_appl()
            time.sleep(3)
            main_page.close_quiz()

    @allure.title("Переход на страницу поиска без адреса через перелинковку улиц")
    def test_transition_search_page_from_perelinkovka(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-verislutskoi-id295004"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tohome_page = TohomePage(page=page)
            tohome_page.click_on_not_address_block()
            tohome_page.check_address_page_pol_kolpino()

    @allure.title("Заявка через компонент поиска по адресу в блоке провайдеров (квиз)")
    def test_application_search_providers_quiz(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-verislutskoi-id295004"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            block_page = BlockProviders(page=page)
            block_page.click_search_bilain()
            wind_page = WindowPopUp(page=page)
            popup_page = OpenPopUpAddress(page=page)
            popup_page.choose_in_business()
            popup_page.choose_in_sat()
            popup_page.choose_in_flat()
            wind_page.fill_the_application_with_address_only_house_forty_eight()
            main_page = SearchFromMain(page=page)
            time.sleep(4)
            main_page.check_quiz()
            time.sleep(4)
            main_page.quiz_send_appl()
            time.sleep(3)
            main_page.close_quiz()

    @allure.title(
        "Заявка через компонент поиска по адресу под блоком провайдеров (адрес-тариф-подключить, без фильтрации и сортировки)")
    def test_application_search_providers_withoutfilters(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-verislutskoi-id295004"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            block_page = BlockProviders(page=page)
            block_page.click_all_providers_button()
            popup_page = OpenPopUpAddress(page=page)
            popup_page.choose_in_business()
            popup_page.choose_in_sat()
            popup_page.choose_in_flat()
            wind_page = WindowPopUp(page=page)
            wind_page.fill_the_application_with_address_only_house_forty_eight()
            main_page = SearchFromMain(page=page)
            main_page.close_quiz()
            time.sleep(3)
            tariff_page = TariffPage(page=page)
            tariff_page.fill_the_application_with_address_pol()
            time.sleep(2)

    @allure.title("Заявка через компонент с тарифами (с просмотром деталей тарифа)")
    def test_application_tariff_with_details(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-verislutskoi-id295004"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tariff_section = TariffsSection(page=page)
            tariff_section.click_on_tariff_details()
            tariff_section.check_modal_window_more_about_tariffs()
            tariff_section.click_on_more_about_tariff()
            tariff_section.close_more_about_tariff()
            time.sleep(3)
            tariff_section.fill_the_application_with_address_third()
            time.sleep(3)

    @allure.title("Заявка через компонент поиска по адресу под блоком тарифы (адрес-тариф-подключить, без фильтрации)")
    def test_application_search_from_tariffs_without_filters(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-verislutskoi-id295004"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tariff_section = TariffsSection(page=page)
            tariff_section.click_on_button_find_tariffs()
            main_page = SearchFromMain(page=page)
            main_page.search_working()
            main_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.fill_the_application_with_address_third()
            time.sleep(3)

    @allure.title("Написать отзыв со страницы улицы")
    def test_write_review(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-bratevradchenko-id295002"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            review_block_page = ReviewBlockPage(page=page)
            review_block_page.check_review_block_street_page()
            review_feedback = ReviewPageFeedback(page=page)
            time.sleep(3)
            review_feedback.click_on_write_review_street()
            review_feedback.leave_feedback()
            review_feedback.go_back()

    @allure.title("Проверка человеческой перелинковки")
    def test_people_perelinkovka(self):
        full_url = "https://piter-online.net/kolpino/ulicy/internet-provaydery-ul-verislutskoi-id295004"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            perelinkovka_page = PerelinkovkaCheck(page=page)
            perelinkovka_page.click_other_streets()
            perelinkovka_page.click_marks_street()
            time.sleep(2)
            perelinkovka_page.click_other_streets()
            perelinkovka_page.click_mashinostroy_street()
            time.sleep(2)
            perelinkovka_page.click_other_streets()
            perelinkovka_page.click_oktiabiriskaya_street()