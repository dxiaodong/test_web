import xlrd
from xlutils.copy import copy
data ={'username': '李寒云', 'email': 'AeSAwRw@163.com', 'password': 'MHUQ9rAymV5UYB', 'cf_password': 'MHUQ9rAymV5UYB', 'qq': '93744', 'mobile': '15322778804', 'question': 7, 'answer': '一日不见，如三月兮'}
data_keys =list(data.keys())
print(data_keys)

data_values = []
for key in data.keys():
    data_values.append(data[key])
print(data_values)


"""写入excel数据"""

old_data = xlrd.open_workbook('../data/registerdata.xls')
old_sheet = old_data.sheet_by_index(0)
new_data = copy(old_data)
new_sheet = new_data.get_sheet(0)
# 插入新数据
insert_row_no = 1
for i in range(len(data_values)):
       new_sheet.write(1,i,data_values[i])

# 复写老数据
for row_index in range(insert_row_no,old_sheet.nrows):
       for col_index in range(old_sheet.ncols):
              new_sheet.write(row_index + 1,col_index,old_sheet.cell_value(row_index,col_index))

new_data.save('../data/registerdata.xls')



