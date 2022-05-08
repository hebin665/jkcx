info = {"name":"班长","id":100,"sex":'f',"address":"中国北京"}
print(info["name"])
print(info["address"])
# 如果使用这种方式访问不存在的键，会报错 KeyError错误
# print(info["age"])
# 当不确定键存不存在时候，使用get方法，get方法会返回默认值None
print(info.get("age"))
# 如果设置了默认值，返回的是默认值
print(info.get("age",18))