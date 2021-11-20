# coding = utf-8
import unittest
import HTMLTestRunner
import os
import time
from BeautifulReport import BeautifulReport

report_path = os.path.dirname(os.path.abspath('.')) + '/result/'
now = time.strftime("%Y-%m-%d %H_%M_%S ", time.localtime(time.time()))
HtmlFile = report_path + now + "HTMLtemplate.html"

fp = open(HtmlFile, "wb")
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite = unittest.TestLoader().discover("testsuites")
#
#
#     runner = unittest.TextTestRunner()
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"后台项目测试报告", description=u"用例测试情况")
#     runner.run(suite)
#     fp.close()
# 一次性加载一个包或者文件夹下所有的测试用例
# suite = unittest.TestLoader().discover("testsuites")
# 一次性加载一个类文件下所有测试用例到suite中去
#suite = unittest.TestSuite(unittest.makeSuite(TestSchool))
# 加载测试函数
# suite.addTest(TestSchool("test_school_01"))

#用BeautifulReport生成报告
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().discover("testsuites")


    runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"后台项目测试报告", description=u"用例测试情况")
    runner = BeautifulReport(suite)
    runner.report(description='Beautiful Report', filename=now+'report.html', log_path=report_path)
    fp.close()



