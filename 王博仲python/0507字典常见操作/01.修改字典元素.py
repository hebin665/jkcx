info = {"name": "班长", "id": 100, "sex": "f", "address": "中国北京"}
print(info)
new_id = input("输入新学号")
info["id"] = int(new_id)
print("修改后的id值：%d" % info["id"])
print(info)
# 当遇到没有的键，会把键值对加入到字典中
info["age"] = 11
print(info)



