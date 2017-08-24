# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/7 15:59 '

#穷举法，列出不重复的三位数
#百位数a：1-9
#十位数b：0-9
#个位数c：0-9

def fun():

    count = 0
    list = range(10)
    for a in list[1:]:#因为a是1-9之间
        for b in list:
            if a==b:continue  #过滤了a=b的情况
            for c in list:
                if c!=a and c!=b: #再次过滤a=c,b=c的情况
                    print(a,b,c)#产生了所有的三位数
                    count +=1
    print('count:', count)

fun()