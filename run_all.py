import os
import run_main_demo

cur_path = os.path.dirname(os.path.relpath(__file__))
case_path = os.path.join(cur_path,'case')
rule = 'test_login.py'
#1.加载测试用例
all_case = run_main_demo.add_case(case_path,rule)
# 2.执行测试用例
report_path = os.path.join(cur_path,'report')
run_main_demo.run_case(all_case,report_path)
# 3.获取最新的测试报告
report_file = run_main_demo.get_report_new(report_path)
# 4.发送邮件
smtpserver = "smtp.163.com"
sender = "ymsdtest@163.com"
password = "zcx123456"
addressee = ["ymsdtest@163.com","308597323@qq.com"]
run_main_demo.send_mail(sender,password,addressee,smtpserver,report_file)