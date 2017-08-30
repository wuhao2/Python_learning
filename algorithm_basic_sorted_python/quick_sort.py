# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/2 13:30 '

# 快速排序要点：1、选择基准数据 2、left和right指针和 活动指针的交叉移动

def quick_sort(array, left, right):
    if left < right:
        base = quick_sort_process(array, left, right)
        quick_sort(array, left, base)  # 对base左边的数据进行排序
        quick_sort(array, base + 1, right)  # 对base右边的数据进行排序


# 快速排序过程函数
def quick_sort_process(array, left, right):
    base = array[left]
    while left < right:
        # 如果右边的数大于base，则活动指针不需要移动，只需要将right指针前向移动
        while left < right and array[right] >= base:
            right -= 1
        # 如果右边的数小于base，
        while left < right and array[right] < base:
            array[left] = array[right]  # 先将右边的数放到左边
            left += 1  # 左指针加1
            array[right] = array[left]  # 将左边的是放到右边，这样避免了活动指针交叉变换到左边
    array[left] = base
    return left


list = [3, 2, 4, 1, 59, 23, 13, 11, 34]
quick_sort(list, 0, len(list) - 1)
print("after sorted:", list)
