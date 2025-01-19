import allure
import uuid
from playwright.sync_api import Page, expect, sync_playwright
from pages.urls_stage_msk import urls, names
from pages.pol_main_page import MainPage, SelectRegionPage
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
            select_page.choose_sertolovo()
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
    def test_chech_catbanner_ai(self):
        full_url = f"{pol_url}"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(full_url)
            main_page = MainPage(page=page)
            main_page.check_cat_ai()
            main_page.use_cat_ai_help()

