import time
from abc import ABC
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions




class TestBaseClass(ABC):
    wait: WebDriverWait
    driver: WebDriver

    def setup(self):
        c = webdriver.ChromeOptions()
        c.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path="E:\IT\chromedriver.exe", options=c)
        self.driver.implicitly_wait(1)
        self.driver.set_window_size(1500, 1200)
        self.wait = WebDriverWait(self.driver, 10)
        return self.driver

    def tear_down(self,driver):
        self.driver.close()





