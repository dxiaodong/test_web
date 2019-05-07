"""
生成HTML测试报告
使用HTMLTestRunner

"""
import os,time,unittest
from plugins import HTMLTestRunnerPlugins

# 用例路径
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
# 创建测试用例集
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test_login.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    # 测试报告保存路径及测试报告名称
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    stream = open(report_path + '\\' + now + 'HTMLReport.html', 'wb')
    # 创建执行用例的方法--定义测试报告
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        title='ECShop web自动化测试报告',# 测试报告的标题
        description='用例执行情况',# 测试报告描述
        stream=stream,#测试报告存放位置,写入报告
        verbosity=2,#执行结果概述
        retry=0#设置重复执行次数
    )
    # 执行测试用例
    runner.run(all_case())
    stream.close()



