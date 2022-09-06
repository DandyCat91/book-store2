import time
from selenium import webdriver
# Registration_login: регистрация аккаунта
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
email=driver.find_element_by_id("reg_email")
email.send_keys("111@mail.ru")
password=driver.find_element_by_id("reg_password")
password.send_keys("Meow243521!")
driver.find_element_by_css_selector("[value='Register']").click()
time.sleep(3)
driver.quit()
# Registration_login: логин в систему
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
logout = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/customer-logout/']")
logout_check = logout.text
if logout_check == "Logout":
    print("Logout is available")
else:
    print("Logout is not available")
driver.quit()

