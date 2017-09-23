# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 18:00'

if __name__ == "__main__":
    import pickle

    # 在a.txt
    obj = 123, "abcdedf", ["ac", 123], {"key": "value", "key1": "value1"}
    print(obj)

    f = open("a.txt", 'wb')
    pickle.dump(obj, f)  # 序列化
    f.close()

    f = open("a.txt", 'rb')  # 反序列化
    print(pickle.load(f))

##########################################
    # 在内存中
    obj1 = pickle.dumps(obj)  # 序列化
    print(type(obj1))  # <class 'bytes'>
    print(obj1)  # 二进制方式存储在内存中

    obj2 = pickle.loads(obj1)  # 反序列化
    print(obj2)
