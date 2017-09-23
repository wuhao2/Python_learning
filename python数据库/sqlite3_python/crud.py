from sqlite3 import connect

db_name = 'test.db'

con = connect(db_name)
cur = con.cursor()

# #创建表
# cur.execute('create table star(id integer,name text,age integer,address text)')
#定义数据行（多行）
# rows = [(1,"王俊凯",16,"重庆"),(2,"王源",15,"重庆"),(3,"易烊千玺",15,"怀化")]
#
# #多次执行插入语句
# for item in rows:
#     cur.execute("insert into star (id,name,age,address) values (?,?,?,?)",item)
#
# #查询，显示每一行数据
# cur.execute('select * from star')
# for row in cur:
#     print(row)
#
# #数据库更新操作
# cur.execute('update star set age=? where id=?',(18,3))
# cur.execute('select * from star')
# for row in cur:
#     print(row)

cur.execute('delete from star where id=?',(2,))
cur.execute('select * from star')
for row in cur:
    print(row)

con.commit()
con.close()