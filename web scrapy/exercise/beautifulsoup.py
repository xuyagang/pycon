'''
借助网页的结构和属性等特性来解析网页
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.string)

# prettify()方法可以把要解析的字符串以标准的缩进格式输出，输出结果里面包含
# body和html节点，对于不标准的HTML字符串Beautifulsoup会自动更改格式，不是
# 在prettify中完成，在初始化的时候完成
# .string 可以获取文本

# 节点选择器
    # 直接调用节点可以选择节点元素
html ="""<html><head><title>The Dormouse ’ s story</title></head> <body> 
<p class=”title” name=”dromouse”><b>The Dormouse ’ s story</b></p> <p class
＝飞tory”＞Once upon a time there were three little sisters; and their names
 were <a href＝”http : //example.com/elsie” class="sister” id＝”linkl＂＞＜ ！
  … Elsie 一＞＜la>, <a href＝”http://example.com/lacie” class＝飞ister" id=”link2" >
  Lacie< /a> and <a href=“http://example.com/tillie” class=”sister" id="link3”>
  Tillie< la>; and they lived at the bottom of a well. </p> <p class=”story”) ...</p>"""
soup = BeautifulSoup(html, 'lxml')
# .后的方法不带括号
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
# prettify()   需要加括号调用
print(soup.prettify())
# 获取节点名称
# 利用name属性获取节点的名称
print(soup.title.name)
# 利用attrs获取所有属性，返回字典类型
print(soup.p.attrs)
# 对于attrs获取的字典结果调用属性名就可以获取属性值了
print(soup.p.attrs['name'])
# 也可简写成如下格式
print(soup.p['name'])
print(soup.p['class'])
# 返回结果有的时字符串，有的是列表，实际处理过程中要注意判断类型


# 获取内容
# 利用string属性获取节点元素包含的文本内容
print(soup.p.string)

# 嵌套选择
# 每一个返回结果是bs4.element.Tag类型，可以继续调用进行选择
print(soup.head.title)


# 关联选择
# 不能一步得到目标元素，需要先选中某个节点，然后以它为基准在选择它的
# 子节点，父节点，兄弟节点等
    # 字节点和子孙节点
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')
print(soup.p.contents)
# 返回列表形式，包含文本，节点，列表中的元素都是p节点的直接子节点
# contents属性得到的结果是直接子节点的列表

# 可以调用children得到相应的结果
print(soup.p.children)
# 返回结果是生成器类型
for i, child in enumerate(soup.p.children):
    print(i,child)

# 子孙节点的获取可调用descendants属性       descendants
soup = BeautifulSoup(html, 'lxml')
print(soup.p.descendants)
# descendants会递归查询所有子节点，得到所有的子孙节点
# 父节点和祖先节点，可以调用parent属性,选择直接父节点
print(soup.a.parent)

# 调用parents获取祖先节点

# 调用parents
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

# 兄弟节点
# 获取同级节点
html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
soup = BeautifulSoup(html, 'lxml')
# 获取节点的下一个和上一个元素
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
# 返回所有前面或后面的兄弟节点生成器
print('Next Sibling', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))


# 提取信息
# 关联元素节点信息（文本、属性）获取
# 直接调用string、attrs等属性获取文本和属性
# 得到多个节点的生成器可以转为list然后取出某个元素

# 方法选择器
# 前面的方法是通过属性来选择，速度快
# 如果需要做复杂的查询方法，可以采用查询方法 find_all(), find()函数
# find_all（）函数
    # 根据节点名来查询元素
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
# 每个元素是bs4.element.Tag类型
print(type(soup.find_all(name='ul')[0]))
# 都是Tag类型，以然可以进行嵌套查询
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))

    # 根据节点属性来查询
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# 得到的结果是列表形式
print(soup.find_all(attrs={'id': 'list-1'}))
# 对于常用属性我们可以不用传入 attrs 属性，直接传入属性

print(soup.find_all(id='list-1'))
# 由于class是python的关键字，所以后面需要加下划线，即 class_ = 'element'
print(soup.find_all(class_='element'))

    # text参数匹配节点的文本，可传入字符串或正则表达式
    # 结果返回所有的匹配正则表达式的节点文本组成的列表
import re
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
print('#'* 10)
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))


# find 方法
# find:返回单个元素，第一个匹配的元素
# find_all:返回所有匹配的元素列表
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_ = 'list'))

# 使用 css 选择器时，只需要调用 select（）方法，传人相应的 css 选择器即可
# 获取属性
# 直接传入中括号和属性名，以及通过 attrs 属性获取属性值，都可以
for ul in soup.select('ul'):
    print(ul.attrs['id'])
    # 等价于
    print(ul['id'])

# 文本
# 可以用string属性，也可以使用get_text()方法
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)




