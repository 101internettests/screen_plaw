import time
import allure
import re
from locators.mol_locators import ReviewPage
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class ReviewPageFeedback(BasePage):
    # @allure.title("Проверить хлебные крошки")
    # def check_breadcrumbs(self):
    #     expect(self.page.locator(OrdersSatPage.BREADCRUMBS_INTERNET_FOR_SAT)).to_be_visible()
    #     expect(self.page.locator(OrdersSatPage.BREADCRUMBS_CONNECT_INTERNET)).to_be_visible()
    #
    @allure.title("Кликнуть на кнопку написать отзыв")
    def click_on_write_review_button(self):
        self.page.locator(ReviewPage.BUTTON_WRITE_REVIEW).click()

    @allure.title("Заполнить отзыв")
    def leave_feedback(self):
        with allure.step("Выбрать в квартире"):
            self.page.locator(ReviewPage.CHOSE_IN_FLAT).click()
        with allure.step("Выбрать Ростелеком"):
            self.page.locator(ReviewPage.INPUT_PROVIDER).fill("Рост")
            self.page.locator(ReviewPage.CHOOSE_ROSTEL).click()
        with allure.step("Оставить оценки"):
            self.page.locator(ReviewPage.FOUR_INTERNET).click()
            self.page.locator(ReviewPage.FOUR_TV).click()
            self.page.locator(ReviewPage.FOUR_MONTAZ).click()
        with allure.step("Оставить отзыв"):
            self.page.locator(ReviewPage.REVIEW_TEXTAREA).fill("Пользуюсь Ростелекомом: интернет в целом стабильный, но иногда случаются перебои. Поддержка старается помочь, но не всегда быстро.")
        with allure.step("Выбрать срок 3 мес - 1 год"):
            self.page.locator(ReviewPage.THREE_MONTH_YEAR).click()
        with allure.step("Вставить имя"):
            self.page.locator(ReviewPage.NAME_INPUT).fill("ГостьТ")
        with allure.step("Отправить отзыв"):
            self.page.locator(ReviewPage.SEND_REVIEW_BUTTON).click()
        with allure.step("Проверить, что отзыв отправился"):
            expect(self.page.locator(ReviewPage.CHECK_THANKFORREVIEW)).to_be_visible()


