from selenium import webdriver
import time


class Login:
    def __init__(self):
            browser = webdriver.Chrome(
            executable_path=r"C:/Users/29726.ITCINFOTECH/Desktop/Advantage/Python/PycharmProjects/Google_test_Shukla/Drivers/chromedriver.exe")
            browser.maximize_window()
            browser.get("http://www.gmail.com")