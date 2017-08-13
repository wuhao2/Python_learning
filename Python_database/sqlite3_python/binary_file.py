# _*_ coding: utf-8 _*_
from sqlite3 import connect,Row,Binary
import binascii

db_name = 'test.db'

con = connect(db_name)
cur = con.cursor()

sql_scrpit = """
drop table if exists testa;
create table if not exists testa(id integer,data blob);
"""
cur.executescript(sql_scrpit)

f = open('test.jpg','rb')#以二进制格式打开一个文件
cur.execute('insert into testa (id,data) values (3,?)',(f.read(),))#调用游标的execute方法，以参数的形式向数据库中插入数据，

#在数据库中查询数据
cur.execute('select * from testa where id=3')
record = cur.fetchone()#获取一行记录
f = open('tt.jpg',"wb+")#重新打开一个文件，并且将从数据库中取出的数据重新写到tt.jpg文件中
f.write(record[1])

con.commit()
con.close()