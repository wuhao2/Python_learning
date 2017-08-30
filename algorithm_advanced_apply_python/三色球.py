# 若一个口袋中放有12个球， 其中有3个红球，3个黄球，6个绿球。
# 从中任意取8个球。
# 问共有多少中国不同的颜色搭配方法。

# 比较简单，用穷举法, 抽象三种球的个数分别为:
# 0<=red<=3;  0<=yellow<=3yellow  green=8 - red - yellow


def fun():
    count = 0
    for red in range(4):
        for yellow in range(4):
            if 8 - red - yellow <= 6:
                print(red, yellow, 8-red-yellow)
                count += 1
    print("count:", count)

print(fun())
