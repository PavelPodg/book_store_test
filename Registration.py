from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

email = 'copexaw762@krunsea.com' 
password = 'N1E0s20QPK'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)

#Registration_login: регистрация аккаунта
driver.get("http://practice.automationtesting.in/")
myAcc = driver.find_element_by_id('menu-item-50').click()

regEmail = driver.find_element_by_id('reg_email').send_keys(email)
regPassword = driver.find_element_by_id('reg_password').send_keys(password)
register = driver.find_element_by_name('register').click()
print('test_1 finished successfull')
driver.quit()


#Registration_login: логин в систему

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)

menuMyAccount = driver.find_element_by_id('menu-item-50')
menuMyAccount.click()

fieldUserName = driver.find_element_by_id('username')
fieldUserName.send_keys(email)

fieldPassword = driver.find_element_by_id('password')
fieldPassword.send_keys(password)

buttonLogin = driver.find_element_by_css_selector('[value=Login]')
buttonLogin.click()

logOutChek = driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a').text
assert logOutChek == 'Logout'
print('test_2 finished successfull')
driver.quit()