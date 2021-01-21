# -*- coding: utf-8 -*-
# @Project       : work_scripts
# @File Name     : learn_change.py
# @Author        : liushuangdan 
# @Date          : 2021/1/20 15:21
# @IDE           : PyCharm

# 1. dict 新特性 字典合并

# dict_a = {"Jack": "任中", "Diana": "LIU"}
# dict_b = {"Seth": "张玮豪", "Diana": "LIU"}
#
# dict_new_1 = dict_a | dict_b
# print(dict_new_1)
#
# print("**"*20)
#
# dict_new_2 = dict_b | dict_a
# print(dict_new_2)


"""

{'Jack': '任中', 'Diana': 'LIU', 'Seth': '张玮豪'}
****************************************
{'Seth': '张玮豪', 'Diana': 'LIU', 'Jack': '任中'}

"""

# 2. 新增用于移除前缀和后缀的字符串方法
#
# a_string = "~~Jack is a handsome man!~~"
#
# b_string = "**Jack is a handsome man!**"
#
# a_string_new = a_string.removeprefix("~~")
#
#
# b_string_new = b_string.removesuffix("**")
#
# print(a_string_new)
#
# print("-----------difference-------------")
#
# print(b_string_new)

"""

Jack is a handsome man!~~
-----------difference-------------
**Jack is a handsome man!

"""


# 3. 标准多项集中的类型标注泛型
"""
在类型标注中，3.9 支持使用内置多项集成类型，例如List， dict
做为通用类型而不必从typing导入对应的大写形式类型名
标准库中的其他一些类型现在也是通用的， 例如queue.Queue
"""


def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello %s!" % name)


greet_all(names=["Jack", "Diana", "Rose", "哲理瑞"])










