import unittest
from page.init import *
from page.sina import *
from selenium import webdriver
from utils.operationXml import *


class SinaTest(Init, Sina):
    # def test_sinaLogin_01(self, parent='divText', value='emailNull'):
    #     self.login('', '')
    #     self.assertEqual(self.getLoginError, self.getXmlUser(parent, value))

    def test_sinaLogin_02(self, parent='divText', value='emailFormat'):
        self.login('abc', 'asd888')
        self.assertEqual(self.getLoginError, self.getXmlUser(parent, value))


if __name__ == '__main__':
    unittest.main(verbosity=2)
