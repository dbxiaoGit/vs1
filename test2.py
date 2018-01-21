import sys,os
import xlrd

_wb = xlrd.open_workbook('t1.xls')
_sheet = _wb.sheet_by_index(0)
print('hello world')  
for _row in range(_sheet.nrows) :
    print(_sheet.row_values(_row))
