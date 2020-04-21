def handler():
    '''use global for state'''
    
widget = Button(text='spam', command=handler)


# 类的绑定方法的使用
class Mywidget:
    def handler(self):
        '''use global for state'''
    def makewidgets(self):
        b = Button(text='spam', command=self.handler)