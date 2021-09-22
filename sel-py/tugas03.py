from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver.exe')

driver.get('https://demoqa.com/alerts')

driver.find_element_by_id('timerAlertButton').click()
try:
    WDW(driver , 10).until(EC.alert_is_present())
    print('Nah alert nya muncul')
    driver.switch_to.alert.accept()


except TimeoutException:
    print('ndak muncul ')
    pass

driver.close()