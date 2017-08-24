# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 11:26 '

"""
#选择排序
#循环len(list)次，找最小，依次从大到小排序

def selectSort(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[j]<list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
        # i+=1 #多余的

list = [9,8,7,6,5,4,3,2,1]
selectSort(list)
print("after sorted：", list)#after sorted： [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""



"""
def selectSort(arr):#选择排序
    for i in range(0, len(arr)):
        k = i
        for j in range(i+1, len(arr)):#循环len(list)趟
            if arr[j] < arr[k]:
                k = j
        arr[i],arr[k] = arr[k],arr[i]#交换位置
list = [9,8,7,6,5,4,3,2,1]
selectSort(list)
print(list)#[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""




#this is my source code

list = [7,6,9,8,5,4,3,2,1]
# temp = 0
# for i in range(0, len(list)):
#     if temp <= list[i]:
#         temp = list[i]
# print(temp)
def select(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return print(list)
select(list)


