from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://demoqa.com/webtables')

# manual flow to input into the form

# driver.find_element_by_id('addNewRecordButton').click()
# judulForm = driver.find_element_by_id('registration-form-modal')
# print('Pindah ke modal')
# driver.find_element_by_id('firstName').send_keys('mawar')
# driver.find_element_by_id('lastName').send_keys('merah')
# driver.find_element_by_id('userEmail').send_keys('mawar1@mail.com')
# driver.find_element_by_id('age').send_keys('21')
# driver.find_element_by_id('salary').send_keys('100')
# driver.find_element_by_id('department').send_keys('FE')
# driver.find_element_by_id('submit').click()

# driver.find_element_by_id('addNewRecordButton').click()
# judulForm = driver.find_element_by_id('registration-form-modal')
# print('Pindah ke modal')
# driver.find_element_by_id('firstName').send_keys('melati')
# driver.find_element_by_id('lastName').send_keys('putit')
# driver.find_element_by_id('userEmail').send_keys('melati1@mail.com')
# driver.find_element_by_id('age').send_keys('22')
# driver.find_element_by_id('salary').send_keys('200')
# driver.find_element_by_id('department').send_keys('BE')
# driver.find_element_by_id('submit').click()

# driver.find_element_by_id('addNewRecordButton').click()
# judulForm = driver.find_element_by_id('registration-form-modal')
# print('Pindah ke modal')
# driver.find_element_by_id('firstName').send_keys('bunga')
# driver.find_element_by_id('lastName').send_keys('kamboja')
# driver.find_element_by_id('userEmail').send_keys('bunga1@mail.com')
# driver.find_element_by_id('age').send_keys('23')
# driver.find_element_by_id('salary').send_keys('300')
# driver.find_element_by_id('department').send_keys('Fullstack')
# driver.find_element_by_id('submit').click()


# set list in each field
namaAwal = ['mawar' , 'melati' , 'bunga']
namaAkhir = ['merah' , 'putih' , 'kamboja']
emailNya = ['mawar1@mail.com' , 'melati1@mail.com' , 'bunga1@mail.com']
umurNya = ['21' , '22' , '23']
gajiNya = ['100' , '200' , '300']
deptNya = ['FE' , 'BE' , 'Fullstack']

# loop using while
i = 0
while i <= 2:
    driver.find_element_by_id('addNewRecordButton').click()
    judulForm = driver.find_element_by_id('registration-form-modal')
    print('Pindah ke modal ' , i+1 ,' kali')
    driver.find_element_by_id('firstName').send_keys(namaAwal[i])
    driver.find_element_by_id('lastName').send_keys(namaAkhir[i])
    driver.find_element_by_id('userEmail').send_keys(emailNya[i])
    driver.find_element_by_id('age').send_keys(umurNya[i])
    driver.find_element_by_id('salary').send_keys(gajiNya[i])
    driver.find_element_by_id('department').send_keys(deptNya[i])
    driver.find_element_by_id('submit').click()
    i = i+1

time.sleep(7)
driver.close()
