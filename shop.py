from tkinter.tix import Select
from selenium import webdriver
import time
from soupsieve import select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#############################################################Shop: 1) отображение страницы товара
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")

menuMyAccount = driver.find_element_by_id('menu-item-50')
menuMyAccount.click()

fieldUserName = driver.find_element_by_id('username')
fieldUserName.send_keys('jahav56970@tsclip.com')

fieldPassword = driver.find_element_by_id('password')
fieldPassword.send_keys('0s9SESHNbc')

buttonLogin = driver.find_element_by_css_selector('[value=Login]')
buttonLogin.click()

menuShop = driver.find_element_by_xpath('//*[@id="menu-item-40"]/a')
menuShop.click()

driver.execute_script("window.scrollBy(0, 200);")
nameOfBook = driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a[1]/h3')
nameOfBook.click()


elementNameOfBook = driver.find_element_by_xpath('//*[@id="product-181"]/div[2]/h1') 
element_get_text = elementNameOfBook.text # получили текст элемента с помощью .text
assert element_get_text == "HTML5 Forms" 
print('test_1 finished successfull')
driver.quit()



#############################################################Shop: 2) количество товаров в категории

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")

menuMyAccount = driver.find_element_by_id('menu-item-50')
menuMyAccount.click()

fieldUserName = driver.find_element_by_id('username')
fieldUserName.send_keys('jahav56970@tsclip.com')

fieldPassword = driver.find_element_by_id('password')
fieldPassword.send_keys('0s9SESHNbc')

buttonLogin = driver.find_element_by_css_selector('[value=Login]')
buttonLogin.click()

menuShop = driver.find_element_by_id('menu-item-40')
menuShop.click()

linkHTML = driver.find_element_by_css_selector('.cat-item.cat-item-19 >a')
linkHTML.click()

amount_of_goods = driver.find_elements_by_tag_name('h3')
# print(type(amount_of_goods))
amount_of_goods_int = len(amount_of_goods)
if amount_of_goods_int == 3: 
    print('Количество товаров равно трем')
else: 
    print('Количество товаров не совпадает с 3')

print('test_2 finished successfull')    
driver.quit()



#############################################################Shop: 3) Shop: сортировка товаров

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")

menuMyAccount = driver.find_element_by_id('menu-item-50')
menuMyAccount.click()

fieldUserName = driver.find_element_by_id('username')
fieldUserName.send_keys('jahav56970@tsclip.com')

fieldPassword = driver.find_element_by_id('password')
fieldPassword.send_keys('0s9SESHNbc')

buttonLogin = driver.find_element_by_css_selector('[value=Login]')
buttonLogin.click()

menuShop = driver.find_element_by_id('menu-item-40')
menuShop.click()

#sort = Select(driver.find_element_by_class_name('orderby')).selecet_by_value('menu_order').get_attribute('selected')
sort = driver.find_element_by_class_name('orderby')
select = Select(sort)
select.select_by_value("menu_order")
sortMenu = sort.get_attribute("value")
print(sortMenu)
if sortMenu == 'menu_order':
    print('Выбрана сортировка по умолчанию')
else: 
    print('Выбрана другая сортировка')

select = Select(sort)
select.select_by_value("price-desc") 
HighToLow = driver.find_element_by_class_name('orderby')
HighToLowCheck = HighToLow.get_attribute("value")
#print(HighToLowCheck)
if HighToLowCheck == 'price-desc':
    print('Выбрана сортировка от большей к меншьей')
else:
    print('Ошибка сортировки')

print('test_3 finished successfull')   
driver.quit()



# jahav56970@tsclip.com - email
# 0s9SESHNbc - password
#############################################################Shop: 4) Shop: отображение, скидка товара

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.implicitly_wait(10)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)

driver.get("http://practice.automationtesting.in/")

menuMyAccount = driver.find_element_by_id('menu-item-50')
menuMyAccount.click()

fieldUserName = driver.find_element_by_id('username')
fieldUserName.send_keys('jahav56970@tsclip.com')

fieldPassword = driver.find_element_by_id('password')
fieldPassword.send_keys('0s9SESHNbc')

buttonLogin = driver.find_element_by_css_selector('[value=Login]')
buttonLogin.click()

menuShop = driver.find_element_by_id('menu-item-40')
menuShop.click()

androidQuickStartBook = driver.find_element_by_css_selector('.post-169 h3')
androidQuickStartBook.click()

newPriceItem = driver.find_element_by_css_selector('.price :nth-child(2)')
newPriceItemText = newPriceItem.text
oldPriceItem = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/del/span')
oldPriceItemText = oldPriceItem.text

assert newPriceItemText == "₹450.00"
assert oldPriceItemText == "₹600.00"

book_cover = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,".images")))
driver.execute_script("return arguments[0].scrollIntoView(true);", book_cover)
book_cover.click()

book_cover_close = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close")))
book_cover_close.click()
print('test_4 finished successfull')
driver.quit()


