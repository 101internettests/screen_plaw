import os
import time

import allure
from playwright.sync_api import sync_playwright
from pages.pol_main_page import MainPage, SelectRegionPage, SearchFromMain, TariffsSection, ReviewCatPopup, OpenPopUpAddress, BlockProviders, ReviewBlockPage
from pages.orders_office_page import OfficePage
from pages.review_page import ReviewPageFeedback
from pages.tariff_page import TariffPage
from pages.sat_page import SatPage
from config import pol_url
HEADLESS = True if os.getenv("HEADLESS") == "True" else False

class TestPolMainWithRegion:
    @allure.title("Выбрать регион из хедера")
    def test_choose_region_from_header(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.open_select_region_window()
            select_page = SelectRegionPage(page=page)
            select_page.check_select_region_page()
            select_page.choose_leningrad_region()
            main_page.check_header_city()
            main_page.check_main_page_has_leningrad_region()

    @allure.title("Выбрать район из хедера")
    def test_choose_district_from_header(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.open_select_region_window()
            select_page = SelectRegionPage(page=page)
            select_page.check_select_region_page()
            main_page.choose_sertolovo()
            main_page.check_header_sertolovo()
            with allure.step("Проверить, что URL соответствует ожидаемому для Сертолово"):
                expected_url = "https://piter-online.net/leningradskaya-oblast/sertolovo-id386"
                current_url = page.url
                assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"

    @allure.title("Отправить заявку из попапа жду звонка")
    def test_send_popup_waitforcall(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.open_popup_wait_for_call()
            main_page.send_popup_wait_for_call()
            main_page.check_success_popups()
            main_page.close_popup_wait_for_call()

    @allure.title("Отправить заявку из попапа жду звонка из хедера")
    def test_send_popup_waitforcall_footer(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.open_popup_wait_for_call_footer()
            main_page.send_popup_wait_for_call()
            main_page.check_success_popups()
            main_page.close_popup_wait_for_call()

    @allure.title("Проверить кото-баннер аи")
    def test_check_catbanner_ai(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.check_cat_ai()
            main_page.use_cat_ai_help()

    @allure.title("Проверить заявку через компонент поиска по адресу (квиз)")
    def test_send_application_quiz(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.search_gorokhovaya()
            search_page.check_quiz()
            search_page.quiz_send_appl()
            main_page = MainPage(page=page)
            main_page.check_success_popups()
            main_page.close_popup_wait_for_call()

    @allure.title("Проверить заявку через компонент поиска по адресу (адрес-тариф подключить, без фильтрации)")
    def test_send_application_address(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_flat()
            search_page.search_gorokhovaya()
            search_page.check_quiz()
            search_page.close_quiz()
            time.sleep(5)
            tariff_page = TariffPage(page=page)
            tariff_page.check_tag_home_internet()
            tariff_block = TariffsSection(page=page)
            time.sleep(7)
            tariff_page.fill_the_application()
            main_page = MainPage(page=page)
            time.sleep(2)
            main_page.check_success_popups()
            main_page.close_popup_wait_for_call()

    @allure.title("Проверить вкладку Для бизнеса")
    def test_check_for_business_page(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_business()
            with page.expect_navigation():
                search_page.click_tender_button()
            expected_url = "https://piter-online.net/orders/office"
            page.wait_for_url(expected_url)
            with allure.step("Проверить, что URL соответствует ожидаемому"):
                current_url = page.url
                assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"
            office_page = OfficePage(page=page)
            office_page.check_breadcrumbs()
            with page.expect_navigation():
                office_page.return_to_the_main_page()
            expected_url = "https://piter-online.net/"
            page.wait_for_url(expected_url)
            with allure.step("Проверить, что URL соответствует ожидаемому"):
                current_url = page.url
                assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"
                time.sleep(4)

    @allure.title("Проверить вкладку Интернет на дачу")
    def test_check_for_sat_page(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            search_page = SearchFromMain(page=page)
            search_page.choose_type_search_garden()
            with page.expect_navigation():
                search_page.click_all_garden_tariffs()
            expected_url = "https://piter-online.net/orders/sat"
            page.wait_for_url(expected_url)
            with allure.step("Проверить, что URL соответствует ожидаемому"):
                current_url = page.url
                assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"
            office_page = SatPage(page=page)
            office_page.check_breadcrumbs()
            with page.expect_navigation():
                office_page.return_to_the_main_page()
            expected_url = "https://piter-online.net/"
            page.wait_for_url(expected_url)
            with allure.step("Проверить, что URL соответствует ожидаемому"):
                current_url = page.url
                assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"
                time.sleep(4)

    @allure.title("Заявка через компонент с тарифами")
    def test_send_application_from_component_with_tariffs(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tariff_page = TariffsSection(page=page)
            tariff_page.check_tariffs_section()
            tariff_page.fill_the_application_with_address()
            main_page = MainPage(page=page)
            time.sleep(2)
            main_page.check_success_popups()
            main_page.close_popup_wait_for_call()

    @allure.title("Посмотреть детали тарифа")
    def test_check_tariff_details(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tariff_page = TariffsSection(page=page)
            tariff_page.check_tariffs_section()
            tariff_page.find_price_in_tariffs()
            time.sleep(5)
            tariff_page.click_on_tariff_details()
            time.sleep(3)
            tariff_page.click_on_more_about_tariff()
            tariff_page.check_modal_window_more_about_tariffs()
            tariff_page.close_more_about_tariff()

    @allure.title("Отправить обратную связь с главной страницы")
    def test_send_review_cat(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            review_page = ReviewCatPopup(page=page)
            review_page.open_popup_cat_website()
            review_page.leave_feedback_cat()

    @allure.title("Кнопка подняться наверх работает")
    def test_catupper_button(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.check_cat_upper()
            main_page.make_screenshot()

    @allure.title("Заявка через компонент поиска по адресу под блоком тарифы")
    def test_send_application_from_address(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            tariff_page = TariffsSection(page=page)
            tariff_page.click_on_button_find_tariffs()
            popup_page = OpenPopUpAddress(page=page)
            popup_page.check_popup_window()
            popup_page.choose_in_flat()
            popup_page.search_address()
            search_page = SearchFromMain(page=page)
            search_page.close_quiz()
            tariff_page = TariffPage(page=page)
            tariff_page.check_tag_home_internet()
            time.sleep(3)
            tariff_page.fill_the_application()
            main_page = MainPage(page=page)
            time.sleep(2)
            main_page.check_success_popups()
            main_page.close_popup_wait_for_call()

    @allure.title("Заявка через компонент поиска по адресу в блоке провайдеров (попап, адрес-тариф-подключить)")
    def test_send_application_from_prov_block(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            blockprov_page = BlockProviders(page=page)
            blockprov_page.check_providers_block()
            blockprov_page.click_search_sat()
            popup_page = OpenPopUpAddress(page=page)
            popup_page.check_popup_window()
            popup_page.choose_in_business()
            popup_page.choose_in_sat()
            popup_page.choose_in_flat()
            tariff_block = TariffsSection(page=page)
            time.sleep(7)
            popup_page.fill_the_application_with_address()
            main_page = MainPage(page=page)
            time.sleep(2)
            search_page = SearchFromMain(page=page)
            search_page.quiz_send_appl()
            main_page = MainPage(page=page)
            main_page.check_success_popups()
            main_page.close_popup_wait_for_call()
            tariff_page = TariffPage(page=page)
            tariff_page.check_tag_home_internet()
            tariff_page.fill_the_application()

    @allure.title(
        "Проверить заявку через компонент поиска по адресу (адрес-тариф подключить, фильтрация по провайдеру, скорости и цене)")
    def test_send_application_address_with_filter(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
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
            tariff_page.click_on_tariff_with_500()
            main_page = MainPage(page=page)
            time.sleep(2)
            tariff_page.send_popup_wait_for_call()
            main_page.check_success_popups()
            main_page.close_popup_wait_for_call()

    @allure.title("Просмотр всех отзывов по региону")
    def test_check_all_reviews_in_region(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            review_block_page = ReviewBlockPage(page=page)
            review_block_page.check_review_block()
            review_block_page.click_button_more_reviews()
            expected_url = "https://piter-online.net/reviews"
            page.wait_for_url(expected_url)
            with allure.step("Проверить, что URL соответствует ожидаемому"):
                current_url = page.url
                assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"
                time.sleep(4)

    @allure.title("Написать отзыв")
    def test_write_review(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            review_block_page = ReviewBlockPage(page=page)
            review_block_page.check_review_block()
            review_block_page.click_button_more_reviews()
            expected_url = "https://piter-online.net/reviews"
            page.wait_for_url(expected_url)
            with allure.step("Проверить, что URL соответствует ожидаемому"):
                current_url = page.url
                assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"
                time.sleep(4)
            review_feedback = ReviewPageFeedback(page=page)
            review_feedback.click_on_write_review_button()
            review_feedback.leave_feedback()
            review_feedback.go_back()
            time.sleep(5)
            expected_second = "https://piter-online.net/reviews"
            page.wait_for_url(expected_url)
            with allure.step("Проверить, что URL соответствует ожидаемому"):
                current_url = page.url
                assert current_url == expected_second, f"Ожидался URL {expected_url}, но получен {current_url}"