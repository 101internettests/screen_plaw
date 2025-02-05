import time

import allure
import uuid
from playwright.sync_api import Page, expect, sync_playwright
from pages.urls_stage_msk import urls, names
from pages.pol_main_page import MainPage, SelectRegionPage, SearchFromMain, TariffsSection, ReviewCatPopup
from pages.orders_office_page import OfficePage
from pages.sat_page import SatPage
from config import pol_url


class TestPolMainWithRegion:
    @allure.title("Выбрать регион из хедера")
    def test_choose_region_from_header(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
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
            browser = playwright.chromium.launch(headless=False)
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
            browser = playwright.chromium.launch(headless=False)
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
            browser = playwright.chromium.launch(headless=False)
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
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.check_cat_ai()
            main_page.use_cat_ai_help()

    @allure.title("Проверить заявку через компонент поиска по адресу (квиз)")
    def test_send_application_quiz(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
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

    @allure.title("Проверить вкладку Для бизнеса")
    def test_check_for_business_page(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
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
            browser = playwright.chromium.launch(headless=False)
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

    @allure.title("Посмотреть детали тарифа")
    def test_check_tariff_details(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
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
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(full_url)
            review_page = ReviewCatPopup(page=page)
            review_page.open_popup_cat_website()
            review_page.leave_feedback_cat()

    @allure.title("Кнопка подняться наверх работает")
    def test_catupper_button(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.check_cat_upper()
            main_page.make_screenshot()