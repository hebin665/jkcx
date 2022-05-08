dic = {"name":"小明","age":18}
# 1.遍历字典中的key
for key in dic:
    print(key)

# 2.遍历字典中的key
for key in dic.keys():
    print(key)

# 3.遍历字典中的value
for value in dic.values():
    print(value)

# 4.遍历字典中的每一项
for item in dic.items():
    print(item)

# 5.遍历字典中的每一项,使用两个值来接收
for key,value in dic.items():
    print(key,value)