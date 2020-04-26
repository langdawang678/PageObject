import unittest
from page.sina import *
from selenium import webdriver

class SinaTest(unittest.TestCase, Sina):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn')

    def tearDown(self):
        self.driver.quit()

    def test_sinaLogin_01(self):
        self.login('', '')
        self.assertEqual(self.getLoginError, '请输入邮箱名')

    def test_sinaLogin_02(self):
        self.login('wuya1303', 'asd888')
        self.assertEqual(self.getLoginError, '您输入的邮箱名格式不正确')

if __name__ == '__main__':
    unittest.main(verbosity=2)
