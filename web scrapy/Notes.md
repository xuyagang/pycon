[TOC]

## 第二章 爬虫基础

### 2.1   http基本原理

- URI的全称为 Uniform Resource Identifier，即统一资源标志符
- URL 的全称为 Universal Resource Locator，即统一资源定位符
  - 通过一个链接，我们便可以从互联网上 找到这个资源，这就是 URL/URI
-  URN全称为 Universal Resource Name，即统一资 源名称
  - 以唯一标识这本书，但是没有指定到哪里定位这本书，这就是 URN
- URN 用得非常少，所以几乎所有的 URI 都是 URL

- 超文本（hypertext）

  - 在浏览器里看到的网 页就是超文本解析而成的
  - 浏览器Elements 选项卡即可看到当前网页的源代码，这些源代码都是超文本

- HTTP和HTTPS

  - URL 的开头会有 http 或 https，这就是访问资源需要的协议类型
    - 还会看到ftp、sftp、 smb 开头的 URL，它们都是协议类型
  - HTTP 的全称是 Hyper Text Transfer Protocol，中文名叫作==超文本传输协议==，用于从网络到本地浏览器的传动协议，保证高效而准确的传输
    - HTTP 由万 维网协会（ World Wide Web Consortium ）和 Internet 工作小组 IETF ( Internet Engineering Task Force ) 共同合作制定的规范，目前广泛使用的是 __HTTP 1.1 __ 版本
  - HTTPS 的全称是 Hyper Text Transfer Protocol over Secure Socket Layer
    - 以安全为目标的 HTTP 通道，简单讲是 HTTP 的安全版， 即 HTTP 下加入 SSL 层，简称为 HTTPS
    - HTTPS 的安全基础是SSL，因此通过它传输的内容都是经过 SSL加密的，主要作用:
      1. 建立一个信息安全通道保证信息安全
      2. 确认网站的真实性，凡是使用了 HTTPS 的网站，都可以通过点击浏览器地址栏的锁头标志来 查看网站认证之后的真实信息，也可以通过 CA 机构颁发的安全签章来查询。

