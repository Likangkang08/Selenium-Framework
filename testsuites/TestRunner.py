#_*_ coding:utf-8 _*_

import unittest
from MyHTMLTestReportCNs.HTMLTestReportCN import HTMLTestRunner
import os
import time

# 定义输出的文件位置和名字
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

HtmlFile = report_path+now+"HTMLTestReportCN.html"

fp = open(HtmlFile, "wb")


if __name__=='__main__':
    suite = unittest.TestLoader().discover("testsuites")

    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'执行情况',tester=u'QA')
    runner.run(suite)
    fp.close()
