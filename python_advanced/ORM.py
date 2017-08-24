# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/21 9:29'

"""
ORM全称“Object Relational Mapping”，即对象-关系映射，
就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，
写代码更简单，不用直接操作SQL语句。
要编写一个ORM框架，所有的类都只能动态定义，
因为只有使用者才能根据表的结构定义出对应的类来
"""
"""
当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，
如果没有找到，就继续在父类Model中查找metaclass，找到了，
就使用Model中定义的metaclass的ModelMetaclass来创建User类，
也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

在ModelMetaclass中，一共做了几件事情：
排除掉对Model类的修改；

在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，
同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；

把表名保存到__table__中，这里简化为表名默认为类名。

在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
"""
# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


# 基类Model：
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，
# 想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

"""
序列化与反序列化
"""
import pickle
d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，
# 就可以把这个bytes写入文件。或者用另一个方法pickle.dump()
# 直接把对象序列化后写入一个file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()
# 方法从一个file-like Object中直接反序列化出对象。
# 我们打开另一个Python命令行来反序列化刚才保存的对象：
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)  # 反序列结果：{'score': 88, 'age': 20, 'name': 'Bob'}

"""
JSON类型  	Python类型
{}	        dict
[]	        list
"string"	str
1234.56	    int或float
true/false	True/False
null	    None
"""

# import json
# d = dict(name='Bob', age=20, score=88)
# json.dumps(d)  # '{"age": 20, "score": 88, "name": "Bob"}'
#
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# json.loads(json_str)
# print(json_str)  # {"age": 20, "score": 88, "name": "Bob"}

import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):  # 序列化函数
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):  # 反序列化函数
    return Student(d['name'], d['age'], d['score'])
# 序列化
s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))
# 把calss实例序列化为json的dict{"score": 88, "age": 20, "name": "Bob"}

# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。
# 我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))