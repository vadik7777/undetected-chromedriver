# Generated by Selenium IDE
import pytest
import time
import json
import undetected_chromedriver as webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestpy():
  def setup_method(self, method):
    self.options = webdriver.ChromeOptions()
    self.options.add_argument("--disable-setuid-sandbox")
    self.options.add_argument("--ignore-certificate-errors")
    self.options.add_argument("--ignore-certificate-errors")
    self.driver = webdriver.Chrome(self.options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testpy(self):
    self.driver.get("https://nowsecure.nl/")
    self.driver.set_window_size(1039, 692)
    assert self.driver.title == "NowSecure.nl"
  
