import unittest
from script.register_flow import RegisterFlow
from base.register_data import RegisterData
from base.exceluntil import ExcelUntil

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.rf = RegisterFlow()
        self.data = RegisterData()
        self.execl = ExcelUntil("../data/registerdata.xls")
    def test_case_1(self):
        data = self.data.full_register()
        data_list = self.data.get_data_list(data)
        self.execl.write_data(data_list)
        self.rf.full_register(data)


if __name__ == '__main__':
    unittest.main()