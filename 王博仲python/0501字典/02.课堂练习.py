dict = {"k1":"v1","k2":"v2","k3":"v3","k4":"v4"}
# 1.获取k2对应的值
print(dict["k2"])
# 2.获取k6对应的值，不报错，输出None
print(dict.get("k6","None"))