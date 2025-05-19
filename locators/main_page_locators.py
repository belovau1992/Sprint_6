from selenium.webdriver.common.by import By


class MainPageLocators:
    UP_BUTTON_ORDER = (By.CLASS_NAME, "Button_Button__ra12g")
    DOWN_BUTTON_ORDER = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    LOGO_SCOOTER = (By.XPATH, "//div[@class = 'Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, "//div[@class = 'Header_LogoYandex__3TSOI']")

    @staticmethod
    def question_number(question):
        return By.XPATH, f'//div[contains(@class, "accordion__item") and .//div[contains(text(), "{question}")]'
