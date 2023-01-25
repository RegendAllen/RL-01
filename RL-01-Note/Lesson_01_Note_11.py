

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

'''
课后作业：
1、整理复现课程上的代码，并将之封装为  .py文件
2、课程中的代码是先全部sampling，然后再利用所有sampling的结果更新policy，这是off-line的形式，
    请将之改为一边sampling，一边更新policy的on-line形式。
3、在2的on-line基础上，观察mean-reward随着episode增加后的变化趋势，产出结果画为图形
4、你认为还有哪些方式增加胜率和mean-reward？
5、强化学习与监督学习和非监督学习最大的区别是什么？（提示：强化学习和监督学习都需要预测一个结果，
    但这两个的预测过程不同；强化学习与非监督学习都不需要人工标注label，但它们之间有很大区别）'''



