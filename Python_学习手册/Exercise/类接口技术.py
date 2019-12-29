class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        # 超类中可以有未定义的方法，可用于调用继承类中的方法
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in Replacer.method')
    
class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('Ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
        print('\nProvider ...')
        x = Provider()
        x.delegate()