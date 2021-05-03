import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import string


class syneostest(unittest.TestCase):
    def test_syneos(self):
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\karthik_ettaveni\PycharmProjects\pythonProject1\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://google.com/")
    if __name__ == "__main__":
        unittest.main()