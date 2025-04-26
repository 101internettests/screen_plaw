import os
import time

import allure
from playwright.sync_api import sync_playwright
from pages.orders_tohome_page import TohomePage
from pages.mol_main_page import SearchFromMain, TariffsSection, OpenPopUpAddress
from pages.mol_main_page import BlockProviders, ReviewBlockPage, PerelinkovkaCheck
from pages.review_page import ReviewPageFeedback
from pages.tariff_page import WindowPopUp, TariffPage
HEADLESS = True if os.getenv("HEADLESS") == "True" else False


class TestMolHousePage:
    @allure.title("Заявка тариф-подключить тег Домашний интернет")
    def test_application_tag_house_internet(self):
        full_url = "https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422/%D0%BC%D0%BA%D1%80-%D0%B3%D0%B0%D0%B3%D0%B0%D1%80%D0%B8%D0%BD%D0%B0-id294535"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = SearchFromMain(page=page)
            main_page.search_babyshkina()
            time.sleep(4)
            main_page.close_quiz()
            time.sleep(4)
            tariff_page = TariffPage(page=page)
            tariff_page.choose_price_before_oneth()
            tariff_page.choose_filter_all_providers()
            tariff_page.choose_filter_speed_200()
            tariff_page.accept_button_show_filters()
            tariff_page.use_sorting_button_speed()
            time.sleep(4)
            tariff_page.click_tariff_details_first_tariff()
            tariff_page.click_on_first_prov()
            time.sleep(3)
            tariff_page.quiz_send_appl()
            time.sleep(4)

    @allure.title("Заявка тариф-подключить тег Интернет и ТВ")
    def test_application_tag_house_internet_tv(self):
        full_url = "https://www.moskvaonline.ru/balashiha/address/%D0%B1%D0%B0%D0%BB%D0%B0%D1%88%D0%B8%D1%85%D0%B0-id422/%D0%BC%D0%BA%D1%80-%D0%B3%D0%B0%D0%B3%D0%B0%D1%80%D0%B8%D0%BD%D0%B0-id294535"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = SearchFromMain(page=page)
            main_page.search_babyshkina()
            time.sleep(4)
            main_page.close_quiz()
            time.sleep(4)
            tariff_page = TariffPage(page=page)
            tariff_page.choose_tag_internet_tv()
            tariff_page.choose_price_before_seven()
            tariff_page.choose_filter_all_providers()
            tariff_page.choose_filter_speed_100()
            tariff_page.accept_button_show_filters()
            tariff_page.use_sorting_button()
            tariff_page.click_tariff_details_four_tariff()
            time.sleep(3)
            tariff_page.click_on_four_prov()
            time.sleep(3)
            tariff_page.quiz_send_appl()
            time.sleep(4)







