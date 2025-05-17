import allure

from url import dzen_page
from url import main_site
from pages.main_page import MainPage


class TestLogoRedirect:
    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_Yandex()
        assert driver.current_url == dzen_page

    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат"')
    def test_logo_redirect_to_scooter_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_Scooter()
        assert driver.current_url == main_site