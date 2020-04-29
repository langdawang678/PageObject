# coding:utf-8
import unittest
from selenium import webdriver
from utils.operationXml import *
class Init(unittest.TestCase,OpeartionXml):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.getXmlData('url'))

    def tearDown(self):
        self.driver.quit()