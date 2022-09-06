import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
# Shop: отображение страницы товара
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
email2=driver.find_element_by_id("username")
email2.send_keys("111@mail.ru")
password2=driver.find_element_by_id("password")
password2.send_keys("Meow243521!")
time.sleep(3)
driver.find_element_by_css_selector("[value='Login']").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()
header = driver.find_element_by_css_selector("[itemprop='name']")
header_check=header.text
assert header_check== "HTML5 Forms"
driver.quit()
# Shop: количество товаров в категории
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
email2=driver.find_element_by_id("username")
email2.send_keys("111@mail.ru")
password2=driver.find_element_by_id("password")
password2.send_keys("Meow243521!")
time.sleep(3)
driver.find_element_by_css_selector("[value='Login']").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product-category/html/']").click()
number=driver.find_element_by_css_selector(".cat-item.cat-item-19.current-cat>span")
number_check=number.text
books = driver.find_elements_by_css_selector(".products.masonry-done>li")
if len(books) == 3:
    print("3 товара")
else:
    print("Ошибка. Количество товаров в корзине: " + str(len(books)))
driver.quit()
# Shop: сортировка товаров
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
email2=driver.find_element_by_id("username")
email2.send_keys("111@mail.ru")
password2=driver.find_element_by_id("password")
password2.send_keys("Meow243521!")
time.sleep(3)
driver.find_element_by_css_selector("[value='Login']").click()
driver.find_element_by_id("menu-item-40").click()
select=driver.find_element_by_css_selector("[value='menu_order']")
select_check = select.get_attribute("selected")
if select_check is not None:
    print("Сортировка по умолчанию")
else:
    print("Атрибута нет")
sorting = driver.find_element_by_css_selector(".orderby")
select = Select(sorting)
select.select_by_value("price")
select2=driver.find_element_by_css_selector("[value='price']")
select2_check=select2.get_attribute("selected")
if select2_check is not None:
    print("Сортировка по убыванию цены")
else:
    print("Атрибута нет")
driver.quit()
# Shop: отображение, скидка товара
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
email2=driver.find_element_by_id("username")
email2.send_keys("111@mail.ru")
password2=driver.find_element_by_id("password")
password2.send_keys("Meow243521!")
time.sleep(3)
driver.find_element_by_css_selector("[value='Login']").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector(".post-169 h3").click()
old_price=driver.find_element_by_css_selector(".price > del > span")
old_price_text=old_price.text
new_price=driver.find_element_by_css_selector(".price > ins > span")
new_price_text=new_price.text
assert old_price_text == "₹600.00"
assert new_price_text == "₹450.00"
picture=WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")) )
picture.click()
picture_close=WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
picture_close.click()
driver.quit()
# Shop: проверка цены в корзине
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
email2=driver.find_element_by_id("username")
email2.send_keys("111@mail.ru")
password2=driver.find_element_by_id("password")
password2.send_keys("Meow243521!")
time.sleep(2)
driver.find_element_by_css_selector("[value='Login']").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(3)
cart_number=driver.find_element_by_css_selector(".cartcontents")
cart_number_text=cart_number.text
cart_price=driver.find_element_by_css_selector("#wpmenucartli > a > :nth-child(3)")
cart_price_text=cart_price.text
assert cart_number_text == "1 Item"
assert cart_price_text == "₹180.00"
driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
subtotal= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']>:nth-child(1)"), "₹" + "180.00"))
total= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-subtotal>:nth-child(1)"), "₹" + "180.00"))
driver.quit()
# Shop: работа в корзине
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(5)
driver.find_element_by_css_selector("[data-product_id='180']").click()
time.sleep(3)
driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
time.sleep(3)
driver.find_element_by_css_selector("[data-product_id='180']").click()
driver.find_element_by_css_selector(".woocommerce-message a").click()
locator=driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
locator.clear()
locator.send_keys("3")
driver.find_element_by_css_selector("[value='Update Basket']").click()
locator=driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
locator_number=locator.get_attribute("value")
assert locator_number == ("3")
time.sleep(3)
driver.find_element_by_css_selector("[value='Apply Coupon']").click()
error=driver.find_element_by_css_selector(".woocommerce-error")
error_text=error.text
assert error_text == "Please enter a coupon code."
driver.quit()
# Shop: покупка товара
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(3)
driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
proceed=WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/checkout/']")) )
proceed.click()
name=WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")) )
name.send_keys("Kate")
last_name=driver.find_element_by_id("billing_last_name")
last_name.send_keys("Ivanova")
email=driver.find_element_by_id("billing_email")
email.send_keys("111@mail.ru")
phone=driver.find_element_by_id("billing_phone")
phone.send_keys("77777777777")
driver.find_element_by_css_selector(".select2-choice").click()
country=driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Russia")
driver.find_element_by_id("select2-result-label-394").click()
address=driver.find_element_by_id("billing_address_1")
address.send_keys("Novaya")
city=driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
state=driver.find_element_by_id("billing_state")
state.send_keys("Russia")
zip=driver.find_element_by_id("billing_postcode")
zip.send_keys("123456")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
some_element2= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments"))
driver.quit()
