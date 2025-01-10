import base64
import io
import os
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys("Thivakar")
driver.find_element(By.ID,"password").send_keys("Testing")

try:
    ScreenShot_Folder = "ScreenShot"
    if not os.path.exists(ScreenShot_Folder):
        os.makedirs(ScreenShot_Folder)
        driver.save_screenshot(os.path.join(ScreenShot_Folder,f"test_{time.strftime("%Y%m%d_%H%M%S")}.png"))
finally:
    print("ScreenShot added Successfull")
time.sleep(5)
driver.close()
# try:
#     driver.save_screenshot(os.path.join("ScreenShot","ownTest.png"))
# finally:
#     print("Testing successfully")
