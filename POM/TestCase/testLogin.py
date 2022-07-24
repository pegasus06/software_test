#用例层
from time import time, sleep

from ddt import ddt,unpack,data
import unittest
from PageObject.loginPage import LoginPage
from selenium import webdriver
@ddt
class TestLoginPage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.log=LoginPage(self.driver)
    def tearDown(self) -> None:
        sleep(3)
        self.driver.quit()

    @data(*LoginPage(None).openFile(LoginPage.date))
    @unpack
    def test01_login(self,user,pwd):
        self.log.login(user,pwd)
if __name__ == '__main__':
    unittest.main()