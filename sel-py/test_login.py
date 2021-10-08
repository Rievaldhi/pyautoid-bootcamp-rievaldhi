import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class TestRegister():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver.exe')
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_pageTitle(self,setup):
        self.driver.get("https://www.demoqa.com/login")
        assert self.driver.title == 'ToolsQA'

    def test_loginBetul(self,setup):
        self.driver.get("https://www.demoqa.com/login")
        self.driver.find_element_by_id('userName').send_keys('bunga')
        self.driver.find_element_by_id('password').send_keys('As12345678**')
        self.driver.find_element_by_id('login').click()
        usernameNya = self.driver.find_element_by_id('userName-value').text
        assert usernameNya == 'bunga'

    def test_loginSalah(self,setup):
        self.driver.get("https://www.demoqa.com/login")
        self.driver.find_element_by_id('userName').send_keys('bunga')
        self.driver.find_element_by_id('password').send_keys('salah**')
        self.driver.find_element_by_id('login').click()
        infoSalah = self.driver.find_element_by_id('name').text
        assert infoSalah == 'Invalid username or password!'


        

