import unittest
# from common.aaHTMLTestRunner import HTMLTestRunner
from common.HTMLTestRunner_cn import HTMLTestRunner
import os
from common.sendEmail import SendEmail
import time


file = os.path.realpath(__file__)  # 当前文件真实目录
root = os.path.dirname(file)  # 根目录
casePath = os.path.join(root, "case")  # 用例所在目录
reportPath = os.path.join(root, "report", "result.html")  # 报告所在目录


while 1 == 1:
    # if time.strftime("%Y-%m-%d %X") == '2019-08-09 08:11:30':
    if 1 == 1:
        discover = unittest.defaultTestLoader.discover(casePath, pattern="test*.py")
        with open(reportPath, "wb") as fp:
            runner = HTMLTestRunner(
                stream=fp,
                title="团队行程pc端接口测试报告",
                description="团队行程pc端接口测试"
                # retry=2
            )
            runner.run(discover)

        # 发送邮件
        # SendEmail(reportPath).sendFJ()
        break





