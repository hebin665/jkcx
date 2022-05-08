# 1.len()计算字典的元素个数
dic = {"k1":"v1","k2":"v2","k3":"v5"}
print(len(dic))

# 2.get()返回字典中键对应的值，如果键不存在，那么返回默认值None（如果定义了默认值，返回的是定义好的默认值）
print(dic.get("k1"))
print(dic.get("k6"))
print(dic.get("k6",18))


# 3.keys() 返回字典中所有的键组成的列表
dic = {"name":"小明","age":7,"class":"First"}
print(dic.keys())

#4.values() 返回字典中所有的值组成的列表
print(dic.values())

# 5. items()返回字典中(键,值)元组组成的列表
print(dic.items())

# 6.popitem() 删除并返回字典中的最后一个键值对(元组类型)
print(dic.popitem())
print(dic)

# 7.update() 把字典中的元素更新到另外一个字典中
dic1 = {'name': '小明', 'age': 7}
dic2 = {'sex': 'f'}
dic1.update(dic2)
print(dic1)

# 8.clear() 把字典中的所有元素进行清空
dic1.clear()
print(dic1)
