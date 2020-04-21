class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instances via inheritance of __str__, coded here; displays
    instance attrs only; self is the instance of lowest class;
    use __X names to avoid clashing with client's attrs
    """
    def __str__(self):
        # 所有派生自该类的实例在打印的时候会调用该方法
        return 'Instance of %s, address %s:\n%s' %(
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' %(attr, self.__dict__[attr])
        return result
        
if __name__ == '__main__':
    class Spam(ListInstance):
        def __init__(self):
                self.data1 = 'food'
    x = Spam()
    print(x)
    print(repr(str(x)))