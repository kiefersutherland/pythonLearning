#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import xlwt
# from .mysqlTest import MysqlDB as db
import datetime

#转时间
def xldate_as_tuple(xldate, datemode=0):
  if isinstance(xldate, float):
        date = int(xldate)
        year, month, day, hour, minute, second = xlrd.xldate_as_tuple(date,datemode)
        #print(year)
        if month==12:
          year=2017
        py_date = datetime.datetime(year, month, day, hour, minute,  second)
        return py_date.strftime("%Y-%m-%d")

#写excel
def write_xls_data():
  book = xlwt.Workbook(encoding='utf-8', style_compression=0)
  sheet = book.add_sheet('test', cell_overwrite_ok=True)
  # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
  # 向表test中添加数据
  sheet.write(0, 0, 'EnglishName')  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
  sheet.write(1, 0, 'Marcovaldo')
  txt1 = '中文名字'
  sheet.write(0, 1,  txt1 )  # txt1.decode('utf8') 此处需要将中文字符串解码成unicode码，否则会报错??不需要了!
  txt2 = '马可瓦多'
  sheet.write(1, 1, txt2)
    # 最后，将以上操作保存到指定的Excel文件中
  book.save(r'f:\test1.xls')  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错
  print('成功保存')


#读excel
def read_xls_data():
 excelFile='F:\Book1.xlsx'
 data = xlrd.open_workbook(excelFile)

 table = data.sheets()[0]
 nrows = table.nrows #行数
 ncols = table.ncols #列数

 cc=0
 bus=0.0
 for i in  range(0,nrows):
   rowValues= table.row_values(i) #某一行数据
   for item in rowValues:
       pass
       # if isinstance(item,float):
       #   print('时间')
       # else:
       #print (item)
   #print(rowValues)

   if(rowValues[3]>0):
     cc+=rowValues[3]
   if str(rowValues[2]).find(r'交')>-1:
     bus+=rowValues[3]
     #print(rowValues)

   # db.insert_money(xldate_as_tuple(rowValues[0]),xldate_as_tuple(rowValues[1]),rowValues[2],rowValues[3],str(rowValues[4]))


def read_brand_data():
  excelFile = 'E:\最新品牌excel版.xlsx'
  data = xlrd.open_workbook(excelFile)
  table = data.sheets()[0]
  nrows = table.nrows  # 行数
  # print(nrows)
  for i in range(1, 10):
    rowValues = table.row_values(i)  # 某一行数据
    for item in rowValues:
      pass
     # print(rowValues[0],rowValues[1])
     #  db.insert_Brand(rowValues[0],rowValues[1])

if __name__=='__main__':
   read_brand_data()
   #read_xls_data()
  # write_xls_data()