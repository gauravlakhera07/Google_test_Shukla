from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from test_methods.test_login import Login

class Gmail(Login):
    def test_gmail_login(self,browser):
        g.brfind_element_by_id('identifierId').send_keys("shamatapatra2216@gmail.com")


        #super.self.test_chrome()
        # browser = webdriver.Chrome(executable_path=r"C:/Users/29726.ITCINFOTECH/Desktop/Advantage/Python/PycharmProjects/Google_test_Shukla/Drivers/chromedriver.exe")
        # browser.get('http://gmail.com')

        # action = webdriver.ActionChains(Login.test_chrome.browser)
        # email_elem = Login.test_chrome.browser.find_element_by_id('identifierId')
        # email_elem.send_keys("shamatapatra2216@gmail.com")
        # nextButton = Login.test_chrome.browser.find_element_by_xpath("//*[@id='identifierNext']/div/button/span")
        # nextButton.click()
        # time.sleep(2)
        # passwordElem = Login.test_chrome.browser.find_element_by_id('Passwd')
        # passwordElem.send_keys('y3qy8pem')
        # signinButton = Login.test_chrome.browser.find_element_by_id('signIn')
        # signinButton.click()
        # time.sleep(3)
        # Login.test_chrome.browser.quit()

g = Gmail()
p=g.__init__()


