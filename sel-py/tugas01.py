from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:/chromedriver_win32/chromedriver.exe')

web = [ 'https://noobtest.id', 
        'https://erzaf.com', 
        'https://orangsiber.com', 
        'https://demoqa.com', 
        'https://automatetheboringstuff.com'
    ]

namaWeb = [
            'noobtest.id --> ',
            'erzaf.com --> ',
            'orangsiber.com --> ',
            'demoqa.com --> ',
            'automatetheboringstuff.com --> '
        ]

for openWeb, output in zip(web, namaWeb):

    driver.minimize_window()
    driver.get(openWeb)
    judulWeb = driver.title
    print(output, judulWeb)

driver.close()

