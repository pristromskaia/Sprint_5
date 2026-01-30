import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import Waits
from utils.constants import Constants
from utils.dropdowns import select_random_from_dropdown
from locators import MainPage, AdvtCreationPage, PersonalPage


class TestCreateAdvt:
    
    # Создание объявления неавторизованным пользователем
    def test_create_advt_unauthorized_user(self, driver):
        driver.find_element(*MainPage.PLACE_AD_BUTTON_UNAUTH).click()
        
        assert WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(
                AdvtCreationPage.REGISTRATION_WARNING_HEADER)
            ).text == Constants.ADVT_WARNING

    # Создание объявления авторизованным пользователем
    def test_create_advt_authorized_user(self, login_user):
        driver = login_user
        
        driver.find_element(*PersonalPage.PLACE_AD_BUTTON).click()
        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(AdvtCreationPage.NEW_ADVT_HEADER)
        )
        driver.find_element(*AdvtCreationPage.ADVT_NAME).send_keys(Constants.ADVT_TITLE)
        driver.find_element(*AdvtCreationPage.ADVT_DESCRIPTION).send_keys(Constants.ADVT_DESCRIPTION)
        driver.find_element(*AdvtCreationPage.ADVT_PRICE).send_keys(Constants.ADVT_PRICE)
        
        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(AdvtCreationPage.ADVT_CATEGORY)
        ).click()

        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(AdvtCreationPage.ADVT_CATEGORY_OPTION_AUTO)
        ).click()

        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(AdvtCreationPage.ADVT_CITY)
        ).click()

        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(AdvtCreationPage.ADVT_CITY_OPTION_MOSCOW)
        ).click()

        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(AdvtCreationPage.ADVT_CONDITION_USED)
        ).click()
        
        driver.find_element(*AdvtCreationPage.ADVT_PUBLISH_BUTTON).click()

        WebDriverWait(driver, Waits.DEFAULT_WAIT_TIME).until(
                EC.visibility_of_element_located(PersonalPage.PROFILE_NAME)
            )
    
        assert WebDriverWait( 
            driver, Waits.DEFAULT_WAIT_TIME).until( 
            EC.visibility_of_element_located((PersonalPage.ADVT_CARD)) 
            )
        