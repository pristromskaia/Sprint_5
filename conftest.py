import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import Waits
from utils.base_url import BaseUrl
from utils.test_user import TestUser
from selenium.webdriver.common.by import By
from locators import MainPage, SignInPage, PersonalPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(BaseUrl.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_user(driver):

    # Вход на сайт под тестовым пользователем
    driver.find_element(*MainPage.LOGIN_BUTTON).click()
    driver.find_element(*SignInPage.EMAIL_INPUT).send_keys(TestUser.EMAIL)
    driver.find_element(*SignInPage.PASSWORD_INPUT).send_keys(TestUser.PASSWORD)
    driver.find_element(*SignInPage.LOGIN_BUTTON).click()

    # Проверка, что пользователь вошёл успешно
    WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
        EC.visibility_of_element_located(PersonalPage.PROFILE_AVATAR_BUTTON)
    )
    return driver
