from selenium.webdriver.common.by import By

class Locators:
    #Локаторы для регистрации
    REG_NAME = (By.XPATH, "//fieldset[1]//input[@name='name']") # поле ввода имени для регистрации
    REG_EMAIL = (By.XPATH, "//fieldset[2]//input[@name='name']") # поле ввода email для регистрации
    REG_PASSWORD = (By.XPATH, "//fieldset[3]//input[@name='Пароль']") # поле ввода пароля для регистрации
    BUT_REG_END = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # кнопка завершения регистрации
    TEXT_INVALID_PASSWORD = (By.XPATH, "//fieldset[3]//p[@class='input__error text_type_main-default']") # текст ошибки ввода пароля при регистрации
    #Локаторы для входа
    BUT_LOGIN_IN_ACCOUNT = (By.XPATH, "//section[2]//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # кнопка войти в аккаунт
    BUT_PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']") # кнопка личный кабинет
    BUT_REGISTRATION = (By.XPATH, "//p[1]//a[@class='Auth_link__1fOlj']") # кнопка регистрации на странице входа
    BUT_RECOVERY_PASSWORD = (By.XPATH, "//p[2]//a[@class='Auth_link__1fOlj']") # кнопка восстановления пароля на странице входа
    BUT_LOGIN = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # кнопка войти на странице входа
    LOG_EMAIL = (By.XPATH, "//input[@name='name']") # поле ввода пароля на странице входа
    LOG_PASSWORD = (By.XPATH, "//input[@name='Пароль']") # поле ввода email на странице входа
    BUT_ORDER_PLACE = (By.XPATH, "//section[2]//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # кнопка оформить заказ
    BUT_LOGIN_WHEN_REGISTRATED = (By.XPATH, "//a[@href='/login']") # кнопка войти на странице регистрации
    BUT_LOGIN_RECOVERY_PASSWORD = (By.XPATH, "//a[@href='/login']") # кнопка войти на странице восстановления пароля
    #Локаторы для перехода в личный кабинет
    TEXT_PERSONAL_DATA = (By.XPATH, "//p[.='В этом разделе вы можете изменить свои персональные данные']") # текст на странице личного кабинета
    INVISIBLE_ELEMENT = (By.XPATH, "//img[@alt='loading animation']") # перекрывающий элемент
    #Локаторы StellarBurger
    BUT_STELLAR_BURGERS = (By.XPATH, "//a[@href='/']") # кнопка stellar burgers
    BUT_CONSTRUCTOR = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2']") # кнопка конструктор
    #Локаторы для выхода из аккаунта
    BUT_EXIT = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']") # кнопка выхода из аккаунта
    TEXT_LOGIN = (By.XPATH, "//h2[.='Вход']")
    #Локаторы для переходов к разделам
    BUT_CHAPTER_ROLLS = (By.XPATH, "//div[.='Булки']") # кнопка булки
    BUT_CHAPTER_SAUCES = (By.XPATH, "//div[.='Соусы']") # кнопка соусы
    BUT_CHAPTER_FILLINGS = (By.XPATH, "//div[.='Начинки']") # кнопка начинки
