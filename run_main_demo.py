"""
目的:
    将加载用例,执行用例,生成报告,发送邮件集成在一个文件下,形成方法:
步骤:
    1.加载测试用例
    2.执行测试用例
    3.获取最新的测试报告
    4.将最新的测试报告以邮件的形式发送
"""
import unittest,time,os
from plugins import HTMLTestRunnerPlugins
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1.加载测试用例
def add_case(case_path,rule):
    # 创建测试套件
    testsuite = unittest.TestSuite()
    # 加载需要执行的测试用例
    discover = unittest.defaultTestLoader.discover(case_path,
                                        pattern=rule,
                                        top_level_dir=None)
    # 将测试用例添加到测试套件中
    testsuite.addTests(discover)
    return testsuite

# 2.执行测试用例
def run_case(all_case,report_path):
    now = time.strftime("%Y_%m_%d %H_%M_%S %p")
    report_abspath = os.path.join(report_path,now + "report.html")
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(title="自动化测试报告",
                                                  description="测试用例执行情况",
                                                  stream=fp,
                                                  verbosity=2,
                                                  retry=0
                                                  )
    # 执行的用例是add_case方法的用例
    runner.run(all_case)
    fp.close()

# 3.获取最新的测试报告
def get_report_new(report_path):
    # 以列表的形式将所有测试报告读出来
    lists = os.listdir(report_path)
    # 根据最后修改时间对文件名进行排序
    lists.sort(key=lambda fn:os.path.getmtime(report_path + "\\" +fn))
    # 取出最新的测试报告
    print("最新测试报告:"+ lists[-1])
    report_file = os.path.join(report_path,lists[-1])
    return report_file

# 4.将最新的测试报告以邮件的形式发送
def send_mail(sender,password,addressee,smtpserver,report_file):
    # 实例化一个带附件的邮件
    msg = MIMEMultipart()
    msg['subject'] = "ECShop系统登录自动化测试报告"
    msg['from'] = sender
    msg['to'] = ";".join(addressee)
    # 邮件主体
    # 读取测试报告
    with open(report_file,"rb") as fp:
        mail_body = fp.read()

    body = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(body)

    # 邮件附件
    att = MIMEText(mail_body,_subtype='base64',_charset='utf-8')
    att['"Content-Type"'] = "application/octet-stream"
    # filename 可以使任意名字,只是文件后缀不能随意修改
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att)

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,password)
    smtp.sendmail(sender,addressee,msg.as_string())
    print("邮件发送成功")

if __name__ == '__main__':
    cur_path = os.path.dirname(os.path.relpath(__file__))
    case_path = os.path.join(cur_path,'test_suite')
    rule = 'test*.py'
    #1.加载测试用例
    all_case = add_case(case_path,rule)
    # 2.执行测试用例
    report_path = os.path.join(cur_path,'report')
    run_case(all_case,report_path)
    # 3.获取最新的测试报告
    report_file = get_report_new(report_path)
    # 4.发送邮件
    smtpserver = "smtp.163.com"
    sender = "ymsdtest@163.com"
    password = "zcx123456"
    addressee = ["ymsdtest@163.com","308597323@qq.com"]
    send_mail(sender,password,addressee,smtpserver,report_file)