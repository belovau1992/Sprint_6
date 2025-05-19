from selenium.webdriver.common.by import By


class OrderFormLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.CLASS_NAME, "select-search__select")
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    ORDER_WINDOW = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")

class AboutRentLocators:
    WHEN_TO_BRING = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-arrow")
    RENTAL_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    TWO_DAYS_RENT = (By.XPATH, "//div[@class = 'Dropdown-option' and text() = 'двое суток']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    KOMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_IN_ORDER = (By.XPATH, "//button[contains(@class, 'Order_Buttons') and text()='Заказать']")
    BUTTON_YES = (By.XPATH, "//button[contains(text(),'Да')]")