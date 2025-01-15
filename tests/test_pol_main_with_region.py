import allure
import uuid
from playwright.sync_api import Page, expect, sync_playwright
from pages.urls_stage_msk import urls, names
from pages.pol_main_page import MainPage, SelectRegionPage


class TestPolMainWithRegion:
    @allure.title("Выбрать регион из хедера")
    def test_choose_region_from_header(self):
        page.goto('https://101internet.ru/select-region')
        main_page = MainPage(page=page)
        main_page.open_select_region_window()
