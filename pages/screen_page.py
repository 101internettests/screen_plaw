import allure
from locators.screen_locators import ScreenLocators
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class ScreenPage(BasePage):
    def open_read_more_buttons(self):
        while True:
            read_more_buttons = self.page.locator(ScreenLocators.READ_MORE_BUTTON)
            count = read_more_buttons.count()

            if count == 0:
                print("Нет кнопок 'Читать далее' для клика.")
                break

            for i in range(count):
                try:
                    # Click the button
                    read_more_buttons.nth(0).click()  # Always click the first button
                    print(f"Нажата кнопка 'Читать далее' #{i + 1}.")
                    self.page.wait_for_timeout(1000)  # Give time for new content to load
                    break  # Exit the loop after the click
                except Exception as e:
                    print(f"Ошибка при клике на кнопку 'Читать далее': {e}")

            # Wait for additional content to fully load (if necessary)
            self.page.wait_for_timeout(1000)  # Wait for the content to render

    def open_read_full_buttons(self):
        while True:
            read_more_buttons = self.page.locator(ScreenLocators.READ_FULL_BUTTON)
            count = read_more_buttons.count()

            if count == 0:
                print("Нет кнопок 'Читать далее' для полностью.")
                break

            for i in range(count):
                try:
                    # Click the button
                    read_more_buttons.nth(0).click()  # Always click the first button
                    print(f"Нажата кнопка 'Читать далее' #{i + 1}.")
                    self.page.wait_for_timeout(1000)  # Give time for new content to load
                    break  # Exit the loop after the click
                except Exception as e:
                    print(f"Ошибка при клике на кнопку 'Читать полностью': {e}")

            # Wait for additional content to fully load (if necessary)
            self.page.wait_for_timeout(1000)  # Wait for the content to render

    def click_all_faq_buttons(self):
        buttons = self.page.locator(ScreenLocators.FAQ_OPEN).all()

        # Нажимаем на каждую кнопку
        for button in buttons:
            button.click()