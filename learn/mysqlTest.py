import mysql.connector as my
import datetime
# conn=my.connect(host='127.0.0.1',user='root',password='10086',database='test', buffered= True)
# try:
#     cursor=conn.cursor()
#     cursor.execute("select * from money")
#     print(cursor.fetchone())
# except conn.Error as err:
#     print('当前错误'+str(err))
# else:
#   conn.close()

config = {'host': '127.0.0.1',  # default localhost
          'user': 'root',
          'password': '10086',
          'port': 3306,  # 默认即为3306
           'database':'test',
          'charset': 'utf8',  # 默认即为utf8
          'buffered': True,
          }
try:
  conn = my.connect(**config)
  cursor = conn.cursor()
 # cursor.execute('truncate table money')
except my.Error as e:
  print('connect fails!{}'.format(e))




class MysqlDB:
  @classmethod
  def test_insert_mysql(self):
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   #时间转字符串
    cursor.execute('insert into  py (name ,title,createtime) values (%s,%s,%s)',['李四','加班不要',dt])
    conn.commit()
    # cursor.execute("select * from py")
    #
    # values=cursor.fetchall()
    # print(values)

    #cursor.execute(" truncate table py")
    #conn.commit()
    cursor.close()
    conn.close()

  @classmethod
  def insert_money(self,use_date,remark_date,remark,total_money,car_no):
    #print(use_date)
    cursor.execute('insert into money (use_date,remark_date,remark,total_money,car_no) '
                   'values (%s,%s,%s,%s,%s)', [use_date, remark_date, remark,total_money,car_no])
    conn.commit()

    #cursor.close()
    #conn.close()

  @classmethod
  def insert_Brand(self, id, full_name):
      # print(use_date)
      cursor.execute('insert into brand (id,full_name) values (%s,%s)', [id, full_name])
      conn.commit()
