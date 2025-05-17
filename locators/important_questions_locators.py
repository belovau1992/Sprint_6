from selenium.webdriver.common.by import By


class ImportantQuestionLocators:
    QUESIONS = (By.CLASS_NAME, "accordion")

    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")

    ANSWER_1 = (By.ID, "accordion__panel-0")
    ANSWER_2 = (By.ID, "accordion__panel-1")
    ANSWER_3 = (By.ID, "accordion__panel-2")
    ANSWER_4 = (By.ID, "accordion__panel-3")
    ANSWER_5 = (By.ID, "accordion__panel-4")
    ANSWER_6 = (By.ID, "accordion__panel-5")
    ANSWER_7 = (By.ID, "accordion__panel-6")
    ANSWER_8 = (By.ID, "accordion__panel-7")

    ANSWERS = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not (@hidden)]")

    @staticmethod
    def question(number):
        # локатор для вопроса
        return (By.XPATH, f'//div[@id="accordion__heading-{number - 1}"]/parent::div')

    @staticmethod
    def answer(number):
        # локатор для ответа
        return (By.XPATH, f'//div[@id="accordion__panel-{number - 1}"]')