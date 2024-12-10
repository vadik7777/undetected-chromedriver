import undetected_chromedriver as uc
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

print("start of script")

options = uc.ChromeOptions()
# options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--ignore-certificate-errors")

driver = uc.Chrome(options)
driver.maximize_window()

driver.get("https://lenta.ru")
driver.save_screenshot('lenta.png')

driver.get("https://www.e1.ru")
driver.save_screenshot('e1.png')
driver.close()

print("end of script")
