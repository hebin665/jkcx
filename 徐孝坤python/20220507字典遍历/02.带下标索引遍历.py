list1 = ["a","b","c"]
i = 0
for item in list1:
    print(i,item)
    i+=1

# enumerate()函数用于将可迭代的序列（列表，元组，字符串）
# 转为带下标的索引序列，一般使用在for循环中
for index,value in enumerate(list1):
    print(index,value)

# 输出字典中每个元素对应的下标及元素
dic = {"name":"小明","age":18}
for index,value in enumerate(dic.items()):
    print(index,value)