# -*- coding: utf-8 -*-
# @Project       : work_scripts
# @File Name     : learn_change1.py
# @Author        : liushuangdan 
# @Date          : 2021/1/20 16:27
# @IDE           : PyCharm


# 1. 新增语法 赋值表达式
"""
新增的语法 := 可在表达式内部为变量赋值。 它被昵称为“海象运算符”因为它很像是 海象的眼睛和长牙。
以下实例中， 赋值表达式可以避免调用 len() 两次
"""
import re
from datetime import date
from math import cos, radians

from Tools.scripts.pdeps import process
from unicodedata import normalize

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
if (n := len(a)) > 10:
    print(f"List is too long ({n}) elements, expected <= 10)")

"""
List is too long (11) elements, expected <= 10)
"""

"""
类似的益处还可以提现再正则表达式匹配中需要使用两次匹配对象的情况中
一次检测用于匹配是否发生，另一次用于提取子分组
"""

advertisemnt = "The shirt was 5 $, but now it's on sale at 20% discount."
discount = 0.0
if mo := re.search(r'(\d+)% discount', advertisemnt):
    discount = float(mo.group(1)) / 100.0
    print(discount)

# 此运算符也适合用于配合while循环计算一个值来检测循环是否终止， 而同一个值又在循环体中再次被使用的情况
# loop over fixed length blocks
# f 不确定是不是 读取文件 rename 的f， process 不确定是从哪个包引入的，官网上没有注明
# while (block := f.read(250)) != "":
#     process(block)

# 出现在列表推导式中， 在筛选条件中计算一个值， 而同一个值又在表达式中需要被使用

# [clean_name.title() for name in names if (clean_name := normalize("NFC", name)) in allowed_names]

# 2. 仅限位置形参
"""
新增一个函数形参语法 / 

用来指明某些函数形参必须使用仅限位置而非关键字参数的形式。

这种标记语法与通过help（）所显示的使用Larry Hastings 的Argument Clinic工具标记的C函数相同

在下面的例子中， 形参a和b为仅限位置形参，c或d可以是位置形参或关键字形参， 而e或f 要求为关键字形参
"""


def func_param(first_param, b, /, c, d, *, e, f):

    print("仅限位置形参", first_param, b)
    print("位置形参或者关键字形参", c, d)
    print("关键字形参", e, f)


# 以下是合法的调用
func_param(10, 20, 30, d=40, e=50, f=66)

"""
仅限位置形参 10 20
位置形参或者关键字形参 30 40
关键字形参 50 66


func_param(10, b=20, c=30, d=40, e=50, f=60)   # b 不可以是一个关键字参数
func_param(10, 20, 30, 40, 50, f=60)           # e 必须是一个关键字参数

这种标记形式的一个用例是它匀速纯python函数完整模拟现有的用C代码编写的函数的行为。
例如： 内置的pow()函数不接受 关键字参数：
"""


def pow_func(x, y, z=None, /):
    """Emulate the built in pow function"""
    r = x * y
    return r if z is None else r % z


print(pow_func(1, 3))


"""
3

另一个用例是在不需要形参名称时排除关键字参数。 例如： 内置的 len()函数的签名为len(obj, /).
这个可以排除如下笨拙的调用方式
"""

# len(obj='hello')  # The "obj" keyword argument impairs readability

# 另一个益处是将形参标记为仅限位置形参将允许在未来修改形参名而不会破坏客户的代码。
# 例如，在 statistics 模块中，形参名 dist 在未来可能被修改。这使得以下函数描述成为可能:

"""
def quantiles(dist, /, *, n=4, method='exclusive')  
    ...
"""

# 由于在 / 左侧的形参不会被公开为可用关键字，其他形参名仍可在 **kwargs 中使用:


def f(a, b, /, **kwargs):
    print(a, b, kwargs)


f(10, 20, a=1, b=2, c=3)

"""
# a and b are used in two ways 
10 20 {'a': 1, 'b': 2, 'c': 3}
"""


# 这极大地简化了需要接受任意关键字参数的函数和方法的实现

"""
class Counter(dict):    

    def __init__(self, iterable=None, /, **kwds):   

        # Note "iterable" is a possible keyword argument
"""

# 3. f 字符串支持 =
"""
增加 = 说明符用于 f-string。 形式为：f'{expr=}' 的 f 字符串将扩展表示为表达式文本， 加一个等于号， 再加表达式的求值结果
"""
user = 'Diana'
member_since = date(1993, 3, 8)
print(f'{user=} {member_since=}')

"user='Diana' member_since=datetime.date(1993, 3, 8)"

# f 字符串格式说明符允许更细致地控制所要显示的表达式结果:

delta = date.today() - member_since

print(f'{user=!s}  {delta.days=:,d}')

'user=Diana  delta.days=10,181'


# = 说明符将输出整个表达式，以便详细演示计算过程:

theta = 10
print(f'{theta=} {cos(radians(theta))=:.3f}')

"theta=10 cos(radians(theta))=0.985"

