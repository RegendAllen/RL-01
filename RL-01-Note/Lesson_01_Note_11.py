

# 21点的发牌生成器，可以自己记录一下，看看胜率，并与前面的蒙特卡罗方法比较一下


from itertools import product  # 引入离散数学的乘法
import random


numbers = '23456789TJQKA'  # 数字
colors = '黑红梅方'  # 花色
one_suite_cards = [n + c for n, c in product(numbers, colors)]  # 生成扑克牌


def distribute():
    random.shuffle(one_suite_cards)
    for c in one_suite_cards:
        yield c

print(next(distribute()))
print(distribute())
distribute()


