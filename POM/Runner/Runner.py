import unittest
from Utils import HTMLTestRunner3_New
import time
import datetime
class RunCms():
    def run(self,reportPath,casePath):
        fileName=reportPath+"\\"+datetime.datetime.now().strftime("%A")+"report.html"
        with open(fileName,"wb")as f:
            discover=unittest.TestLoader().discover(casePath,"test*")
            runner=HTMLTestRunner3_New.HTMLTestRunner\
                (stream=f,description="测试情况如下",title="CMS平台自动化测试"\
                 ,tester="zhourui")
            runner.run(discover)
if __name__ == '__main__':
    RunCms().run(r"F:\PythonStudy\automation_test\POM\Report",r"F:\PythonStudy\automation_test\POM\TestCase")