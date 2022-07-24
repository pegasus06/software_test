# 封装元素操作和业务流程
from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.pageMethod import PageMethod


class LoginPage(PageMethod):
    date = r"F:\PythonStudy\automation_test\POM\Date\userAccount"
    url = r"http://cms.duoceshi.cn/cms/manage/login.do"
    username = (By.ID, "userAccount")
    passwd = (By.ID, "loginPwd")
    button = (By.ID, "loginBtn")
    webdriver.Chrome()

    def login(self, user, pwd):
        self.visit(self.url)
        self.sendKeys(self.username, user)
        self.sendKeys(self.passwd, pwd)
        self.click(self.button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    LoginPage(driver).login("admin", 123456)
