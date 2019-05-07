import xlrd
from xlutils.copy import copy

class ExcelUntil:
    def __init__(self,file_path):
        """初始化表格"""
        self.file_path = file_path
        self._table = xlrd.open_workbook(file_path)

    def data_type_conversion(self,val):
        """转化excel中的数字和True,False"""
        if isinstance(val,float):
            value = str(int(val))
            return value
        elif isinstance(val,int):
            if val == 1:
                return True
            elif val == 0:
                return False
        else:
            return val

    def _get_execl_info(self):
        """获取表格信息,并输出列表字典格式"""
        key = self._sheet.row_values(0)
        data_list = []
        for i in range(1, self._sheet.nrows):
            #value =  self._sheet.row_values(i)
            value = [self.data_type_conversion(val) for val in self._sheet.row_values(i)]
            tmp = zip(key, value)
            # print(dict(tmp))
            data_list.append(dict(tmp))
        #print(userdata_list)
        return data_list
    def get_sheet_info_by_name(self,sheetname):
        self._sheet = self._table.sheet_by_name(sheetname)
        return self._get_execl_info()
    def get_sheet_info_by_index(self,index):
        self._sheet = self._table.sheet_by_index(index)
        return self._get_execl_info()

    def write_data(self,list):
        """更新excel表格数据"""
        old_sheet = self._table.sheet_by_index(0)
        new_table = copy(self._table)
        new_sheet = new_table.get_sheet(0)
        # 插入新数据
        insert_row_no = 1 #新数据插入在表格的第一行
        for i in range(len(list)):
            new_sheet.write(1,i,list[i])

        # 复写老数据
        for row_index in range(insert_row_no,old_sheet.nrows):
            for col_index in range(old_sheet.ncols):
                new_sheet.write(row_index + 1,col_index,old_sheet.cell_value(row_index,col_index))

        # 保存更新后的表格
        new_table.save(self.file_path)

    def get_col_data(self,col_name):
        """根据列名找到对应的列的数据"""
        col_name = None
        col_index = 0
        sheet = self._table.sheet_by_index(0)
        for i in range(sheet.ncols):
            if(sheet.cell_value(0,i) == col_name):
                col_index = i
        col_index_value = sheet.col_values(col_index,1,sheet.nrows)
        return col_index_value

if __name__ == '__main__':
    book = ExcelUntil("../data/userdata.xlsx")
    data1 = book.get_sheet_info_by_index(0)
    # data2 = book.get_sheet_info_by_name("userdata")
    # print(data1)
    # #print(data2)
    print(data1)


