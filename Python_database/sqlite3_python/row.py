from sqlite3 import connect,Row

db_name = 'test.db'

con = connect(db_name)
con.row_factory = Row
cur = con.cursor()

cur.execute('select * from star')
row = cur.fetchone()#获取一个行对象

print(type(row))#查看列名

print('以列名访问：',row['name'])

print('以索引号访问：',row[1])

print('以迭代的访问：')
for item in row:
    print(item)

print("len():",len(row))#测试有多少列

con.close()