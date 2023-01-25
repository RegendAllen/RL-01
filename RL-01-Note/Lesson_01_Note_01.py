

# 为扑克牌游戏做准备


numbers = '23456789TJQKA'  # 数字
colors = '黑红梅方'  # 花色
attributes = 'xyz'  # 三副牌

for n in numbers:
    for c in colors:
        for a in attributes:
            print(n + c + a)
# 若还有其他条件，则for嵌套多层会非常难看明白，所以采用其他方法


print("++++++++++++++++++++++++++++++++++++++")


from itertools import product  # 引入离散数学的乘法

one_suite_cards = [ n+c for n,c in product(numbers, colors) ]

print(one_suite_cards)
print(len(one_suite_cards))
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

joker = "JK, jk".split()  # 大小王

# 给各张扑克按照不同大小赋值以供排序
def number_value(n):
    shift = 2  # 偏移值为2
    qq = numbers.find(n)
    print("numbers.find(n)是：" + str(qq))
    position_v = numbers.find(n) + shift

    if n == 'A':
        return position_v, 1  # A可以返回两个数，因为QKA是一种组合，A23是一种组合
    else:
        return position_v,  # 必须加一个逗号，表示输出的是tuple而不是int，这样后面才能用product函数迭代

print(number_value('A'))
print(number_value('黑'))  # 注意，当输入一个扑克牌中不存在的字符时，numbers.find（）函数不会报错，只会输出-1
print(number_value('9'))
print("================================================")

# 给扑克洗牌
import random

random.shuffle(one_suite_cards)
print(one_suite_cards)
print("##################################################")


def is_straight(hand):
    return print(number_value(n) for n, _ in hand)
is_straight(['2红', '3红', 'A梅'])

def is_straight(hand):
    return print([number_value(n) for n, _ in hand])
is_straight(['2红', '3红', 'A梅'])

def is_straight(hand):
    return print(set(number_value(n) for n, _ in hand))
is_straight(['2红', '3红', 'A梅'])