#############################################################Shop: 5) проверка цены в корзине

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")

menuShop = driver.find_element_by_css_selector("[id=menu-item-40] > a")
menuShop.click()



chooseBook = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[1]/h3')
driver.execute_script("return arguments[0].scrollIntoView(true);", chooseBook)
chooseBook.click()

addToBasket = driver.find_element_by_tag_name('button')
addToBasket.click()

basketItem = driver.find_element_by_css_selector('[class=wpmenucart-contents] :nth-child(2)')
basketItemText = basketItem.text
print(basketItemText)
basketPrice = driver.find_element_by_css_selector('[class=wpmenucart-contents] :nth-child(3)')
basketPriceText = basketPrice.text
print(basketPriceText)

assert basketItemText == '1 Item'
assert basketPriceText == '₹180.00'

goToBasketMenu = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a')
goToBasketMenu.click()

priceSubTotalCheking = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title=Subtotal] :nth-child(1)"), "180.00"))

prieceTotalCehking = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.TAG_NAME, "strong"), "189.00"))
print('Test_5 fineshed successfully')
driver.quit()


#############################################################Shop: 6) работа в корзине

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")

menuShop = driver.find_element_by_css_selector("[id=menu-item-40] > a")
menuShop.click()

driver.execute_script("window.scrollBy(0, 300);")
 
time.sleep(3)
BokWeb = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
time.sleep(3)
bookJs = driver.find_element_by_xpath('//*[@id="content"]/ul/li[5]/a[2]').click()
 
time.sleep(3)

basketMenu = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/i').click()
time.sleep(3)
removeBook = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a').click()

undo = driver.find_element_by_link_text('Undo?').click()
clearItem = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
clearItem.clear()
clearItem.send_keys('3')
update_cart = driver.find_element_by_name('update_cart').click()
checkElement = clearItem.get_attribute('value')
assert checkElement == '3'
time.sleep(3)
applyCoupon = driver.find_element_by_name('apply_coupon').click()
checkAnnotation = driver.find_element_by_class_name("woocommerce-error").text
assert checkAnnotation == 'Please enter a coupon code.'
print(checkAnnotation,checkElement)
print('test_6 finished successfull')
driver.quit()

#############################################################Shop: 7) покупка товара

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")

menuShop = driver.find_element_by_css_selector("[id=menu-item-40] > a")
menuShop.click()



chooseBook = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[1]/h3')
driver.execute_script("return arguments[0].scrollIntoView(true);", chooseBook)
chooseBook.click()

time.sleep(3)
addToBaskets = driver.find_element_by_tag_name('button').click()
time.sleep(2)

goToBasketMenu =  WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[1]/a'))).click()
#вот так вот используем явное ожидание с нажатием кнопки

proceed_to_Checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page-34"]/div/div[1]/div/div/div/a'))).click()
fieldFirstName = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="billing_first_name"]'))).send_keys("Firstusername")
fieldLastName = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="billing_last_name"]'))).send_keys("Lastusername")
driver.execute_script("window.scrollBy(0, 100);") 
fieldTelefon = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="billing_phone"]'))).send_keys("123445678")
fieldEmail = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="billing_email"]'))).send_keys("example@gmail.com")
driver.execute_script("window.scrollBy(0, 400);") 

filedZip = driver.find_element_by_xpath('//*[@id="billing_postcode"]')
filedZipText = filedZip.send_keys('125480')
fieldAdress = driver.find_element(By.ID, "billing_address_1").send_keys('Ul. Lenina 24')
fieldCity = driver.find_element(By.ID,"billing_city").send_keys('Enywherecity')


selectCountry = driver.find_element_by_xpath('//*[@id="s2id_billing_country"]/a').click()
selectCountryField = driver.find_element_by_xpath('//*[@id="s2id_autogen1_search"]').send_keys('rus')
selectCountryItem = driver.find_element_by_xpath('//*[@id="select2-results-1"]/li[3]').click() 

fieldCounty = driver.find_element_by_css_selector('[name=billing_state]').send_keys('Moscow')

time.sleep(3)
#fieldCountySearch = driver.find_element_by_xpath('//*[@id="s2id_autogen251_search"]').send_keys('Ac')
#fieldCountyItem =  driver.find_element_by_xpath('//*[@id="select2-result-label-252"]').click()
#selectCountryItem = driver.find_element_by_css_selector('[id=select2-result-label-997]').click()

goToPlaceOrder = driver.find_element_by_xpath('//*[@id="place_order"]')
driver.execute_script("return arguments[0].scrollIntoView(true);", goToPlaceOrder) # автоматически проскроллили до зоны видимости кнопки
goToPlaceOrder.click()
#driver.execute_script("return arguments[0].scrollIntoView(true);", goToPlaceOrder) # автоматически проскроллили до зоны видимости кнопки


check_thank_you = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
print('test_7 finished successfull')
driver.quit()
