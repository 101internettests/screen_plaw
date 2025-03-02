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
            search_page.choode_admir_area()

            time.sleep(3)
            # main_page.open_select_region_window()
            # select_page = SelectRegionPage(page=page)
            # select_page.check_select_region_page()
            # time.sleep(5)
            # select_page.choose_leningrad_region()
            # main_page.check_header_city()
            # main_page.check_main_page_has_leningrad_region()