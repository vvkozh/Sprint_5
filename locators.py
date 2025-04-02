from selenium.webdriver.common.by import By

class Locators:
    #Локаторы для регистрации
    REG_NAME = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") # поле ввода имени для регистрации
    REG_EMAIL = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") # поле ввода email для регистрации
    REG_PASSWORD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input") # поле ввода пароля для регистрации
    BUT_REG_END = (By.XPATH, "//*[@id='root']/div/main/div/form/button") # кнопка завершения регистрации
    TEXT_INVALID_PASSWORD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p") # текст ошибки ввода пароля при регистрации
    #Локаторы для входа
    BUT_LOGIN_IN_ACCOUNT = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") # кнопка войти в аккаунт
    BUT_PERSONAL_ACCOUNT = (By.XPATH, "//*[@id='root']/div/header/nav/a") # кнопка личный кабинет
    BUT_REGISTRATION = (By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a") # кнопка регистрации на странице входа
    BUT_RECOVERY_PASSWORD = (By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a") # кнопка восстановления пароля на странице входа
    BUT_LOGIN = (By.XPATH, "//*[@id='root']/div/main/div/form/button") # кнопка войти на странице входа
    LOG_EMAIL = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") # поле ввода пароля на странице входа
    LOG_PASSWORD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") # поле ввода email на странице входа
    BUT_ORDER_PLACE = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") # кнопка оформить заказ
    BUT_LOGIN_WHEN_REGISTRATED = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a") # кнопка войти на странице регистрации
    BUT_LOGIN_RECOVERY_PASSWORD = (By.XPATH, "//*[@id='root']/div/main/div/div/p/a") # кнопка войти на странице восстановления пароля
    #Локаторы для перехода в личный кабинет
    TEXT_PERSONAL_DATA = (By.XPATH, "//*[@id='root']/div/main/div/nav/p") # текст на странице личного кабинета
    #Локаторы StellarBurger
    BUT_STELLAR_BURGERS = (By.XPATH, "//*[@id='root']/div/header/nav/div/a") # кнопка stellar burgers
    BUT_CONSTRUCTOR = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p") # кнопка конструктор
    #Локаторы для выхода из аккаунта
    BUT_EXIT = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button") # кнопка выхода из аккаунта
    #Локаторы для переходов к разделам
    BUT_CHAPTER_ROLLS = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]") # кнопка булки
    BUT_CHAPTER_SAUCES = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]") # кнопка соусы
    BUT_CHAPTER_FILLINGS = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]") # кнопка начинки
