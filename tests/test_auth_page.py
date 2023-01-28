# from pages.locators import MainPage

# Для запуска тестов этойго файла ввести в терминал:
# pytest -v --driver Chrome --driver-path \projects\chromedriver2.exe tests\test_auth_page.py


import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def page(driver):
    driver.get("https://wordflow.online/signup")
    yield driver.current_url
    driver.quit()


def test_signup_on_site_positive(driver, page):
    assert "https://wordflow.online/signup" in driver.current_url

    email_field = driver.find_element_by_xpath("//input[@name='email']")
    email_field.send_keys("test@test.com")

    password_field = driver.find_element_by_xpath("//input[@name='password']")
    password_field.send_keys("test123")

    confirm_password_field = driver.find_element_by_xpath("//input[@name='confirm']")
    confirm_password_field.send_keys("test123")

    terms_checkbox = driver.find_element_by_xpath("//div[@class='checkbox']//input")
    terms_checkbox.click()

    button_signup = driver.find_element_by_xpath("//button[@type='submit']")
    button_signup.click()

    greeting = driver.find_element_by_xpath("//h2[@class='greeting']").text
    assert greeting == "Welcome to WordFlow! Let's get started."


def test_signup_on_site_negative(driver, page):
    assert "https://wordflow.online/signup" in driver.current_url

    email_field = driver.find_element_by_xpath("//input[@name='email']")
    email_field.send_keys("test@test.com")

    password_field = driver.find_element_by_xpath("//input[@name='password']")
    password_field.send_keys("test")

    confirm_password_field = driver.find_element_by_xpath("//input[@name='confirm']")
    confirm_password_field.send_keys("test")

    button_signup = driver.find_element_by_xpath("//button[@type='submit']")
    button_signup.click()

    error_message = driver.find_element_by_xpath("//div[@class='Error']").text
    assert error_message == "Passwords must be at least 8 characters long"

"""Тестируем возможность входа  в личный кабинет с корректным и некорректным логином (код скидки). 4 теста."""

"""Вход с корретными данными"""
#
# def test_valid_login_auth_page(web_browser):
#     page = MainPage(web_browser)
#     page.my_labirint.click()
#     page.login_field.send_keys("1208-41C9-80DB")
#     page.enter.click()
#     page.automatic_closing.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/'
#
# """Вход с некорретными данными"""
#
#
# def test_invalid_login_auth_page(web_browser):
#     page = MainPage(web_browser)
#     page.my_labirint.click()
#     page.login_field.send_keys("12F8-41C9-80DB")
#     page.enter.click()
#
#     assert page.auth_error
#
#
# """Вход с пробелом"""
#
#
# def test_blanc_login_auth_page(web_browser):
#     page = MainPage(web_browser)
#     page.my_labirint.click()
#     page.login_field.send_keys("      ")
#
#     assert page.auth_error_2
#
# """Вход по электронной почте"""
#
# def test_email_login_auth_page(web_browser):
#     page = MainPage(web_browser)
#     page.my_labirint.click()
#     page.login_field.send_keys("len8272@gmail.com")
#     page.enter.click()
#
#     assert page.login_field
