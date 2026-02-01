from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import Waits
from utils.generator import UserDataGenerator
from utils.test_user import TestUser
from utils.constants import Constants
from locators import MainPage, SignInPage, RegistrationPage, PersonalPage


class TestRegistration:
    
    # Тестирование регистрации с валидными и невалидными данными
    def test_registration_valid_user(self, driver):
        
        email = UserDataGenerator.random_email()
        password = UserDataGenerator.random_password()
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*SignInPage.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.REGISTER_HEADER))
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPage.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(PersonalPage.PLACE_AD_BUTTON)
        )
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(PersonalPage.PROFILE_AVATAR_BUTTON)
        )
        assert (
            WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME)
            .until(
                EC.visibility_of_element_located(PersonalPage.PROFILE_NAME))
            .text
            == Constants.USER_PROFILE_NAME
        )


    # Тестирование регистрации с невалидным email
    def test_registration_invalid_email(self, driver):
        
        email = UserDataGenerator.invalid_email()
        password = UserDataGenerator.random_password()

        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*SignInPage.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(
                RegistrationPage.REGISTER_HEADER
            )
        )
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPage.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.REGISTRATION_ERROR_LABEL)
            ).text == Constants.ERROR_LABEL

        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.INPURT_ERROR_EMAIL)
        )
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.INPUT_ERROR_PASSWORD)
        )
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.INPUT_ERROR_SUBMIT_PASSWORD)
        )

    # Тестирование регистрации с уже существующим пользователем
    def test_registration_existing_user(self, driver):

        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        driver.find_element(*SignInPage.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(
                RegistrationPage.REGISTER_HEADER
            )
        )
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(TestUser.EMAIL)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(TestUser.PASSWORD)
        driver.find_element(*RegistrationPage.SUBMIT_PASSWORD_INPUT).send_keys(TestUser.PASSWORD)
        driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
        
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.REGISTRATION_ERROR_LABEL)
            ).text == Constants.ERROR_LABEL
        
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.INPURT_ERROR_EMAIL)
        )
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.INPUT_ERROR_PASSWORD)
        )
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RegistrationPage.INPUT_ERROR_SUBMIT_PASSWORD)  
        )
        