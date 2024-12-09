import undetected_chromedriver as uc
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

print("start of script")

options = uc.ChromeOptions()
driver = uc.Chrome(options)
driver.maximize_window()

driver.get("https://ria.ru")
driver.save_screenshot('ria.png')

print("end of script")

while True: time.sleep(10)
