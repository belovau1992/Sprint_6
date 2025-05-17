import allure

from pages.order_form_page import OrderForm
from data import CredentialsOne


class TestSuccessfulOrderWindow:
    @allure.title("Тест успешного оформления заказа")
    def test_successful_order(self,driver):
        # Arrange
        order_form_page = OrderForm(driver)
        credentials = CredentialsOne()
        # Act
        order_form_page.click_on_button_order_up()
        order_form_page.fill_order_form(
            credentials.name,
            credentials.last_name,
            credentials.address,
            credentials.metro,
            credentials.telephone
        )
        order_form_page.click_on_cook()
        order_form_page.click_on_next()
        order_form_page.fill_rent_form(credentials.date,credentials.komment)
        order_form_page.click_on_order_button_in_order()
        # Assert
        assert order_form_page.check_displaying_of_successful_order_window()
