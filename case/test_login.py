from script.login_flow import LoginFlow
from base.base_handle import Base
import unittest,ddt,time
from base.exceluntil import ExcelUntil
book = ExcelUntil("../data/userdata.xlsx")
data = book.get_sheet_info_by_index(0)

@ddt.ddt
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = LoginFlow()
        cls.driver = cls.login.driver
        cls.base = Base(cls.driver)
    @ddt.data(*data)
    def test_case_login(self,userdata):
        """登录测试"""
        self.login.login(userdata["username"],userdata["password"])
        result = self.login.is_login_success(userdata["username"])
        self.assertEqual(result, userdata["expect"])
        if result:
            self.login.logout()
            self.login.re_login()
        else:
            self.login.refresh()
            if self.base.is_alert_present() != False:
                self.base.operation_alter()
            time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.login.close_browser()

if __name__ == '__main__':
    unittest.main()

