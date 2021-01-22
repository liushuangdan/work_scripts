# -*- coding: utf-8 -*-
# @Project       : work_scripts
# @File Name     : learn_change.py
# @Author        : liushuangdan 
# @Date          : 2021/1/20 15:21
# @IDE           : PyCharm

# 语言上的变化

# 1. dict 新特性 字典合并

dict_a = {"Jack": "任中", "Diana": "LIU"}
dict_b = {"Seth": "张玮豪", "Diana": "LIU"}

dict_new_1 = dict_a | dict_b
print(dict_new_1)

print("**" * 20)

dict_new_2 = dict_b | dict_a
print(dict_new_2)

"""

{'Jack': '任中', 'Diana': 'LIU', 'Seth': '张玮豪'}
****************************************
{'Seth': '张玮豪', 'Diana': 'LIU', 'Jack': '任中'}

"""

# 2. 新增用于移除前缀和后缀的字符串方法

a_string = "~~Jack is a handsome man!~~"

b_string = "**Jack is a handsome man!**"

a_string_new = a_string.removeprefix("~~")

b_string_new = b_string.removesuffix("**")

print(a_string_new)

print("-----------difference-------------")

print(b_string_new)

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

# 4. 使用python进行相应导包的时候，import出现异常时类型由原来的ValueError变成了ImportError。

"""
Resolve a relative module name to an absolute one.

 bits = package.rsplit('.', level - 1)
 if len(bits) < level:
- raise ValueError('attempted relative import beyond top-level package')
+ raise ImportError('attempted relative import beyond top-level package')
 base = bits[0]
 return '{}.{}'.format(base, name) if name else base


#globals() 函数会以字典类型返回当前位置的全部全局变量。
#locals() 函数会以字典类型返回当前位置的全部局部变量。
ImportError 触发异常原因：在涉及到相对导入时，package 所对应的文件夹必须正确的被 python 解释器视作 package ，
而不是普通文件夹。否则由于不被视作 package，无法利用 package 之间的嵌套关系实现 Python 中包的相对导入。
"""

# 5. Python 现在获取在命令行上指定的脚本文件名的绝对路径
"""
（例如：python script.py：main 模块的 file 属性，sys.argv[0] 和 sys.path[0] 显示的也是绝对路径，
而不是相对路径 (这地方之前提出了一个 bug)，通过 os.chdir（）更改当前目录后，这些路径仍然有效。
但是现在出现异常 traceback 信息的时候还会显示.

__main__模块的绝对路径。（由 Victor Stinner 在 bpo-20443 中贡献。）

"""

import sys

print(f"{__file__=}")
print(f"{sys.argv[0]=}")
print(f"{sys.path[0]=}")

"""
__file__='D:\\work_scripts\\python39_new\\learn_change.py'
sys.argv[0]='D:/work_scripts/python39_new/learn_change.py'
sys.path[0]='D:\\work_scripts\\python39_new'
"""


