from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url = "https://clubetudiants.ma/post/cours/-EMI-Exemples-des-anciens-concours"
# url = "https://clubetudiants.ma/exemple-des-anciens-concours/ecoles"
email = "email_here"
psw = "pasword_here"
driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(url)


element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jconfirm-scrollpane"))
    )
btn = driver.find_element_by_class_name('btn-default').click()
print(driver.title)
driver.find_element_by_class_name('ce-login').click()
driver.implicitly_wait(1)
alert = driver.switch_to.window("xtf")

# alert.find_element_by_xpath('//input[@name="email"]').send_keys(email)
driver.find_elements_by_class_name('form-control')[0].send_keys(email)
driver.find_elements_by_class_name('form-control')[1].send_keys(psw)
driver.find_element_by_class_name('ce-btn-submit').click()
driver.implicitly_wait(3)
driver.switch_to.window('')
time.sleep(1)
p = driver.find_elements_by_xpath('//p/a')
for t in p:
    print()
    t.click()
    driver.find_element_by_class_name('down').click()
    driver.back()


driver.close()
# jconfirm-scrollpane
