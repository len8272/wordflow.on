# import os
# from pages.base import WebPage
# # from pages.elements import WebElement
#
#
# class MainPage(WebPage):
#
#     def __init__(self, web_driver, url=''):
#         if not url:
#             url = os.getenv("MAIN_URL") or https://wordflow.online/signin'
#
#         super().__init__(web_driver, url)
#
#     """Авторизация"""

    # login_field = WebElement(xpath='//*[@class="full-input__input formvalidate-error"]')
    # enter = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    # automatic_closing = WebElement(xpath='//*[@id="auth-success-login"]/input[2]')
    # auth_error = WebElement(xpath='//a[contains(text(),"Введенного кода не существует")]')
    # auth_error_2 = WebElement(xpath='//span[contains(text(),"Нельзя использовать символ «{N}»")]')