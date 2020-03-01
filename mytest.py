# -*- coding: utf-8 -*-
# project: vip5
# author : Gavin Jiang
# time   : 2020/2/29 16:52
# file   : mytest.PY

# a = 2
# b = 2.5
# c = 'happy'
# d = "let's go"
# print(a,b,c,d)

# 为变量e从键盘接收数值
# e = input('请输入你的值：')
# print(e)

# 为两个变量输入
# f,g = input('请为两个数输入，并用逗号分隔').split(',')
# print(f,g,type(f),type(g))

# 格式化输出
# print(("%d,%f,%s")%(a,b,c))

# format输出
# print(('a={},b={},c={}').format(a,b,c))

# 列表
# a = [1,2,3,4,5,6,7,8,9]
# print(a[2:7:2])
# print(a[:5])

# 元组
# a = (1,2,3,4,5,6,7,8,9)
# print(a[-3])
# print(a[3:8:2])

# 类型转换
# a = '5'
# print(int(a))
# print(list(range(5)))
# print(tuple(range(5)))
# print(list(range(1,9,2)))

# 逆序存放：s.reverse()---改变原来元组的值   该函数无返回值
# a = [1,2,3,4,5,6,7,8,9]
# a.reverse()
# print(a)

# 排序存放：s.sort()---------改变原来元组的值组的值    该函数无返回值
# a = [1,3,2,4,5,6,7,8,9]
# a.sort()
# print(a)

# 排序：sorted(s)---------不改变原来元组的值，只返回一个排序结果  该函数有返回值
# a = [1,3,2,4,5,6,7,8,9]
# b = sorted(a)
# print(b)

# 插入：s.insert(n,m)-----在某一位置(s[n]前面)插入该值m   该函数无返回值
# a = [1,3,2,4,5,6,7,8,9]
# b = a.insert(3,22)
# print(b)

# 追加：s.append(n)-------在该元组末尾追加n   该函数无返回值
# a = [1,3,2,4,5,6,7,8,9]
# a.append(11)
# print(a)

# 连接两个列表：m.extend(n) ---将m和n两个列表连接  该函数无返回值
# m = [1,2,3,4,5]
# n = [6,7,8,9,]
# m.extend(n)
# print(m)

# 删除指定元素：m.pop(n) ------删除m[n]并返回该值
# a = [1,3,2,4,5,6,7,8,9]
# b = a.pop(3)
# print(a)


# 删除指定元素第一次出现的值：m.remove(n) –将第一次出现的元素n删除   该函数无返回值
a = [1,3,1,4,1,6,7,8,9]
a.remove(1)
print(a)

# 返回该值在列表中出现的次数：m.count(n) –返回元素n在列表中出现的次数  该函数有返回值
# a = [1,3,1,4,1,6,7,8,9]
# b = a.count(1)
# print(b)

# 返回列表中元素最大值：max(s) 该函数有返回值
# a = [1,2,3,4,5,6,7,8,9]
# b = max(a)
# print(b)

# 返回列表中元素最小值：min(s) 该函数有返回值
# a = [1,2,3,4,5,6,7,8,9]
# b = min(a)
# print(b)

# 长度：len(s) ---返回列表元素的个数    该函数有返回值
# a = [1,3,1,4,1,6,7,8,9]
# b = len(a)
# print(b)

# 删除：del s[n] ----删除s[n]，n为下标
# a = [1,2,3,4,5,6,7,8,9]
# del a[2]
# print(a)

# 获得元素的下标：s.index(n) -------得到元素n在列表中的下标    该函数有返回值
# a = [1,2,3,4,5,6,7,8,9]
# b = a.index(8)
# print(b)

# 清空列表：s.clear() --------清空列表   该函数无返回值
# a = [1,2,3,4,5,6,7,8,9]
# a.clear()
# print(a)

# in 和 not in ---用来检查是否在列表中




