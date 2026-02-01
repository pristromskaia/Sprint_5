from selenium.webdriver.common.by import By

class MainPage:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Вход и регистрация')]")
    PLACE_AD_BUTTON_UNAUTH = (By.XPATH, "//button[contains(.,'Разместить объявление')]")

class PersonalPage:
    PROFILE_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    PROFILE_AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(.,'Выйти')]")
    PLACE_AD_BUTTON = (By.XPATH, "//button[contains(.,'Разместить объявление')]")
    ADVT_CARD = (By.CSS_SELECTOR, "div[class*='card']")
    
class RegistrationPage:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    NAME_INPUT = (By.NAME, "name")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Создать аккаунт')]")
    REGISTER_HEADER = (By.XPATH, "//h1[contains(., 'Зарегистрироваться')]")
    REGISTRATION_ERROR_LABEL = (By.XPATH, "//span[contains(@class, 'input_span') and text() = 'Ошибка']")
    INPURT_ERROR_EMAIL = (By.CSS_SELECTOR, "div[class*=input_inputError] input[name='email']")
    INPUT_ERROR_PASSWORD = (By.CSS_SELECTOR, "div[class*=input_inputError] input[name='password']")
    INPUT_ERROR_SUBMIT_PASSWORD = (By.CSS_SELECTOR, "div[class*=input_inputError] input[name='submitPassword']")

class SignInPage:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(.,'Нет аккаунта')]")

class AdvtCreationPage:
    REGISTRATION_WARNING_HEADER = (By.XPATH, "//h1[text() = 'Чтобы разместить объявление, авторизуйтесь']")
    NEW_ADVT_HEADER = (By.XPATH, "//h1[contains(., 'Новое объявление')]")  
    ADVT_NAME = (By.NAME, "name")
    ADVT_DESCRIPTION = (By.CSS_SELECTOR, "textarea[name='description']")
    ADVT_PRICE = (By.NAME, "price")
    ADVT_CATEGORY = (By.CSS_SELECTOR, "div[class*='dropDownMenu_input'] input[name='category'] + button")
    ADVT_CATEGORY_OPTION_AUTO = (By.XPATH, "//button[.//span[normalize-space()='Авто']]")
    ADVT_CITY = (By.CSS_SELECTOR, "div[class*='dropDownMenu_input'] input[name='city'] + button")
    ADVT_CITY_OPTION_MOSCOW = (By.XPATH, "//button[.//span[normalize-space()='Москва']]")
    ADVT_CONDITION_USED = (By.XPATH, "//label[normalize-space()='Б/У']")
    ADVT_PUBLISH_BUTTON = (By.XPATH, "//button[contains(.,'Опубликовать')]")