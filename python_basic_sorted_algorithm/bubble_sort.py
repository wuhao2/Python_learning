# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 22:00 '
#java代码
# public static void bubbleSort(int[] numbers, int n){
#
#         for (int i = 1; i <= n-1; i++ ){//比较n-1轮
#
#             for (int j = 1; j <= n-i; j++){
#                 //比较相邻两个数
#                 if (numbers[j-1] > numbers[j]){
#                     int temp = numbers[j-1];
#                     numbers[j-1] = numbers[j];
#                     numbers[j] = temp;
#                 }
#             }
#
#         }
#     }

# 遍历数据

def printData(list):
    print("本轮排序结果：", list, end='')
    print()


# python冒泡排序法
def bubbleSort(list):
    for i in range(len(list)-1):  # 比较len(list)-1轮 ，
        for j in range(len(list)-1-i):  # 比较两个相邻的数 ，找最大的数，排在最后
            if list[j] > list[j+1]:
                # temp = list[j]
                # list[j] = list[j+1]
                # list[j+1] = temp
                list[j], list[j+1] = list[j+1], list[j]#交换位置
        printData(list)  # 查看排序结果

list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubbleSort(list)
print("after sorted:", list)#after sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9]