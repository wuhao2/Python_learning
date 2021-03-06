# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 21:08'

pl = ["<0112>", "<32>", "<1024x768", "<60>", "<1>", "<100.0>"]
s = ''
for p in pl:
    s += p
    print(s)

# 资源巨大的浪费：大量的字符串拷贝，资源回收与释放，如果字符串很长时，巨浪费
# <0112>
# <0112><32>
# <0112><32><1024x768
# <0112><32><1024x768<60>
# <0112><32><1024x768<60><1>
# <0112><32><1024x768<60><1><100.0>
# 利用join就不存临时变量的浪费, 推荐使用
print('****'*10)
print(''.join(pl))

print('****'*10)
print(';'.join(['abc', '123', 'xyz']))  # 以；相连接
print(''.join(['abc', '123', 'xyz']))  # 以，连接

print('****'*10)
l = ['abc', 123, 45, 'xyz']
print(''.join([str(x) for x in l]))  # 列表解析产生了一个新列表，如果原列表很多，又是一个大的开销
print(''.join(str(x) for x in l))  # （str(x) for x in l）产生的是一个生成器，开销很小
