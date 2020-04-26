# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class WebDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def findElement(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def findsElement(self, *loc):
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            print("Error Details {0}".format(e.args[0]))

    @property
    def test(self):
        print("test")