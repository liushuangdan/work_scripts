# -*- coding: utf-8 -*-
# @Project       : work_scripts
# @File Name     : file_lesson1.py
# @Author        : liushuangdan 
# @Date          : 2021/1/22 16:17
# @IDE           : PyCharm

capital_letters = []
for i in range(26):
    num = 65 + i
    capital_letters.append(u"%c" % num)
print(capital_letters)
"""
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
"""