import allure
import pytest

import data
from pages.important_questions_page import ImportantQuestions

class TestAnswers:
    @allure.title("Тест ответов на вопросы")
    @pytest.mark.parametrize('question_number, expected_text', data.Data.question_names)
    def test_question_names(self,driver,question_number,expected_text):
        # Arrange
        important_questions = ImportantQuestions(driver)
        important_questions.wait_for_question_list()
        # Act
        important_questions.click_on_question(question_number)
        # Assert
        assert important_questions.check_question_name(expected_text, question_number)