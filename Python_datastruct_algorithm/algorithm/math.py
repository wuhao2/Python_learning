# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 22:47 '
#java代码
# 小算法----> 1！ +  2！ + 3！ + .....
# 算法方式1：（两层for循环）
#         int sum = 0;
#         for(int i = 1; i<=3; i++){
#             int temp = 1;
#             for (int j = 1; j<=i; j++){
#                 temp *= j;
#             }
#             sum = sum + temp;
#         }
#         System.out.println(sum);
# 小算法------>九九乘法表
#         for (int i= 1; i<=9; i++){
#             for (int j=1; j<=i; j++){
#                 System.out.print(j + "*" + i + "=" + j*i + "\t");//不换行
#             }
#             System.out.println();//换行
#
#    }
"""
#python实现九九乘法表
def nineNineMuti():
    for i in range(1, 10):
        for j in range(1,i+1):
            print(j,"*",i,"=",j*i,"\t",end='')#不换行
        print()#换行
nineNineMuti()
"""
#python实现1! + 2！+   +n!
def math(n):
    sum = 0
    for i in range(1,n+1):
        temp =1
        for j in range(1,i):
            temp *= j
            sum = sum + temp
    print(sum)
math(4)