from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import Waits
from locators import PersonalPage, MainPage


class TestLogout:
    
    # Тестирование выхода из аккаунта
    def test_login_valid_user(self, login_user):

        driver = login_user
        driver.find_element(*PersonalPage.LOGOUT_BUTTON).click()
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(MainPage.LOGIN_BUTTON)
        )
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.invisibility_of_element_located(PersonalPage.PROFILE_AVATAR_BUTTON)
        )
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.invisibility_of_element_located(PersonalPage.PROFILE_NAME)
        )
