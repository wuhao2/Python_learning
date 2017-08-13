# _*_ coding: utf-8 _*_
from sqlite3 import connect,Row
db_name = 'test.db'

con = connect(db_name)
con.row_factory = Row
cur = con.cursor()
#批量插入的数据
rows = [(14,'Lily',12,'BeiJing'),(6,'John',13,"ChongQing")]
cur.executemany('insert into star (id,name,age,address) values (?,?,?,?)',rows)#通过执行此函数插入数据
#查寻数据并显示
cur.execute('select * from star')
for row in cur:
    for r in row:
        print(r)

con.commit()
con.close()