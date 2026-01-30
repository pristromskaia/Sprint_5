from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import Waits
from locators import PersonalPage
from utils.constants import Constants


class TestLogin:
    
    # Тестирование входа с валидными данными
    def test_login_valid_user(self, login_user):

        driver = login_user

        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(PersonalPage.PROFILE_AVATAR_BUTTON)
        )
        assert (
            WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME)
            .until(
                EC.visibility_of_element_located(
                    PersonalPage.PROFILE_NAME)
            )
            .text
            == Constants.USER_PROFILE_NAME
        )
