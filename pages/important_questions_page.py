import allure

from locators.important_questions_locators import ImportantQuestionLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class ImportantQuestions(BasePage):
    @allure.step("Подождать загрузки списка вопросов")
    def wait_for_question_list(self):
        self.scroll_to_element(ImportantQuestionLocators.QUESIONS)
        self.wait_for_element(ImportantQuestionLocators.QUESIONS)

    @allure.step("Открыть вопрос")
    def click_on_question(self, question_number):
        question_locator = ImportantQuestionLocators.question(question_number)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Сравни ответ")
    def check_question_name(self, expected_text, question_number):
        locator = ImportantQuestionLocators.answer(question_number)
        actual_text = self.get_text_on_element(locator)
        return actual_text == expected_text