- HTTP请求过程

  - 输入一个 URL，回车之后浏览器向网站所在的服务器发送了一个请求，网站服务器接收到这个请求后进行处理和解析，然后返 回对应的响应，接着传回给浏览器，响应里包含了页面的源代码等内容，浏览器再对其进行解析，便 将网页呈现了出来

    - 浏览器的network是监听组件，可以显示访问当前请求网页时所有的网络请求和响应

      ![000](D:\project\pycon\web scrapy\img\000.png)

      - name:请求的名称
      - status:响应的状态码
      - type:文档类型
      - Initiator:请求源
      - size:资源大小
      - Time:发起请求到获取响应所用的总时间
      - waterfall:请求的可视化瀑布流

  - 点击每个条目，会看到单个请求的详细信息

    ![001](D:\project\pycon\web scrapy\img\001.png)

    - request URL:请求的url
    - request method:请求的方法
    - status code:响应状态码
    - remote address：远程服务器的地址和端口
    - request headers:请求头包含很多信息
      - 浏览器标识、cookies、Host等

  - 请求：请求方法、请求网址、请求头、请求体

    - get请求的参数包含在url中，数据可以在url中看到

    - post请，求大多是在表单提交时发起，post请求的url不会包含这些数据，数据包含在请求体中通过表单传播

    - get请求提交的数据最多只有1024字节，post方式没有限制

    - 常用的请求方法时get和post,还有其他的请求方法：

      ![002](D:\project\pycon\web scrapy\img\002.png)

  - 请求头

    用来说明服务器要使用的附加信息，比较重要的有cookie、referer、user-agent等

    - accept:请求报头域，用于指定客户端可接受哪些类型的信息

    - Accept-Language：指定客户端可接受的语言类型

    -  Accept-Encoding ：指定客户端可接受的内容编码

    - Host：用于指定请求资源的主机 IP 和端口号，其内容为请求 URL 的原始服务器或网关的位 置。 从 HTTP 1. l 版本开始，__请求必须包含此内容__

    - Cookie ：也常用复数形式 Cookies,是网站为了辨别用户进行会话跟踪而存储在用户本地 的数据。 它的主要功能是维持当前访问会话

      > Cookies 里有信息标识了我们所对应的服务器 的会话，每次浏览器在请求该站点的页面时，都会在请求头中加上 Cookies 并将其发送给服 务器，服务器通过 Cookies 识别出是我们自己，并且查出当前状态是登录状态，所以返回结 果就是登录之后才能看到的网页内容。 

    - Referer：此内容用来标识这个请求是从哪个页面发过来的，服务器可以拿到这一信息并做相 应的处理，如做来源统计、防盗链处理等

    - User-Agent：简称 UA，它是一个特殊的字符串头，可以使服务器识别客户使用的操作系统 及版本、 浏览器及版本等信息

    - Content-Type：也叫互联网媒体类型（ Internet Media Type ）或者 MIME 类型，在 HTTP 协议 消息头中，它用来表示具体请求中的媒体类型信息

  - 请求体

    - 请求体－般承载的内容是 POST请求中的表单数据，而对于 GET请求，请求体则为空

      ![003](D:\project\pycon\web scrapy\img\003.PNG)

    - 如果要构造 POST 请求，需要使用正确的 Content-Type，并了解各种请求库的各个参 数设置时使用的是哪种 Content-Type， 不然可能会导致 POST 提交后无法正常响应。

  - 响应

    1. 响应状态码（request status code）

       - 200---正常
       - 404---页面未找到
       - 500---服务器内部发生错误

       ![004](D:\project\pycon\web scrapy\img\004.PNG)

       ![005](D:\project\pycon\web scrapy\img\005.PNG)

    2. 响应头 (request headers)

       - date---响应产生的时间
       - last-modified---指定资源的最后修改时间
       - content-encoding---指定响应内容的编码
       - server---服务器信息
       - content-type---文档类型，指定返回数据类型时什么
       - set-cookie---设置cookies,响应头中的set-cookie告诉浏览器要将此内容放在cookies中，下次请求携带cookie请求
       - expires---指定响应过期时间，可以使代理服务器或浏览器将加载的内容更新到缓存中，再次访问时直接从缓存加载，降低服务器负载，缩短加载时间

    3. 相应体 (request body)

       最重要的当属响应体内容了

### 2.2   网页基础

- 网页的组成

  - HTML --- 骨架

    HTML 是用来描述网页的一种语言， 其全称叫作 Hyper Text Markup Language，即超文本标记语言

    - 开发者模式下，elements选项卡可以看到源代码

  - CSS --- 肌肉

    全称叫作 Cascading Style Sheets，即层叠样式表

    -  “样式”指网页中文字大小、 颜色、元 素间距、排列等格式

  - Javascript --- 皮肤

    JavaScript，简称 JS， 是一种脚本语言。 HTML 和 css 配合使用， 提供给用户的只是一种静态信 息，缺乏交互性。 我们在网页里可能会看到一些交互和动画效果，如下载进度条、提示框、 轮播图等， 这通常就是 JavaScript 的功劳

- 选择器

  ![006](D:\project\pycon\web scrapy\img\006.PNG)

  ![007](D:\project\pycon\web scrapy\img\007.PNG)

### 2.3   爬虫的基本原理

爬虫概述：获取网页、提取信息、保存数据、自动化程序

能抓的数据：html源码、json字符串、二进制数据（图片、视频、音频）

> 二进制数据保存成对应文件名即可

- javascript

  有时候，我们在用 时lib 或 requ曰“抓取网页时，得到的游、代码实际和浏览器中看到的不一样,现在网页越来越多地采用 Ajax、前端模块化工具来构建，整个网页可 能都是由 JavaScript 渲染出来的，也就是说原始的 HTML代码就是一个空壳， 对于这样的情 况，我们可以分析其后台 Ajax 接口，也可使用 Selenium、 Splash这样的库来实现模拟 JavaScript渲染。 

### 2.4   会话和cookies

- 静态网页和动态网页
- 

























