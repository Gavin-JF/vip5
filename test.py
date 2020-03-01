# -*- coding: utf-8 -*-
# project: Testing
# author : Gavin Jiang
# time   : 2020/3/1 17:14
# file   : test.PY

# 小技巧：ctrl+鼠标右键  点到函数方法上可以看到原代码，可以看该函数是否有返回值
# 练习：
# 列表[11,13,5,7,0,56,23,34,72]，
# 求该列表中的最大值，最小值及列表中一共有几个元素
# 获取56元素在列表的位置
# 追加元素7
# 删除元素0
# 排序列表（由大到小）
# 将列表[66,67,68]与原列表组合

lists = [11,13,5,7,0,56,23,34,72]
# 求最大值  有返回值
d = max(lists)
print(d)
# 求最小值  有返回值
x = min(lists)
print(x)
# 求列表元素的个数  有返回值
g = len(lists)
print(g)
# 求指定元素的位置  有返回值
index = lists.index(56)
print(index)
# 追加指定元素    无返回值
lists.append(7)
print(lists)
# 删除指定元素    无返回值
lists.remove(0)
print(lists)
# 排序列表(由大到小)    无返回值
lists.sort(reverse=True)
print(lists)
# 将列表[66,67,68]与原列表组合   无返回值
list1 = [66,67,68]
lists.extend(list1)
print(lists)