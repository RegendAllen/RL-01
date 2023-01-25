

# 扑克牌的顺子和同花，并计算顺子和同花各自的概率


from itertools import product  # 引入离散数学的乘法
import random


numbers = '23456789TJQKA'  # 数字
colors = '黑红梅方'  # 花色
one_suite_cards = [n + c for n, c in product(numbers, colors)]  # 生成扑克牌

# 洗牌，然后发牌
def distribute_hand(people_n):
    card_n = 3
    random.shuffle(one_suite_cards)  # 洗牌
    random_hand = [ one_suite_cards[i:i+card_n] for i in range(people_n) ]  # 发牌
    return random_hand

print(distribute_hand(people_n=3))


# 定义同花
def is_flush(hand):
    return len(set(c for _, c in hand)) == 1


# 给各张扑克按照不同大小赋值以供排序
def number_value(n):
    shift = 2  # 偏移值为2
    position_v = numbers.find(n) + shift
    if n == 'A':
        return position_v, 1  # A可以返回两个数，因为QKA是一种组合，A23是一种组合
    else:
        return position_v,  # 必须加一个逗号，表示输出的是tuple而不是int，这样后面才能用product函数迭代

# 排序（看是否符合顺子）
def asc(numbers):
    numbers = sorted(numbers)
    return numbers[2] - numbers[1] == numbers[1] - numbers[0] == 1


# 定义顺子
def is_straight(hand):
    # sorted_n = sorted(hand)
    possible_numbers = [number_value(n) for n, _ in hand]

    all_combination = list(product(*possible_numbers))

    return any(asc(h) for h in all_combination)

print(is_straight(['2红', '3红', 'A梅']))


'''
在编程的时候尽量用变量代替字符串，如FLUSH, STRAIGHT = 'flush', 'straight'，
这样下面在引用变量的时候会高亮显示，或在打错变量名称的时候有红线报错，
而直接用字符串，在字符串因为打错或顺序错误时候，如'straight'和'striaght'、'staright'等，会导致程序不会报错但跑不通。

在编程的时候尽量不要使用除数字0和1之外的数字，
其他的数字叫”magic number“，
如果需要其他数字，用变量表示后引用变量即可，如 
shift = 2   
position_v = numbers.find(n) + shift
不要直接用数字将之写为
position_v = numbers.find(n) + 2
因为如果下面的程序中仍然有很多地方使用了同样的逻辑，那么就需要一行一行仔细改下去，稍不注意就会出错，
这样就不如直接用变量表示数字然后再引用变量
'''


# 分别计算同花和顺子的概率
from collections import Counter

poker_counter = Counter()
total_hand = 0
FLUSH, STRAIGHT = 'flush', 'straight'

for t in range(10000):
    for hand in distribute_hand(people_n=5):
        total_hand += 1
        if is_flush(hand):
            poker_counter[FLUSH] += 1
        elif is_straight(hand):
            poker_counter[STRAIGHT] += 1

print('Flush : ' + str(poker_counter[FLUSH] / total_hand))
print('Straight : ' + str(poker_counter[STRAIGHT] / total_hand))
print( 'Flush / Straight = ' + str(poker_counter[FLUSH]/poker_counter[STRAIGHT]) )


# 将上面计算概率的思路整理并封装为函数
def get_poker_env(people, round_number=10000):
    poker_counter = Counter()
    total_hand = 0
    FLUSH, STRAIGHT = 'flush', 'straight'
    for t in range(round_number):
        for hand in distribute_hand(people_n=people):
            total_hand += 1
            if is_flush(hand):
                poker_counter[FLUSH] += 1
            elif is_straight(hand):
                poker_counter[STRAIGHT] += 1
    return poker_counter

'''
# 测试上述计算概率的函数
people_numbers = range(2, 17)
r = 800
rates = []
for n in people_numbers:
    result = get_poker_env(n, r)
    rates.append(result[FLUSH] / result[STRAIGHT])

import matplotlib.pyplot as plt
plt.plot(people_numbers, rates)  # 坐标轴横轴为参加游戏人数，纵轴为同花比顺子的比率
plt.show()  # 调用show方法才能显示
'''


# 实时观察计算进度的方式计算大样本比率
from tqdm import tqdm


people_numbers = range(2, 17)
r = 20000
rates = []
for n in tqdm(people_numbers):
    result = get_poker_env(n, r)
    rates.append(result[FLUSH] / result[STRAIGHT])

import matplotlib.pyplot as plt
plt.plot(people_numbers, rates)  # 坐标轴横轴为参加游戏人数，纵轴为同花比顺子的比率
plt.show()  # 调用show方法才能显示


'''
思考题：
1、如果押中”什么都没有“，奖励2元，请问押中 FLUSH 和 STRAIGHT 应该奖励多少钱？
2、假设 FLUSH 为15元，STRAIGHT 为60元，问一直开下去是顾客吃亏还是庄家吃亏？
3、假设 FLUSH 为20元，STRAIGHT 为40元，问一直开下去是顾客吃亏还是庄家吃亏？


课后作业：
1、改变代码，增加大小王，大小王可以替代任何数字；
2、将一手牌的张数变为5个，计算在人数为10人时，分别计算下列扑克的概率：
    straight flush：同花顺，即五张同花色的连续数字牌
    four of a kind：其中四张是相同数字的扑克牌
    full house：葫芦，三张相同数字及另外两张相同数字的牌 AAA+BB
    flush：五张相同花色的牌
    strsight：五张连续数字的牌
    three of a kind：三条
    two pair：两对
    pair：一个对子和另外三张无法组成牌型的杂牌
3、在以上的概率求解中，有一个隐藏的bug，导致概率计算有一些轻微的错误，请问这个错误是什么？请修正它。
4、请思考蒙特卡罗方法求解问题和基于组合数学、概率等方法的区别是什么？在计算机环境下有什么优势？
'''



