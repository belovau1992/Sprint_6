import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Кликнуть на логотип Самокат")
    def click_on_logo_Scooter(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип Яндекс")
    def click_on_logo_Yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.get_current_url()