# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 13:24'

# 读取../regular_file/output.xls文件，并修改
import xlrd
rbook = xlrd.open_workbook('../regular_file/output.xls')
rsheet = rbook.sheet_by_index(0)  # 取得表
print("add  before: ")
print("rsheet.nrows: ", rsheet.nrows, "rsheet.ncols: ",rsheet.ncols)
nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u"总分", None)  # 增加一列
for row in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    print("t is %.2f" % (t))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)  # 增加一列
print("after added: ")
print("rsheet.rows is %d,rsheet.cols is %d" % (rsheet.nrows, rsheet.ncols))

# 写excel并保存到../regular_file/output.xls
import xlwt
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizontal center')
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)
wbook.save('../regular_file/output.xls')



# cell = rsheet.cell(0, 0)
# cell2 = rsheet.cell(13, 2)
# print(cell.value)   # Intern termination Checklist
# print(cell2.value)   # Intern termination Checklist
# print(rsheet.nrows)
# print(rsheet.ncols)