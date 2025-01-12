import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element(By.CSS_SELECTOR,"input[name='q']").send_keys("phone")
driver.find_element(By.CSS_SELECTOR,"input[name='q']").submit();
time.sleep(3)
print("1   " + driver.title)
driver.find_element(By.XPATH,"(//div[@class='KzDlHZ'])[1]").click()
time.sleep(3)
list=driver.window_handles
driver.switch_to.window(list[1])
print("2    " + driver.title)
driver.switch_to.window(list[0])
print("3    " + driver.title)
time.sleep(5)
driver.close()