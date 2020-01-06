import unittest

import app
import time

from script.login import Login
from script.test_emp import TestIHRMEmp

from tools.HTMLTestRunner import HTMLTestRunner

# 1.初始化测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))
# 使用HTMLTestRunner执行测试套件,生成测试报告
report_path = app.BASE_DIR + '/report/ihrm{}.html'.format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path, mode='wb')as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=1, title='IRHM人力资源接口测试', description='v1.0.0')
    # 执行测试套件
    runner.run(suite)
