import os
import time
import allure
from playwright.sync_api import sync_playwright
from pages.pol_main_page import MainPage, SelectRegionPage, SearchFromMain
from pages.orders_tohome_page import TohomePage
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