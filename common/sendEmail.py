import zmail
import os
import time

class SendEmail:

    cwd = os.getcwd()  # 当前文件所在文件夹地址
    root = os.path.dirname(cwd)  # 父级目录
    reportP = os.path.join(root, "report", "result.html")  # 报告所在目录


    def __init__(self, reportPath=reportP):
        self.reportPath = reportPath  # 报告所在目录

    def sendText(self):
        '''
        发送纯文本的邮件
        :return:
        '''
        server = zmail.server('420889656@qq.com', 'glaejvtpoqclbgbg')
        mail = {
            'subject': '测试邮件标题-文本!'+time.strftime("%Y-%m-%d %X"),
            'content_text': 'By zmail.'
        }
        # 发送email
        server.send_mail('lidan9152@163.com', mail)

    def sendHtml(self):
        '''
        发送html的邮件
        :return:
        '''
        with open(self.reportPath, 'r', encoding="utf-8") as f:
            content_html = f.read()
        mail = {
            'subject': '测试邮件标题-HTML!'+time.strftime("%Y-%m-%d %X"),  # Anything you want.
            'content_html': content_html,
        }
        server = zmail.server('420889656@qq.com', 'glaejvtpoqclbgbg')
        server.send_mail('lidan9152@163.com', mail)

    def sendFJ(self):
        '''
        发送带附件的邮件
        :return:
        '''
        mail = {
            'subject': '接口功能自动化测试报告'+time.strftime("%Y-%m-%d %X"),  # Anything you want.
            'content_text': '您好，附件为大行管接口功能自动化测试报告，请查收！',
            'attachments': [self.reportPath],  # Absolute path will be better.
        }
        server = zmail.server('420889656@qq.com', 'glaejvtpoqclbgbg')
        server.send_mail('lidan9152@163.com', mail)


if __name__ == '__main__':
    SendEmail().sendFJ()




