from script.login_flow import LoginFlow
from base.base_handle import Base
import unittest,time
import paramunittest
# from base.exceluntil import ExcelUntil
# book = ExcelUntil("./data/userdata.xlsx")
# data = book.get_sheet_info_by_index(0)

@paramunittest.parametrized(
    {'username': '诸葛亮', 'password': 'Test123456', 'expect': 'True'},
    {'username': '诸葛亮', 'password': 'Test123457', 'expect': 'False'},
    {'username': '诸葛亮', 'password': 'Test123458', 'expect': 'False'},
    {'username': '诸葛亮', 'password': 'Test123459', 'expect': 'False'},
    {'username': '诸葛亮', 'password': 'Test123460', 'expect': 'False'},
)

class LoginTest(unittest.TestCase):
    def setParameters(self,username,password,expect):
        self.username = username
        self.password = password
        self.expect = expect

    @classmethod
    def setUpClass(cls):
        cls.login = LoginFlow()
        cls.driver = cls.login.driver
        cls.base = Base(cls.driver)
		
	def setUp(self):
        cls.login = LoginFlow()
        cls.driver = cls.login.driver
        cls.base = Base(cls.driver)

    def test_case_login(self):
        expect_data = self.expect
        if expect_data == "True":
            expect_data = True
        else:
            expect_data = False
        self.login.login(self.username,self.password)
        result = self.login.is_login_success(self.username)
        self.assertEqual(result, expect_data)
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

