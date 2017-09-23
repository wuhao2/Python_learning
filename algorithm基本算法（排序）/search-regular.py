# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 23:39 '
"""
//小算法----->搜索数组中的元素

//查找数组中是否存在某元素----算法方式一  时间复杂度为O（n） 性能不高，要比较n次
        int[] data = new int[]{1,4,6,7,6,234,56,123,85};//数组的静态初始化，最好不要用，表示匿名数组new int[]{1,4,6,7,6}

        boolean flag = false;
        int searchdata = 234;

        for (int i =0; i<data.length; i++){
            if (data[i] == searchdata){
                System.out.println(data[i]);
                flag = true;
            }
        }
        if(flag){
            System.out.println("数据已经查找到！");//成功，但是代码的性能不高，他需要将数组中的每一个元素进行比较，
        }else {
            System.out.println("数据没有查找到！");
        }
"""


# python实现在list中简单搜索某个元素是否存在
def search(data):
    list = [1, 4, 6, 7, 6, 234, 56, 123, 85]
    flag = False
    searchData = data
    for i in range(len(list)):
        if list[i] == searchData:
            print(list[i])
            flag = True
    if flag:
        print("searchData exist in list,and found")
    else:
        print("searchData not found")


search(34)
