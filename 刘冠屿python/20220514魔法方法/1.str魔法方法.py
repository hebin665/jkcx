
class Hero(object):
    def __init__(self,name,skill,hp,atk,arrmor):
        self.name = name
        self.skill =skill
        self.hp = hp
        self.atk = atk
        self.arrmor = arrmor

    # 该方法是魔法方法，在输出这个对象时候会被调用到，这个方法需要return一些数据
    def __str__(self):
        return "英雄%s:生命值:%d,攻击力:%d,护甲值：%d"%(self.name,self.hp,self.atk,self.arrmor)

taidamier = Hero("泰达米尔","旋风斩",2600,450,200)
gailun = Hero("盖伦","大宝剑",4200,260,400)

print(taidamier)
print(gailun)
