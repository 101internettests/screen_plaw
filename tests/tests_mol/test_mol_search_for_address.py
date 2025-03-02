import os
import time
import allure
from playwright.sync_api import sync_playwright
from pages.mol_main_page import MainPage, SelectRegionPage, SearchFromMain
from pages.orders_tohome_page import TohomePage
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