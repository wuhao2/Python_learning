class MyMeta(type):
    def __init__(self,name,bases,dicts):
        print('Init Instance.')

    def __new__(cls,name,bases,dicts):
        dicts['info'] = lambda self:print('Djx.')
        res = type.__new__(cls,name,bases,dicts)
        res.company = 'MaiZi'
        return res

class custom(metaclass=MyMeta):
    pass

if __name__ == '__main__':
    cus = custom()
    cus.info()
    print(cus.company)

class cus:
    __metaclass__ = MyMeta
    pass

__metaclass__ = MyMeta