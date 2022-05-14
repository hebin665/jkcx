class Hero(object):
    def __init__(self,name):
        self.name = name

    # 该方法是魔法方法，在对象被删除时候执行
    def __del__(self):
        print("del方法被调用")
        print("%s被删除"%self.name)


taidamier = Hero("泰达米尔")
print("%d被删除1次"%id(taidamier))
del(taidamier)
print("--"*10)
gailun = Hero("盖伦")
gailun1 = gailun
gailun2 = gailun
print("%d被删除1次"%id(gailun))
del(gailun)

print("%d被删除1次"%id(gailun1))
del(gailun1)
print("%d被删除1次"%id(gailun2))
del(gailun2)

# 当有变量保存了一个对象的引用时，此对象的引用计数会加1
# 当使用del删除变量指向的对象时，会减少对象的引用计数
# 当对象的引用计数为0时候, 对象才会被真正删除
