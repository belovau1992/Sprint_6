import allure
from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.order_form_locators import OrderFormLocators, AboutRentLocators


class OrderForm(BasePage):
    @allure.step("Кликнуть на верхнюю кнопку Заказать")
    def click_on_button_order_up(self):
        self.click_on_element(MainPageLocators.UP_BUTTON_ORDER)

    @allure.step("Кликнуть на нижнюю кнопку Заказать")
    def click_on_button_order_down(self):
        self.click_on_element(MainPageLocators.DOWN_BUTTON_ORDER)

    @allure.step("Выбрать станцию метро")
    def select_metro_station(self):
        self.click_on_element(OrderFormLocators.METRO_STATION)


    @allure.step("Заполнить форму заказа")
    def fill_order_form(self,name,last_name,address,metro,telephone):
        self.send_keys_to_input(OrderFormLocators.NAME, name)
        self.send_keys_to_input(OrderFormLocators.LAST_NAME, last_name)
        self.send_keys_to_input(OrderFormLocators.ADDRESS, address)
        self.send_keys_to_input(OrderFormLocators.METRO, metro)
        self.select_metro_station()
        self.send_keys_to_input(OrderFormLocators.TELEPHONE, telephone)

    @allure.step("Закрыть окно с куками")
    def click_on_cook(self):
        self.click_on_element(OrderFormLocators.COOKIE_BUTTON)

    @allure.step("Кликнуть кнопку Далее")
    def click_on_next(self):
        self.click_on_element(OrderFormLocators.BUTTON_NEXT)

    @allure.step("Заполнить форму аренды")
    def fill_rent_form(self,date,komment):
        self.send_keys_to_input(AboutRentLocators.WHEN_TO_BRING,date)
        self.press_enter()
        self.send_keys_to_input(AboutRentLocators.KOMMENT,komment)
        self.click_on_element(AboutRentLocators.RENTAL_PERIOD)
        self.click_on_element(AboutRentLocators.TWO_DAYS_RENT)
        self.click_on_element(AboutRentLocators.COLOR_BLACK)
        self.click_on_element(AboutRentLocators.ORDER_BUTTON_IN_ORDER)

    @allure.step("Получить текст всплывающего сообщения")
    def get_successful_order_popup_text(self):
        return self.get_text_on_element(OrderFormLocators.ORDER_WINDOW).text

    @allure.step('Проверить отображение окна успешного создания заказа')
    def check_displaying_of_successful_order_window(self):
        return self.check_displaying_of_element(OrderFormLocators.ORDER_WINDOW)

    @allure.step("Клик на кнопку заказать в самой форме заполнения заказа")
    def click_on_order_button_in_order(self):
        self.click_on_element(AboutRentLocators.ORDER_BUTTON_IN_ORDER)