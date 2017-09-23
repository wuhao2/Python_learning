# _*_ coding: utf-8 _*_
from sqlite3 import connect,Row
import binascii

db_name = 'test.db'
#定义一个类，聚合函数定义，可以定义一些用于操作数据库的统计函数
class AbsSum:
    def __init__(self):
        self.s = 0
    def step(self,v):
        self.s += abs(v)#取绝对值并求和
    def finalize(self):
        return self.s

con = connect(db_name)
con.create_aggregate('abssum',1,AbsSum)

cur = con.cursor()

sql_scrpit = """
drop table if exists testa;
create table if not exists testa(id integer,name text,score integer);
insert into testa (id,name,score) values (3,"Lily",8);
insert into testa (id,name,score) values (4,"Jhon",-7);
"""
cur.executescript(sql_scrpit)

cur.execute('select abssum(score) from testa')#对所有的分数取绝对值求和
for item in cur:
    print(item)

con.commit()
con.close()