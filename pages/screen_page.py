import allure
from locators.screen_locators import ScreenLocators
from playwright.sync_api import expect, Request, Page
from pages.base_page import BasePage


class ScreenPage(BasePage):
    def open_read_more_buttons(self):
        max_total_clicks = 20  # защита от бесконечного цикла
        clicks = 0
        while clicks < max_total_clicks:
            read_more_buttons = self.page.locator(ScreenLocators.READ_MORE_BUTTON)
            count = read_more_buttons.count()

            if count == 0:
                if clicks == 0:
                    print("Нет кнопок 'Читать далее' для клика.")
                break

            try:
                read_more_buttons.nth(0).click(timeout=2000)  # кликаем по первой доступной
                clicks += 1
                print(f"Нажата кнопка 'Читать далее' #{clicks}.")
                # Ждем рендеринг контента не дольше 4 секунд
                self.page.wait_for_timeout(4000)
            except Exception as e:
                print(f"Ошибка при клике на кнопку 'Читать далее': {e}")
                break

    def open_read_full_buttons(self):
        max_total_clicks = 20  # защита от бесконечного цикла
        clicks = 0
        while clicks < max_total_clicks:
            read_full_buttons = self.page.locator(ScreenLocators.READ_FULL_BUTTON)
            count = read_full_buttons.count()

            if count == 0:
                if clicks == 0:
                    print("Нет кнопок 'Читать полностью' для клика.")
                break

            try:
                read_full_buttons.nth(0).click(timeout=2000)  # кликаем по первой доступной
                clicks += 1
                print(f"Нажата кнопка 'Читать полностью' #{clicks}.")
                # Ждем раскрытие/рендеринг не дольше 4 секунд
                self.page.wait_for_timeout(4000)
            except Exception as e:
                print(f"Ошибка при клике на кнопку 'Читать полностью': {e}")
                break

    def click_all_faq_buttons(self):
        buttons = self.page.locator(ScreenLocators.FAQ_OPEN).all()

        # Нажимаем на каждую кнопку
        for button in buttons:
            button.click()