from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.implicitly_wait(10)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)


driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")

readMoreButton = driver.find_element_by_xpath('//*[@id="text-22-sub_row_1-0-2-0-0"]/div/ul/li/a[2]').click()
driver.execute_script("window.scrollBy(0, 600);")
reviewsWindow = driver.find_element_by_xpath('//*[@id="product-160"]/div[3]/ul/li[2]').click()
scores = driver.find_element_by_class_name('star-5').click()
comment = driver.find_element_by_id('comment').send_keys('Nice Book!')
name = driver.find_element_by_id('author').send_keys('User')
email = driver.find_element_by_id('email').send_keys('Example@gmail.com')
submit = driver.find_element_by_id('submit').click()
print('test  finished successfull')
driver.quit()