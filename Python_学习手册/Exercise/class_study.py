class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job 
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1+percent))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


# 扩展方法——不好的方式
class Manager1(Person):
    def giveRaise(self, percent, bonus=.10):
        # 不好的方式是复制和粘贴person中的giveraise的代码
        self.pay = int(self.pay * (1 + percent + bonus))


# 扩展方法——好的方式
class Manager(Person):
    def giveRaise(self, percent, bonus=0.10):
        # 使用扩展的方式来直接调用最初的方式
        Person.giveRaise(self, percent + bonus)





if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue', job='dev', pay=10000)
    print(bob)
    sue.giveRaise(.01)
    print(sue)