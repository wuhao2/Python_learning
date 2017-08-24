# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/19 14:57'
from inspect import signature


def f(a, b, c=1):
    pass
sig = signature(f)
print(sig.parameters)
# 实现一个对被装饰的函数的参数类型检查的装饰器

from inspect import signature


# 参数类型检测
def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        # func ->a,b
        # d = {'a':int,'b':str}
        sig = signature(func)  # 获取签名
        # 获得参数类型
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments

        def wrapper(*args, **kargs):
            # arg in d,instance(arg,d[arg])
            for name, obj in sig.bind(*ty_args, **ty_kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name]))
            return func(*args, **kargs)
        return wrapper
    return decorator


@typeassert(int, str, list)
def f(a, b, c):
    print(a, b, c)

# test
f(1, 'abc', [1, 2, 3])
f(1, 2, [1, 2, 3])