import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

REGULAR_APP_EXERCISE = "a[class='button'][ data-action ='bugfree']"
ZADANIE_1 = "//h2[text()='Zadanie 1']"
OKULARY = ":first-child input[type='number'] "
ZAD_1 = "a[href='/task_1']"
ADD_BUTTON = "button[id='add-product-60a93cf5bf479']"

class First:







    def set_up(self, driver):
        c = webdriver.ChromeOptions()
        c.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path="E:\IT\chromedriver.exe", options=c)
        self.driver.implicitly_wait(1)
        self.driver.set_window_size(1500, 1200)
        return self.driver


    def go_to_exercises(self, driver):
        self.driver.get('http://asta.pgs-soft.com/')
        self.driver.find_element_by_css_selector(REGULAR_APP_EXERCISE).click()
        time.sleep(3)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        return self.driver


    def task_1(self, driver):
        self.driver.find_element_by_css_selector(ZAD_1).click()
        time.sleep(2)
        return self.driver


    def task_1_add_product(self, driver):
        self.driver.find_element_by_css_selector(OKULARY).clear()
        self.driver.find_element_by_css_selector(OKULARY).send_keys(3)
        self.driver.find_element_by_css_selector(ADD_BUTTON)
        return self.driver

obj = First()
obj.set_up(driver=webdriver)
obj.go_to_exercises(driver=webdriver)
obj.task_1(driver=webdriver)
obj.task_1_add_product(driver=webdriver)

