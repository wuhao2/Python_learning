# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 22:35 '
#java代码实现数组反转
# public static void reverser(int[] numbers, int length) {
#         int left = 0;
#         int right = length -1;//制定两个索引left和right，交换，加1，减1，再交换，
#         while (left<right){//应用while循环最棒
#             int temp = numbers[left];//直接逆序元素组中的元素
#             numbers[left] = numbers[right];//此算法没有消耗额外的内存，空间复杂度小
#             numbers[right] = temp;
#             left++;
#             right--;
#         }
#python反转数组
def reverse_array(list):
    left = 0
    right = len(list)-1
    while left<right:
        list[left],list[right] = list[right],list[left]
        left+=1
        right-=1
list = [1,2,3,4,5,6,7,8,9]
reverse_array(list)
print("reverse list:",list)#reverse list: [9, 8, 7, 6, 5, 4, 3, 2, 1]
