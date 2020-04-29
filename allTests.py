# coding:utf-8
import unittest
import os
import HTMLTestRunner
import time


def allTests():
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__), "testcase"),
        pattern="tets_*py",
        top_level_dir=None
    )
    return suite


def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_S", time.localtime(time.time()))


def run():
    fileName = os.path.join(os.path.dirname(__file__), "report", getNowTime() + "sinaRreport.html")
    fp = open(fileName, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='UI自动化测试报告', description='UI自动化测试报告')
    runner.run(allTests())


if __name__ == '__main__':
    run()
