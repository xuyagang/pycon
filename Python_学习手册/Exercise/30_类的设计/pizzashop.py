from employee import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    # 类函数的参数可以是外部变量
    def order(self, server):
        print(self.name, 'orders from', server)
    def pay(self, server):
        print(self.name, 'pays for item to', server)

class Oven:
    def bake(self):
        print('oven bakes')

class PizzShop:
    def __init__(self):
        # 构造函数将导入的类实例化并将其嵌入
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()
    
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    scene = PizzShop()
    scene.order('Homer')
    print('...')
    scene.order('shaggy')