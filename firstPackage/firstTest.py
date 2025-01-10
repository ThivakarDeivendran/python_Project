from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium 3 Code
# driver=webdriver.Chrome("D://Drivers//chromedriver-win64//chromedriver-win64//chromedriver.exe")
# driver.get("https://www.saucedemo.com")
# webApplicationTitle =driver.title
# if(webApplicationTitle == "Swag Labs"):
#     print("Application title verified successfully")
# else:
#     print("Application title verified failed")
# driver.find_element_by_css_selector("#user-name").send_keys("Thivakar")
# driver.find_element_by_css_selector("#password").send_keys("Testing")
# driver.find_element_by_id("login-button").click()
# error_Message =driver.find_element_by_tag_name("h3")
# if(error_Message.is_displayed()):
#     print("Error Message visible")
# else:
#     print("Error Message Not Visible")
# driver.close()

#Selenium 4 Code
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")
webApplicationTitle =driver.title
if(webApplicationTitle == "Swag Labs"):
    print("Application title verified successfully")
else:
    print("Application title verified failed")
driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("Thivakar")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("Testing")
driver.find_element(By.ID,"login-button").click()
error_Message =driver.find_element(By.TAG_NAME,"h3")
if(error_Message.is_displayed()):
    print("Error Message visible")
else:
    print("Error Message Not Visible")
driver.close()
