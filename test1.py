print('hello world')
import xlwt
#from datetime import datetime
import datetime

class ExcelTest :
    def __init__(self):
        _style1 = xlwt.easyxf(num_format_str='YYYY/MM/DD')
        _work_book = xlwt.Workbook()
        _sheet_1 = _work_book.add_sheet(sheetname='sheet 1',cell_overwrite_ok=True)

        _sheet_1.write(0,0,'日期')
        _sheet_1.write(0,1,'类型')
        _sheet_1.write(0,2,'名字')
        _sheet_1.write(0,3,'科目')
        _names = ['Aaron,托福,1','Galen,托福,2','Alex,托福,2','Sammy,雅思,1','Amy,雅思,2']
        i = 1
        j = 0
        
        while i < 100  :
            for _name in _names :
                _today = datetime.datetime.today()
                _offset_day = datetime.timedelta(days=j)
                _target_day = _today + _offset_day
                _work_type_1 = ''
                _work_type_2 = ''
                _work_type = ''

                if _target_day.day % 2 ==0 :
                    _work_type_1 = '班'
                    _work_type_2 = '休'
                else :
                    _work_type_1 = '休'
                    _work_type_2 = '班'

                if _name.split(',')[2] =='1' :
                    _work_type = _work_type_1
                else :
                    _work_type = _work_type_2

                _sheet_1.write(i,0,_target_day,_style1)
                _sheet_1.write(i,1,_work_type)
                _sheet_1.write(i,2,_name.split(',')[0])
                _sheet_1.write(i,3,_name.split(',')[1])
                i+=1
            j+=1
        _work_book.save('t1.xls')   
 


if __name__ == '__main__' :
    ExcelTest()