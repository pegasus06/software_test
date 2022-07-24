'''
存放公共方法
@author:zhourui
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PageMethod():
    def __init__(self, driver):
        self.driver = driver

    def find(self, args):  # 传入元组
        return self.driver.find_element(*args)  # 解包

    def visit(self, url):
        return self.driver.get(url)

    def sendKeys(self, args, text):
        return self.find(args).send_keys(text)

    def click(self, args):
        return self.find(args).click()

    def switch_alert(self, flag=None, text=None):
        alert = self.driver.switch_to.alert
        if flag == "accept":
            alert.accept()
        elif flag == "dismiss":
            alert.dismiss()
        else:
            alert.send_keys(text)

    def mouse_over(self, args):
        mouse = self.find(args)
        ActionChains(self.driver).move_to_element(mouse)

    def openFile(self, datePath):
        list1 = []
        with open(datePath, "r", encoding="utf-8")as f:
            file = f.readlines()
            for i in file:
                list1.append(i.strip('\n').split('_'))
        return list1


if __name__ == '__main__':
    test = PageMethod(webdriver.Chrome())
    # locate = (By.ID, "kw")
    # locate1 = (By.ID, "su")
    test.visit("http://www.baidu.com")
    # sleep(1)
    # test.mouse_over(locate1)
    # test.click(locate1)
    # test.sendKeys(locate, "张三")
    # test.click(locate1)
    # test.sendKeys((By.ID,"su"),"今天")
    # print(test.openFile(r'F:\PythonStudy\automation_test\POM\Date\userAccount'))
