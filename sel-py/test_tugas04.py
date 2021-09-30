import pytest
from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

def test_isiForm():
    driver.get('https://demoqa.com/text-box')
    judul = driver.title
    print(judul)
    assert judul == 'ToolsQA'

    driver.find_element_by_id('userName').send_keys('bunga nih')
    driver.find_element_by_id('userEmail').send_keys('bunga-nih@mail.com')
    driver.find_element_by_id('currentAddress').send_keys('Jakartaa')
    driver.find_element_by_id('permanentAddress').send_keys('Rumah desa')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_id('submit').click()
    
    nama = driver.find_element_by_id('name').text
    assert nama == 'Name:bunga nih'

    email = driver.find_element_by_id('email').text
    assert email == 'Email:bunga-nih@mail.com'

    # if "Jakartaa" in  driver.find_element_by_id('currentAddress').text:
    #     print("Alamat sekarang terdeteksi")

    # if "Rumah desa" in  driver.find_element_by_id('permanentAddress').text:
    #     print("Alamat permanen terdeteksi")


    driver.close()

