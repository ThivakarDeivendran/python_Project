import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
if(driver.title == "Register"):
    print("Application Title verified successfully")
else:
    print("Application Title verified failed")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='First Name']").send_keys("Thivakar")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Last Name']").send_keys("Testing")
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("test@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[value='Male']").click()
# Locate the dropdown element
# dropdown_element = driver.find_element(By.CSS_SELECTOR,"#Skills")
# select = Select(dropdown_element)
#
# select.select_by_visible_text("Java")
# # select.select_by_value("optionValue")
# # select.select_by_index(1)

dropdown_element = driver.find_elements(By.CSS_SELECTOR,"#Skills option")
for option in dropdown_element:
    if option.text == "Android":
        option.click()
time.sleep(10)
driver.close()
