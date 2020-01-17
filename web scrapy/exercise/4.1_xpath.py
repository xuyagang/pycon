from lxml import etree

text = ''' <div> <Ul> <li class="item-O"><a href=”linkl. html”>first item</a><lli> 
<li class=”item-1”><a href=”link2.html”>second item</a><lli> <li class=”item-inactive” >
<a href="link3.html”>third item</a></h> <li class=”item-1”><a href="link4.html'’>fourth 
item</a><lli> <li class＝” item－口”＞＜a hre于＝”links . html”＞fi干th item</a> </ul> </div> '''

# 初始化，构成了一个XPath解析对象
# etree可以自动修正HTML文本
html = etree.HTML(text)
# 输出修正后的HTML文本
result = etree.tostring(html)
print(result.decode('utf-8'))
# 修正后li节点补全，自动添加了body,html节点

# # 也可以直接读取文本文件进行解析
html = etree.parse('./exercise/test.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
# 多了一个 DOCTYPE 的声明，不过对解析无任何影响
'''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
<html><body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </li></ul>
 </div></body></html>
'''


# 用双斜杠 // 开始的规则来选取所有符合要求的节点
html = etree.parse('./exercise/test.html', parser=etree.HTMLParser())
result = html.xpath('//*')
# 返 回形式是一个列表，每个元素是element 类型,其后跟了节点的名称，如 html、 body、 div 
print(result)
# 指定节点
print(html.xpath('//li'))


# 通过/ 或 // 可查找元素的字节点或子孙节点
# / 用于选择子节点，选择li的所有直接a子节点
html = etree.parse('./exercise/test.html', parser=etree.HTMLParser())
result = html.xpath('//li/a')
print(result)
# 获取所有子孙节点，就可以使用 //
print(html.xpath('//ul//a'))


# 父节点用 .. 来实现
html = etree.parse('./exercise/test.html', parser=etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

# 属性匹配
# []中@ 加属性
# 选取class为item-0的li节点，可这样实现
result = html.xpath('//li[@class="item-0"]')
print(result)

# 文本获取
# text方法获取节点中的文本
result = html.xpath('//li[@class="item-0"]/text()')
print(result)
'''
以上方法获取不到预期的文字， / 的含义是获取直接字节点，很明显li的直接子节点都是ａ节点，文本都是在
a节点内，这里匹配到的是被修正的li节点内的换行符
'''

# 如果要获取li节点内的文本，有两种方式：
# 第一种是选取a节点在获取文本
# 第二种是使用 // 
'''
获取子孙节点内部的所有文本，用 //text(),但可能会夹杂一些换行符等特殊字符
如果要获取特定子孙节点下的文本，可以线获取节点，然后调用text()
'''

# 节点属性获取使用 @ ,以列表的形式返回
html = etree.parse('./exercise/test.html', parser=etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)

# 属性多值匹配，使用 contains函数
# 某些节点的某个属性可能有多个值
text = '''
<li class="li li-first"><a href＝”link.html">first item</a></li> 
'''
html = etree.HTML(text)
# li 的class属性有两个值，使用此方法无法匹配
result = html.xpath('//li[@classs="li"]/a/text()')
print(result)

# 使用contains函数改写
# contains(属性名称，属性值)
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)

# 多属性匹配
# 多个属性通过and连接放与方括号中
# 我们可能还遇到一种情况，就是根据多个属性确定一个节点，需要匹配多个属性
text = '''<li class=”li li-first" name="item"><a href=”link.html” >first item</a></li> '''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)


# 按序选择
# 中括号中传入索引
    # 数字:顺序第几个
    # last()：最后一个
    # last() - 2 : 倒数第三个
    # position()< 4 ： 位置小于4的
# 还有很多xpath函数，可查阅相关文档
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)


# 节点轴选择
# xpath提供多种节点轴选择方法，包括选择子元素，兄弟元素，父元素，祖先元素等
# 名称后跟 :: 然后是节点选择器
# 选取所有祖先，使用 * （html,body,div,ul）
result = html.xpath('//li[1]/ancestor::*')
print(result)
# 选择指定类型的祖先, :: 后加类型
result = html.xpath('//li[1]/ancestor::div')
print(result)
# 调用attribute轴，获取属性值
result = html.xpath('//li[1]/attribute::*')
print(result)
# 调用child轴，获取直接子节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
# 调用descendant轴，获取子孙节点
result = html.xpath('//li[1]/descendant::span')
print(result)
# 调用following轴，获取当前节点之后的所有节点
result = html.xpath('//li[1]/following::*[2]')
print(result)
# 获取当前节点之后的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)