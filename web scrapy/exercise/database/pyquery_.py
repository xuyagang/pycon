# pyquery
# 初始化_字符串初始化
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
# 初始化字符串
doc = pq(html)
# 连接css选择器
print(len(doc('li')))

# URL初始化
# 初始化的参数不仅可以以字符串的形式传递，还可以传入网页的url
from pyquery import PyQuery as pq
doc = pq(url='http://cuiqingcai.com',encoding='utf-8')
print(doc('title'))

# 文件初始化
# 还可以传递本地的文件名， 此时将参数指定为 filename 即可
from pyquery import PyQuery as pq
# doc = pq(filename='demo.html')

# 基本 css 选择器
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
''' 
from pyquery import PyQuery as pq
doc = pq(html)
# 选取id为container的节点，然后选取class为list的节点内部的li
print('css 选择器',doc('#container .list li'))
print(type(doc('#container .list li')))


# 子节点
items = doc('.list')
print('items:', items)
lis = items.find('li')
print('lis:',lis)
# 如果要选取子节点中符合条件的节点，可以使用children()方法
# 选出子节点中 class 为 active 的节点
lis = items.children('.active')
print('children:', lis)

# 父节点
# 使用parent()获取某个节点的父节点
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
items = doc('.list')
# 获取直接父节点 parent()
container = items.parent()
print('container:', container)
print(type(container))


# 获取祖先节点 parents()
# parents（）方法会返回所有的祖先节点
parents = items.parents()
print('parents:',parents)
# 如果要选择某个祖先节点，可以像parents()传入css选择器
parent = items.parents('.wrap')
print('parent:', parent)

# 兄弟节点
# 获取兄弟节点可使用siblings()方法
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.list .item-0.active')
print('siblings:',li.siblings())
# 获取特定的siblings,可以像其传入css选择器
# 先获取class='item-0'且class='active'的节点
li = doc('.list .item-0.active')
print('li:', li)
# 获取特定兄弟节点
print(li.siblings('.active'))


# 5.遍历
# 对于单个节点
doc = pq(html)
li = doc('.item-0.active')
print('li:', li)
print(str(li))
# 对于多个节点的结果，需要遍历来获取,需要调用items()方法
# 调用items()方法后，会得到一个生成器，遍历会得到节点对象
doc = pq(html)
# 生成器对象-generator
lis = doc('li').items()
print(type(lis))
for li in lis: 
    print(li, type(li))

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
# 调用attr()方法获取属性
print(a.attr('href'))
# 调用attr属性获取属性
print(a.attr.href)

# 选中的是单个多个元素时
a = doc('a')
print("#" * 9)
print(len(a))
print(a.attr('href'))

# 选中的是多个多个元素时
# 多个元素调用attr()方法时，返回一个结果，得到第一个节点属性
# 如果要获取所有 a 节点属性，需要用遍历

# 使用pyquery选择得到的节点不管是单个还是多个，
# 类型都是<class 'pyquery.pyquery.PyQuery'>。

# 如果得到的是多个节点的对象，则需要进行遍历来获取单个节点对象，
# 这时要注意不能直接遍历多个节点对象，而是要调用多节点对象的items()方法
for item in a.items():
    print(item.attr.href)


# 获取文本
# 使用text()函数实现,获取节点内部文本
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
a = doc('.item-0.active a')
print(a.text())

# 获取节点html文本,使用 html()方法
li = doc('.item-0.active')
print('li:', li)
print(li.html())
print(li.text())
print(type(li.text()))

# 如果选中多个节点，text() 或 html() 会返回什么内容？
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('li')
print('li_html:', li.html())
print('li_text:', li.text())
# html()方法返回了第一个li节点的内部HTML文本
# text()方法返回了所有的li节点内部的纯文本，之间用空格割开，即是一个字符串


# 节点操作
# 对某个节点添加一个class,移除某个节点等
# 节点方法较多，举几个典型
    # addClass 和 removeClass ,动态改变节点的class属性
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print('原始的：',li)
li.removeClass('active')
print('移除的：',li)
li.addClass('active')
print('增加的：',li)
'''
原始的： <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
移除的： <li class="item-0"><a href="link3.html"><span class="bold">third item</span></a></li>
增加的： <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
'''

    # attr, text, html
    # attr() 对属性操作
    # text() 和 html() 改变节点内部内容
html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
# 修改属性(属性名，属性值)，添加属性
li.attr('name','link')
print(li)
# 修改节点内部内容
li.text('changed item')
print(li)
# html()方法传入HTML文本后，li节点内部又变为传入的html了
li.html('<span>changed item</span>')
print(li)

# remove
# 移除操作
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())

# 移除p节点内的文本
# 选择p节点，然后移除
wrap.find('p').remove()
print(wrap.text())
# 其他类似的方法：append(), empty(), prepend()


# 伪类选择器
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print('伪类选择器：')
# 第一个节点
li = doc('li:first-child')
print(li,end='\n')
# 最后一个节点
li = doc('li:last-child')
print(li)
# 第二个li节点
li = doc('li:nth-child(2)')
print(li)
# 第三个之后的
li = doc('li:gt(2)')
print(li)
# 偶数位置
li = doc('li:nth-child(2n)')
print(li)
# 包含特定文本的
li = doc('li:contains(second)')
print(li)