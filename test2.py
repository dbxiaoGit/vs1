import sys,os
import xlrd

_wb = xlrd.open_workbook('t1.xls')
_sheet = _wb.sheet_by_index(0)
print('hello world')  
