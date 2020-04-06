[TOC]

## 第二章 爬虫基础

### 2.1   http基本原理

- URI的全称为 Uniform Resource Identifier，即统一资源标志符
- URL 的全称为 Universal Resource Locator，即统一资源定位符

  - 通过一个链接，我们便可以从互联网上 找到这个资源，这就是 URL/URI
- URN全称为 Universal Resource Name，即统一资 源名称

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

  > 一个.html 文件，然后把它放在某台具有固定公网 IP 的主机上， 主机上装上 Apache 或 Nginx 等服务器，这样这台主机就可以作为服务器了 ， 其他人便可 以通过访问服务器看到这个页面，这就搭建了一个最简单的网站
  >
  > 
  >
  > 网页的内容是 HTML 代码编写的，文字、图片等内容均通过写好的 HTML 代码来指定， 这 种页面叫作静态网页。 它加载速度快，编写简单，但是存在很大的缺陷，如可维护性差 ，不能根据 URL灵活多变地显示内容等
  >
  > 
  >
  > 动态网页可以动态解析 URL 中参数的变化，关联数据库井动态呈现不同的页面内容，非常灵活多变

  按照一般的逻辑来说，输入用户名和密码登录之后，肯定是拿到了一种类似凭 证的东西，有了它，我们才能保持登录状态，才能访问登录之后才能看到的页面。 其实它就是会话和 Cookies 共同产生的结果

- 无状态HTTP

  >  HTTP 的无状态是指 HTTP 协议对事务处理是没有记忆能力的，也就是说服务器不知道客户端是 什么状态,当我们向服务器发送请求后，服务器解析此请求，然后返回对应的响应，服务器负责完成 这个过程，而且这个过程是完全独立的，服务器不会记录前后状态的变化，也就是缺少状态记录。 这 意味着如果后续需要处理前面的信息，则必须重传，这导致需要额外传递一些前面的重复请求，才能 获取后续响应，然而这种效果显然不是我们想要的。 为了保持前后状态，我们肯定不能将前面的请求 全部重传一次，这太浪费资源了，对于这种需要用户登录的页面来说，更是棘手
  - 两个用于保持 HTTP 连接状态的技术就出现了，它们分别是会话和 Cookies。 会话在服务端， 也就是网站的服务器，用来保存用户的会话信息； Cookies 在客户端，也可以理解为浏览器端，有了 Cookies，浏览器在下次访问网页时会自动附带上它发送给服务器，服务器通过识别 Cookjes 并鉴定出 是哪个用户，然后再判断用户是否是登录状态，然后返回对应的响应。 

  > 可以理解为 Cookies 里面保存了登录的凭证，有了它，只需要在下次请求携带 Cookies 发送 请求而不必重新输入用户名、密码等信息重新登录了。 
  >
  > > 在爬虫中，有时候处理需要登录才能访问的页面时，我们一般会直接将登录成功后获取的 Cookies 放在请求头里面直接请求，而不必重新模拟登录。 
  - 会话

    会话，其本来的含义是指有始有终的一系列动作／消息。__Web 中，会话对象用来存储特定用户会话所需的属性及配置信息 __

    > 当用户请求来自应用程序的 Web 页时如果该用户还没有会话， 则 Web 服务器将自动创建一个会话 对象。 当会话过期或被放弃后，服务器将终止该会话

  - cookies

    - 会话保持

    Cookies 指某些网站为了辨别用户身份、 进行会话跟踪而存储在用户本地终端上的数据

    > 当客户端第一次请求服务器时，服务器会返回一个请 求头中带有 Set-Cookie 字段的响应给客户端，用来标记是哪一个用户，客户端浏览器会把 Cookies 保 • 存起来。 当浏览器下一次再请求该网站时，浏览器会把此 Cookies 放到请求头一起提交给服务器， “ Cookies 携带了会话 ID 信息，服务器检查该 Cookies 即可找到对应的会话是什么，然后再判断会话来 以此来辨认用户状态。
    >
    > 
    >
    > 在成功登录某个网站时，服务器会告诉客户端设置哪些 Cookies 信息，在后续访问页面时客户端 会把 Cookies 发送给服务器，服务器再找到对应的会话加以判断。 如果会话中的某些设置登录状态的 变量是有效的，那就证明用户处于登录状态，此时返回登录之后才可以查看的网页内容，浏览器再进 行解析便可以看到了。 
    >
    > 如果传给服务器的 Cookies 是无效的，或者会话已经过期了，我们将不能继续访问页面， 此时可能会收到错误的响应或者跳转到登录页面重新登录

    __Cookies 和会话需要配合，一个处于客户端，一个处于服务端，二者共同协作，就实现了 登录会话控制。__

    - 属性结构

      cookies在浏览器application选项面板上

      - name: cookie名称，一旦创建，不可更改
      - value：cookie值，如果值为unicode字符，需要为字符编码，如果值为二进制数据，需要使用base64编码
      - domain: 可以访问cookie的域名（例如，如果设置为.zhihu.com，则所有以 zhihu.com结尾 的域名都可以访问该 Cookie）
      - max age: cookie失效时间，单位为秒，常和expires一起使用，
        - max age 如果为负数，则关闭浏览器时cookie失效
        - max age 如果为正数，则cookie在max age 秒之后失效
      - path: 该cookie的使用路径
        - 如果设置为／path/ ，则只有路径为／path/的页面可以访问该 Cookie
        - 如果设置为人 则本域名下的所有页面都可以访问该 Cookie
      - size: cookie的大小
      - http字段：cookie 的httponly属性
        - 若此属性为 true ，则只有在 HTTP 头中会带有此 Cookie 的信息，而不能通过 document.cookie 来访问此 Cookie。 
      - secure: 该 Cookie 是否仅被使用安全协议传输。 安全协议有 HTTPS 和 SSL 等，在网络上传 输数据之前先将数据加密。 默认为 false

    - 会话cookie和持久cookie

      - 会话 Cookie 就是把 Cookie 放在浏览器内存里，浏览器在关闭之后该 Cookie 即 失效
      - 持久 Cookie 则会保存到客户端的硬盘中，下次还可以继续使用，用于长久保持用户登录状态。 

      __严格来说，没有会话 Cookie 和持久 Cookie 之分，只是由 Cookie 的 Max Age 或 Expires 字段 决定了过期的时间__

- 常见误区

  对 会话来说，除非程序通知服务器删除一个会话，存则服务器会一直保留。 比如，程序一般 都是在我们做注销操作时才去删除会话。 

  > 当我们关闭浏览器时，浏览器不会主动在关闭之前通知服务器它将要关闭，所以服务器根本 不会有机会知道浏览器已经关闭。 之所以会有这种错觉，是因为大部分会话机制都使用会话 Cookie 来保存会话 ID 信息， 而关闭浏览器后 Cookies 就消失了，再次连接服务器时，也就无法找到原来的会 话了。 如果服务器设置的 Cookies 保存到硬盘上，或者使用某种手段改写浏览器发出的 HTTP 请求头， 把原来的 Cookies 发送给服务器， 则再次打开浏览器，仍然能够找到原来的会话 ID， 依旧还是可以保 持登录状态的。 

  恰恰是由于关闭浏览器不会导致会话被删除，这就需要服务器为会话设置一个失效时间，当 距离客户端上一次使用会话的时间超过这个失效时间时，服务器就可以认为客户端已经停止了活动， 才会把会话删除以节省存储空间

### 2.5   代理的基本原理

服务器会检测某个 IP在单位时间内的请求次数，如果超过了这个阔值，就会直接拒绝服务，返 问一些错误信息，这种情况可以称为封 IP

- 基本原理

  代理实际上指的就是代理服务器，英文叫作 proxy server，它的功能是代理网络用户去取得网络信息，它是网络信息的中转站。

  > 设置了代理服务器， 实际上就是在本机和服务器之间搭建了一个 桥， 此时本机不是直接向 Web 服务器发起请求，而是向代理服务器发出请求，请求会发送给代理服务 器，然后由代理服务器再发送给 Web 服务器，接着由代理服务器再把 Web 服务器返回的响应转发给本机 

- 代理的作用
  - 突破门身 IP访问限制，访问一些平时不能访问的站点
  - 访问一些单位或团体内部资惊：比如使用教育网内地址段免费代理服务器，就可以用于对教 育网开放的各类 FTP下载上传，以及各类资料查询共享等服务
  - 提高访问速度：通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同 时也将·其保存到缓冲区中，当其他用户再访问相同的信息时，则直接由缓冲区中取出信息， 传给用户，以提高访问速度
  - 隐藏真实 IP： 上网者也可以通过这种方法隐藏向己的 E， 免受攻击。 对于爬虫来说，我们用 代理就是为了隐藏向身 IP，防止 向身的 IP 被封锁。
- 代理分类
  1. 根据协议
     - FTP代理服务器
       - 主要用于访问 FTP 服务器， 一般有上传、 下载以及缓存功能，端口一般为 21 、 2121 等
     - HTTP代理服务器
       - 主要用于访问网页，一般有内容过滤和缓存功能，端口一般为 80 、 8080、 3128 等。 
     - SSL/TLS代理
       - 主要用于访问加密网站， 一般有 SSL 或 TLS 加密功能（最高支持 128 位加密 强度），端口一般为 443
     - RTSP代理
       - 主要用于访问 Real 流媒体服务器， 一般有缓存功能，端口一般为 554
     - Telnet代理
       - 主要用于telnet远程控制（黑客人侵计算机时常用于隐藏身份），端口一般为 23
     - POP3/SMTP代理
       - 主要用于 POP3/SMTP方式收发邮件， 一般有缓存功能，端口一般为 110/25
     - SOCKS代理
       - 只是单纯传递数据包，不关心具体协议和用法，所以速度快很多， 一般有缓 存功能，端口一般为 1080
       - SOCKS代理协议又分为 SOCKS4和 SOCKS5 ，前者只支持 TCP, 而后者支持 TCP 和 UDP ，还支持各种身份验证机制、服务器端域名解析等。 
  2. 根据匿名程度
     - 高度匿名代理
       - 会将数据包原封不动地转发，在服务端看来就好像真的是一个普通客户端在 访问，而记录的 IP 是代理服务器的 IP
     - 普通匿名代理
       - 会在数据包上做一些改动， 服务端上有可能发现这是个代理服务器，也有一定几 率追查到客户端的真实IP。 
     - 透明代理
       - 不但改动了数据包 还会告诉服务器客户端的真实 IP。 这种代理除了能用缓存技 术提高浏览速度，能用内容过滤提高安全性之外，并无其他显著作用，
     - 间谍代理
       - 指组织或个人创建的用于记录用户传输的数据，然后进行研究、 监控等 目的的代 理服务器。

- 代理设置
  - 网上免费
  - 付费服务
  - ADSL拨号

## 第三章   基本库的使用

### 3.1 urllib

Python 2 中，有 urllib 和 urllib2 两个库来实现请求的发送。 而在 Python 3 中，已经不存在 urllib2 这个库了 ， 统一为 urllib

- urllib 库，它是 Python 内置的 HTTP请求库,包含如下 4个模块
  - request ： 它是最基本的 HTTP 请求模块，可以用来模拟发送请求。 就像在浏览器里输入网挝 然后回车一样，只需要给库方法传入 URL 以及额外的参数，就可以模拟实现这个过程了。 
  - error： 异常处理模块，如果出现请求错误， 我们可以捕获这些异常，然后进行重试或其他操 作以保证程序不会意外终止。
  - parse： 一个工具模块，提供了许多 URL 处理方法，比如拆分、解析、 合并等
  - robotparser：主要是用来识别网站的 robots.txt 文件，然后判断哪些网站可以爬，哪些网站不 可以爬，它其实用得比较少
- 发送请求
  - urlopen()
  - 

### 3.2 requests

- 确保正确安装requests

- 实例

  ```python
  import requests
  
  r = requests.get('https://baidu.com')
  print(type(r))
  # <class 'requests.models.Response'>
  print(r.status_code)
  print(type(r.text))
  print(r.text)
  print(r.cookies)
  # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
  ```

  响应的类型是requests.models.Response，响应体的类型是str,Cookies的类型是RequestsCookieJar

- get请求

  构建一个简单的get请求，链接为`'http://httpbin.org/get'`,该网站会判断客户发起的请求并返回请求信息

  ```
  r = requests.get('http://httpbin.org/get')
  print(r.text)
  >>>
  {
    "args": {},
    "headers": {
      "Accept": "*/*",
      "Accept-Encoding": "gzip, deflate",
      "Host": "httpbin.org",
      "User-Agent": "python-requests/2.19.1"
    },
    "origin": "125.70.77.211, 125.70.77.211",
    "url": "https://httpbin.org/get"
  }
  ```

  发起的get请求，返回结果中包含请求头，url,ip等信息

  对于get请求，如果要附加额外的信息，一般有两种方式：

  - 直接附加到链接中`r = requests.get('http://httpbin.org/get?name=adam&age=22')`

  - 参数方式添加

    ```
    data={
        'name':'adam',
        'age':22
    }
    r = request.get('http://httpbin.org/get',params=data)
    print(r.text)
    >>>
    {
      "args": {
        "age": "22", 
        "name": "adam"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.19.1"
      }, 
      "origin": "125.70.77.211, 125.70.77.211", 
      "url": "https://httpbin.org/get?name=adam&age=22"
    }
    ```

    可以看到链接被自动构造成了之前的格式

    网页返回的实际上是str类型，是json格式的，如果要得到字典格式，可以使用json方法

    返回结果就是字典格式（如果返回结果不是json格式，就会出现json.decoder.JSONDecodeError异常）

    ```
    r.json()
    >>>
    {'args': {'age': '22', 'name': 'adam'},
     'headers': {'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate',
      'Host': 'httpbin.org',
      'User-Agent': 'python-requests/2.19.1'},
     'origin': '125.70.77.211, 125.70.77.211',
     'url': 'https://httpbin.org/get?name=adam&age=22'}
     
    type(r.json())
    >>>
    dict
    ```

- 抓取网页

- 抓取二进制数据

- 添加headers

- post请求

- 响应

   'encoding', 'headers', 'history','json', 'links'，'status_code', 'text', 'url'， 'cookies'

  ```
  requests.codes.ok
  # 内置的请求码
  ```

  - 1开头的——信息性状态吗
  - 2开头的——成功状态码
  - 3开头的——重定向
  - 4开头的——客户端错误码
  - 5开头的——服务端错误码

- 高级用法

  - cookie

    - 可以把cookies设置到headers中

      ```
      Cookie: _ga=GA1.2.1879080799.1543498454; _octo=GH1.1.33263197.1543498454; tz=Asia%2FShanghai; ignored_unsupported_browser_notice=false; _device_id=f95f96fa24bf56d4369ea895b0442d55; has_recent_activity=1; user_session=O1U4N-PfcgxWOt3O3XGwq_T63nfDzOZDK2VB6MZThzu3Zzxe; __Host-user_session_same_site=O1U4N-PfcgxWOt3O3XGwq_T63nfDzOZDK2VB6MZThzu3Zzxe; logged_in=yes; dotcom_user=xuyagang; _gh_sess=Y1g5RTdCMGp5WTBiYkRzaGJXWGsrdFZWNTZsblBKRzIxRHFFYTZHUS93b1B3V0o5SXlSWXloVmZNNFFOR29ibEpFTjNSYkdRbmtJcTJHdWZsYnJuM0krNktFMzBNRnhNR3JYczN6czN5MlBtak5OUXdoN3ZQWFlZUHMrZDNTMk14L1NyQjk3OEhWOWxIL0prc3VBU1htVDJCU1o3Mjh4MGVBZUROVG9CckFmNUorN0lKZWpZNVZJdVdhTVRMc3ZlcldrMmw4amtwTk1sMnZNYytPanpyUT09LS0zeXRQTmgvU0hSYjZRbTFUY0NRQmdRPT0%3D--2b26c6c16630644c2d39e024a1ce14ad903bdc66
      ```

    - 也可以通过cookies参数来设置，需要构造RequestsCookieJar对象，需要分割cookies,相对繁琐

      ```python
      cookies = '_ga=GA1.2.1879080799.1543498454; 
      _octo=GH1.1.33263197.1543498454; tz=Asia%2FShanghai; ignored_unsupported_browser_notice=false; _device_id=f95f96fa24bf56d4369ea895b0442d55; has_recent_activity=1;'
      
      jar = requests.cookies.RequestsCookieJar()
      headers = {
          'Host':url,
          'User-Agent':...,
      }
      for cookie in cookies.split(';'):
          key,value = cookies.split('=',1)
          jar.set(key,value)
      r = requests.get(url,cookies=jar,headers=headers)
      ```

  - 会话维持

    session可以维持一个会话，而不用担心cookies的问题

    ```python
    import requests
    # 请求并设置cookies为123456
    requests.get('http://httpbin.org/cookies/set/number/123456')
    # 随后又请求一次,可以获取当前cookies
    r = requests.get('http://httpbin.org/cookies')
    print(r.text)
    '''
    {
      "cookies": {}
    }
    '''
    
    
    # 我们用session试试
    s = requests.session()
    s.get('http://httpbin.org/cookies/set/number/123456')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)
    '''
    {
      "cookies": {
        "number": "123456"
      }
    }
    '''
    ```

  - 证书验证

    如果一个HTTPS站点，出现证书验证错误页面，可以把 verify参数设置为 False避免这个错误

    ```python
    resp = requests.get('https://www.12306.cn',verify=False)
    >>>
    /usr/lib/python3/dist-packages/urllib3/connectionpool.py:860: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
      InsecureRequestWarning)
    ```

    这样会给出一个警告，建议我们指定证书，可以通过设置忽略警告的方式来屏蔽这个警告

    ```python
    import requests
    from requests.packages import urllib3
    
    urllib3.disable_warnings()
    resp = requests.get('https://www.12306.cn',verify=False)
    print(resp.status_code)
    ```

    或者捕获警告到日志的方式以忽略

    ```python
    import logging
    
    logging.captureWarnings(True)
    resp = resp = requests.get('https://www.12306.cn',verify=False)
    print(resp.status_code)
    ```

    也可以指定一个本地证书用作客户端证书，可以是单个文件或包含两个文件路径的元组

    ```python
    resp = requests.get('https://www.12306.cn', cert=('/path/server.crt','/path/key'))
    ```

    只是演示，需要有crt和key文件，并指定路径，本地的私有证书必须是解密状态

  - 代理设置

    为了防止因频繁请求而封禁客户端，需要设置代理来解决这个问题，需要用到proxies参数

    ```python
    proxies={
        'http':'http://10.10.1.10:3128',
        'https':'http://10.10.1.10:1028'
    }
    requests.get(url,proxies=proxies)
    ```

    requests 还支持socks协议的代理

    ```python
    # 安装socks
    # pip install 'requests[socks]'
    import requests
    proxies={
        'http':'socks5://user:password@host:port',
        'https':'socks5://user:password@host:port'
    }
    requests.get(url, proxies=proxies)
    ```

  - 超时设置

    网络状态不好时，需要等很久的时间才能响应，甚至到最后收不到响应而报错，为了防止不能及时响应，需要设置一个超时时间，即过了这个时间没得到响应就报错，需要用到timeout参数

    这个时间是从发出请求到服务器返回响应的时间

    ```python
    import requests
    
    r = requests.get(url,timeout=1)
    ```

    将超时时间设置为1，如果1秒内没有响应那就抛出异常

    请求分两个阶段，即连接和读取，上面设置的timeout将用连接和读取这两者的timeout总和

    - `连接超时`指的是客户端实现到远端服务器端口的连接时request 所等待的时间。连接超时一般设为比 3 的倍数略大的一个数值，因为 TCP 数据包重传窗口的默认大小是 3。

    - `读取超时`指的客户端已经连接上服务器并且发送了request后，客户端等待服务器发送请求的时间。（一般指的是服务器发送第一个字节之前的时间）

      

    如果要分别指定，可以传入一个元组

    ```python 
    r = requests.get('https://github.com', timeout=(3.05, 27))
    ```

  - 身份认证

    ```python
    import requests
    from requests.auth import HTTPBasicAuth
    
    r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username','password'))
    ```

    如果参数都传HTTPBasicAuth类，就显得有点繁琐，requests提供了一个更简单的写法，直接传入一个元组，会默认使用HTTPBasicAuth类来认证

    ```python
    import requests
    r = requests.get(url,auth=('username','password'))
    ```

    requests还提供了其他认证方式，如OAuth,需要安装oauth包

    ```python
     # pip3 install requests_oauthlib
    import requests
    form requests_oauthlib import OAuth1
    
    auth = OAuth1('app_key','app_secret','oauth_token','oauth_tocken_secret')
    requests.get(url,auth=auth)
    ```

  - Prepared Request

    可以将请求表示为数据结构，各个参数可以通过一个requests对象来表示，这个数据结构叫Prepared Requests

    ```PYTHON
    from requests import Request,Session
    url = 'http://httpbin.org/post'
    data={
        'name':'germey'
    }
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    s = Session()
    # 构造Request对象，
    req = Request('POST', url, data=data, headers=headers)
    # 调用prepare_request()将Request对象转为一个Prepared Request
    prepped = s.prepare_request(req)
    # 调用send()方法发送
    r = s.send(prepped)
    ```

    

### 3.3正则表达式

常用的匹配规则：

| ^           | 匹配字符串的开头                                             |
| ----------- | ------------------------------------------------------------ |
| $           | 匹配字符串的末尾。                                           |
| .           | 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。 |
| [...]       | 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'          |
| [^...]      | 不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。             |
| re*         | 匹配0个或多个的表达式。                                      |
| re+         | 匹配1个或多个的表达式。                                      |
| re?         | 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式         |
| re{ n}      | 精确匹配 n 个前面表达式。例如， **o{2}** 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。 |
| re{ n,}     | 匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。 |
| re{ n, m}   | 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式         |
| a\| b       | 匹配a或b                                                     |
| (re)        | 对正则表达式分组并记住匹配的文本                             |
| (?imx)      | 正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。 |
| (?-imx)     | 正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。     |
| (?: re)     | 类似 (...), 但是不表示一个组                                 |
| (?imx: re)  | 在括号中使用i, m, 或 x 可选标志                              |
| (?-imx: re) | 在括号中不使用i, m, 或 x 可选标志                            |
| (?#...)     | 注释.                                                        |
| (?= re)     | 前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。 |
| (?! re)     | 前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功 |
| (?> re)     | 匹配的独立模式，省去回溯。                                   |
| \w          | 匹配字母数字及下划线                                         |
| \W          | 匹配非字母数字及下划线                                       |
| \s          | 匹配任意空白字符，等价于 [\t\n\r\f].                         |
| \S          | 匹配任意非空字符                                             |
| \d          | 匹配任意数字，等价于 [0-9].                                  |
| \D          | 匹配任意非数字                                               |
| \A          | 匹配字符串开始                                               |
| \Z          | 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。 |
| \z          | 匹配字符串结束                                               |
| \G          | 匹配最后匹配完成的位置。                                     |
| \b          | 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。 |
| \B          | 匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。 |
| \n, \t, 等. | 匹配一个换行符。匹配一个制表符。等                           |
| \1...\9     | 匹配第n个分组的内容。                                        |
| \10         | 匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。 |

![010](D:\project\pycon\web scrapy\img\010.png)

| 实例        | 描述                              |
| :---------- | :-------------------------------- |
| [Pp]ython   | 匹配 "Python" 或 "python"         |
| rub[ye]     | 匹配 "ruby" 或 "rube"             |
| [aeiou]     | 匹配中括号内的任意一个字母        |
| [0-9]       | 匹配任何数字。类似于 [0123456789] |
| [a-z]       | 匹配任何小写字母                  |
| [A-Z]       | 匹配任何大写字母                  |
| [a-zA-Z0-9] | 匹配任何字母及数字                |
| [^aeiou]    | 除了aeiou字母以外的所有字符       |
| [^0-9]      | 匹配除了数字外的字符              |

| 实例 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| .    | 匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。 |
| \d   | 匹配一个数字字符。等价于 [0-9]。                             |
| \D   | 匹配一个非数字字符。等价于 [^0-9]。                          |
| \s   | 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。 |
| \S   | 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。                  |
| \w   | 匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。         |
| \W   | 匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。                 |

#### match(pattern, string, flags=0)

- group(num=0),匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组
- groups(),返回一个包含所有小组字符串的元组，从 1 到 所含的小组号

`从0匹配，匹配不到返回none,此时没group/span属性，配合group返回结果`

match（）方法是从字符串的==开头开始匹配==的，一旦开头不匹配，那么整个匹配就失败 ,适合用来检测某个字符串是存符合某个正则表达式的规则。

向它传人要匹配的字符串以及正则表达式，就 可以检测这个正则表达式是否匹配字符串

试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果；如 果不匹配，就返回 None

```python
content ='Hello 123 4567 World_This is a Regex Demo'
print(len(content)) 
result = re.match(’<Hello\s\d\d\d\s\d{4}\s\w{10}’, content)
```

第一个参数传入了正则表达式，第二个参数传入了要匹配的字符串

打印输出结果，可以看到结果是 SRE_Match 对象,该对象有两个方法： ==group()==方法可以输出匹配到的内容, ==span（）==方法可以输出匹配的范围

```python
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配

m.group(0)   # 可省略 0
m.start(0)   # 可省略 0
m.end(0)     # 可省略 0
m.span(0)    # 可省略 0
```

当匹配成功时返回一个 Match 对象，其中：

- `group([group1, …])` 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 `group()` 或 `group(0)`；
- `start([group])` 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
- `end([group])` 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
- `span([group])` 方法返回 `(start(group), end(group))`

##### 匹配目标

match（）方法可以得到匹配到的字符串内容，但是如果想从字符串中提取一部分内容， 可以使用（）括号将想提取的子字符串括起来。 ==（）实际上标记了一个子表达式的开始和结束位 置==，被标记的每个子表达式会依次对应每一个分组，调用 group（）方法传入分组的索引即可获取提取 的结果

##### 通用匹配

```python
. 任意匹配(除换行)
* 匹配前面字符无限次
.* 万能匹配，任意字符
```

##### 贪婪与非贪婪

```python
.*? 尽可能少的匹配
```

##### 修饰符

```python
# ．匹配的是除换行符之外的任意字符， 当遇到换行符时，．的就不能匹配了，所以导致匹配失败。 这里只需加一个修饰符 re.S，即可修正这 个错误：
result = re.match（'^He.*?（＼d＋）.*?Demo$ '， content, re.S) 
```

![011](D:\project\pycon\web scrapy\img\011.PNG)

1. **re.I** 忽略大小写
2. **re.L** 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
3. **re.M** 多行模式
4. **re.S** 即为 **.** 并且包括换行符在内的任意字符（**.** 不包括换行符）
5. **re.U** 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
6. **re.X** 为了增加可读性，忽略空格和 **#** 后面的注释



##### 转义匹配

. 可以匹配除换行符以外的任意字符，如果目标字符含有 .  就需要用到转义匹配

```
re.match('www\.baidu\.com')
```

#### search(pattern, string, flags=0)

在匹配时会扫描==整个==字符串，然后返回==第一个==成功匹配的结 果

正则表达式可以是字符串的一部分，在匹配时， search（）方法会依次扫描字符串，直到找到==第一个==符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，就==返回 None==

为了匹配方便，我们可以尽量使用 search（）方法

代码有换行，第三个参数需要传人 re. S，这使得==.*?==可以匹配换行

用小括号包围，所以可以用 ==group（）==方法获取

大部分的html文本都包含了换行，所以尽量都加上re.S

```
re.search(pattern, 'html', re.S)
```

- group方法同上

#### findall(string[, pos[, endpos]])

- **string** : 待匹配的字符串。
- **pos** : 可选参数，指定字符串的起始位置，默认为 0。
- **endpos** : 可选参数，指定字符串的结束位置，默认为字符串的长度。

获取匹配正则表达式的所有内容，搜索整个字符串

返回的==列表==中的每个元素都是==元组==类型

#### sub(pattern, repl, string, count=0, flags=0)

- pattern : 正则中的模式字符串。
- repl : 替换的字符串，也可为一个==函数==。
- string : 要被查找替换的原始字符串。
- count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配

来==修改==文本,比如，想要把一串文本中的 所有数字都去掉，如果只用字符串的 replace（）方法，那就太烦琐了，这时可以借助 sub（）方法

```python
content =’54aKS4yrsoiRS4ixSL2g' 
content = re.sub(’\d+',”, content) 
```

第一个参数传入＼d＋来匹配所有的数字，第二个参数为替换成的字符串,第三个参数是原字符串

- replace方法

  ```python
  str.replace(old, new[, max])
  # 将字符串中的 str1 替换成 str2,如果 max 指定，则替换max 次
  # 不指定则全部替换
  ```

#### compile()

将 正则字符串编译成正则表达式对象以便在后面的匹配中复用

```python
pattern = re.compile(’\d{2}:\d{2}’) 
resultl = re.sub(pattern, '’, contentl)
```

`compile(pattern, flags=0) `还可以传入==修饰符==，例如 re . S 等修饰符，这样在 search（） 、 findall（）等方法中 就不需要额外传了。 所以， compile（）方法可以说是给正则表达式做了一层封装，以使我们更好地复用

### re.finditer(pattern, string, flags=0)

 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回

```
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )
```

### re.split(pattern, string[, maxsplit=0, flags=0])

split 方法按照能够匹配的子串将字符串分割后返回列表

- maxsplit:分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。

### re.MatchObject

group() 返回被 RE 匹配的字符串。

- **start()** 返回匹配开始的位置
- **end()** 返回匹配结束的位置
- **span()** 返回一个元组包含匹配 (开始,结束) 的位置

### 3.4抓取猫眼电影

==响应乱码解决方式==

___

- 爬取的网页编码与我们爬取编码方式不一致造成的。如果爬取的网页编码方式为`utf8`，而我们爬取后程序使用`ISO-8859-1`编码方式进行编码并输出，这会引起乱码。如果我们爬取后程序改用`utf8`编码方式，就不会造成乱码

- 首先确定爬取的网页编码方式，编码方式往往可以从HTTP头(header)的`Content-Type`得出。

  `Content-Type`，内容类型，一般是指网页中存在的`Content-Type`，用于定义网络文件的类型和网页的编码，决定浏览器将以什么形式、什么编码读取这个文件，这就是经常看到一些Asp网页点击的结果却是下载到的一个文件或一张图片的原因。如果未指定`ContentType`，默认为TEXT/HTML。`charset`决定了网页的编码方式，一般为`gb2312`、`utf-8`等

- 如果上述方式没有编码信息，一般可以采用`chardet`等第三方网页编码智能识别工具识别:

  `pip install chardet`

  使用`chardet`可以很方便的实现文本内容的编码检测。虽然HTML页面有`charset`标签，但是有些时候并不准确，这时候我们可以使用`chardet`来进一步的判断:

  ```python
  raw_data = urllib.urlopen('http://blog.csdn.net/sunnyyoona').read()
  print chardet.detect(raw_data)  # {'confidence': 0.99, 'encoding': 'utf-8'}
  ```

  函数返回值为字典，有2个元素，一个是检测的可信度，另外一个就是检测到的编码

- 可以使用`r.encoding = xxx`来更改编码方式，这样`Requests`将在你调用`r.text`时使用`r.encoding`的新值，使用新的编码方式

  ```python
  url = "https://baike.baidu.com/item/%E4%B8%80%E7%AD%89%E7%AB%99"
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
  r = requests.get(url, headers=headers)
  
  # 检测编码
  raw_data = urllib.urlopen(url).read()
  charset = chardet.detect(raw_data)  # {'confidence': 0.99, 'encoding': 'utf-8'}
  encoding = charset['encoding']
  # 更改编码方式
  r.encoding = encoding
  ```

## 第四章 解析库的使用

比较强大的解析库lxml,beautiful Soup,pyquery

### 4.1 xPath

全称XML path language

![012](D:\project\pycon\web scrapy\img\012.PNG)

```	python
from lxml import etree
text = '''some text'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
```

etree.parse() 和 etree.HTML() 

```python
# The parse() function is used to parse from files and file-like objects.
from io import BytesIO
some_file_or_file_like_object = BytesIO(b"<root>data</root>")
tree = etree.parse(some_file_or_file_like_object)
etree.tostring(tree)
```

etree可以自动修正HTML文本

tostring方法输出修正后的HTML代码，就是是bytes类型，利用decode转为str

```python
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
```

#### 运算符及其介绍

![013](D:\project\pycon\web scrapy\img\013.PNG)

```python
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
```



### 4.2 Beautiful Soup

是python的一个HTML和XML解析库，可以用来方便的提取数据

==借助网页的结构和属性等特性来解析网页==

自动将输入文档的转为Unicode编码，输出文档转为UTF-8，不需要考虑编码方式，除非原文档没有指定编码，此时说明下编码方式就可以了

- 确认已经安装了==Beautiful Soup 和 lxml==
- 解析时依赖解析器，除了支持python标准库的html外，还支持第三方的解析器如lxml

Beautiful Soup支持的解析器

| 解析器             | 使用                                 | 优势                                                  | 劣势                         |
| ------------------ | ------------------------------------ | ----------------------------------------------------- | ---------------------------- |
| python标准库       | BeautifulSoup(markup, 'html.parser') | 速度适中,容错能力强                                   | py2.7及3.2之前的版本容错力差 |
| lxml   HTML 解析器 | BeautifulSoup(markup, 'lxml')        | 速度快，容错强                                        | 需安装c语言库                |
| lxml  XML 解析器   | BeautifulSoup(markup, 'xml')         | 速度快，唯一支持xml                                   | 需安装c语言库                |
| html5lib           | BeautifulSoup(markup, 'html5lib')    | 最好的容错性，以浏览器方式生成解析文档，生成html5文档 | 速度慢                       |

lxml有解析 HTML和XML的功能，而且速度快，容错力强，推荐使用

> 如果使用lxml,初始化Beautiful Soup时，把第二个参数改为lxml即可

#### 6.方法选择器

-  find_all()  find()

  find_all(tag, attributes, recursive, text, limit, keywords)

  find_all（标签、属性、递归、文本、限制、关键词）

  find(tag, attributes, recursive, text, keywords)

  **find_all会将所有满足条件的值取出，组成一个list**

  > find与find_all的区别，find只会取符合要求的第一个元素，find_all会根据范围限制参数limit限定的范围取元素（默认不设置代表取所有符合要求的元素，find 等价于 find_all的 limit =1 时的情形）

  - attributes

    用字典封装一个标签的若干属性和对应的属性值

  - 递归recursive

    > recursive 设置为 True， find_all 就会根据你的要求去查找标签参数的所有子标签，以及标签的子标签。如果 recursive 设置为 False， find_all 就只查找文档的一级标签。 find_all默认是支持递归查找的（recursive 默认值是 True）；一般情况下这个参数不需要设置，非你真正了解自己需要哪些信息，而且抓取速度非常重要，那时你可以设置递归参数

  - keywords

    > - 关键词参数 keyword，自己选择那些具有指定属性的标签
    >
    > - 如果是class、id等参数，用keywords 或者attributes用法一样，如果是一些其他参数，则用keywords

#### 7.css选择器

使用 css 选择器时，只需要调用 select（）方法，传人相应的 css 选择器即可

- 嵌套选择

  select（）方法同样支持嵌套选择。 例如，先选择所有 ul 节点，再遍历每个 ul 节点，选择其 li 

- 获取属性

  ```python
  # 直接传入中括号和属性名，以及通过 attrs 属性获取属性值，都可以
  for ul in soup.select('ul'):
      print(ul.attrs['id'])
      # 等价于
      print(ul['id'])
  ```

- 获取文本

  ```python
  # 可以用string属性，也可以使用get_text()方法
  for li in soup.select('li'):
      print('Get Text:', li.get_text())
      print('String:', li.string)
  ```

  string 是属性，get_text()是方法

### 4.3 Pyquery

Beautifulsoup的css选择器功能没那么强大，如果喜欢css选择器，并对jQuery有所了解，可以尝试Pyquery

pyquery库是jQuery的Python实现，能够以jQuery的语法来操作解析 HTML 文档，易用性和解析速度都很好，和它差不多的还有BeautifulSoup，都是用来解析的。相比BeautifulSoup完美翔实的文档，虽然PyQuery库的文档弱爆了， 但是使用起来还是可以的

1. 准备工作

   ```python 
   # pip 安装
   pip3 install pyquery
   
   # 验证安装,导入无错误则安装成功
   import pyquery
   ```

2. 初始化

   类似beautifulsoup, pyquery 也需要传入html文本来初始化一个Pyquery对象

   - 字符串初始化

     ```python
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
     ```

   - URL初始化

     初始化的参数不仅可以以字符串的形式传递，还可以传入网页的url

     ```python
     from pyquery import PyQuery as pq
     doc = pq(url='http://cuiqingcai.com',encoding='utf-8')
     print(doc('title'))
     ```

   - 文件初始化

     还可以传递本地的文件名， 此时将参数指定为 filename 即可 

     ```python
     from pyquery import PyQuery as pq
     doc = pq(filename='demo.html')
     ```

3. 基本css选择器

   ```python
   from pyquery import PyQuery as pq
   doc = pq(html)
   # 选取id为container的节点，然后选取class为list的节点内部的li
   print('css 选择器',doc('#container .list li'))
   ```

4. 查找节点

   查找子节点使用find()方法，

   ```python
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
   ```

5. 遍历

   pyquery的选择结果可能是多个节点，也可能是单个节点，类型都是pyquery类型

   - 对于单个节点，可以直接打印输出，也可以转为字符串

   ```python
   # 对于单个节点
   doc = pq(html)
   li = doc('.item-0.active')
   print('li:', li)
   print(str(li))
   ```

   - 对于多个节点的结果，需要遍历来获取,需要调用items()方法

     ```python
     doc = pq(html)
     # 生成器对象-generator
     lis = doc('li').items()
     print(type(lis))
     for li in lis: 
         print(li, type(li))
     ```

6. 获取信息

   提取节点后需要获取信息，主要有两种，属性和文本

   - 获取属性

     ```python
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
     ```

   - 获取文本

     ```python
     # 使用text()函数实现,获取节点内部文本
     doc = pq(html)
     a = doc('.item-0.active a')
     print(a.text())
     
     # 获取节点html文本,使用 html()方法
     li = doc('.item-0.active')
     print('li:', li)
     print(li.html())
     
     # 如果选中多个节点，text() 或 html() 会返回什么内容？
     li = doc('li')
     print('li_html:', li.html())
     print('li_text:', li.text())
     # html()方法返回了第一个li节点的内部HTML文本
     # text()方法返回了所有的li节点内部的纯文本，之间用空格割开，即是一个字符串
     ```

7. 节点操作

   ```python
   # 对某个节点添加一个class,移除某个节点等
   # 节点方法较多，举几个典型
       # addClass 和 removeClass ,动态改变节点的class属性
      
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
   ```

8. 伪类选择器

   css选择器之所以强大，是因为它支持多种多样的伪类选择器，例如：选择第一个节点、最后一个节点、奇偶数节点、包含某一文本的节点

   ```python
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
   ```

   

## 第五章_数据存储

保存数据的形式多种多样，最简单的形式是直接保存为文本文件，如txt,json,csv,还可以保存到数据库，如关系型数据库MySQL,非关系型数据库MongDB,Redis等

### 5.1文件存储

#### txt 文本

操作简单，几乎兼容任何平台，但不利于检索，如果对检索和数据结构要求不高，追求方便，可采用txt文本存储

```python
open方法第二个参数为a,代表追加写入
写入完成，还需调用close()关闭文件对象
```

- 打开方式

  r:只读，指针在开头（默认）

  rb:二进制只读，指针在开头

  r+:读写方式，指针在开头

  rb+:二进制读写，指针在开头

  w:写入方式，存在则覆盖，不存在则创建

  wb:二进制写入，存在则覆盖，不存在则创建

  w+:读写方式，存在则覆盖，不存在则创建

  wb+:二进制读写，存在则覆盖，不存在则创建

  a:追加打开，存在指针放结尾，不存在则创建

  ab:二进制追加打开，存在指针放结尾，不存在则创建

  a+:读写方式的追加，存在则指针放结尾，不存在则创建

  ab+:二进制读写方式的追加，存在则指针放结尾，不存在则创建

- 简化写法

  ```python
  with open() as file:
      file write()
  # 这样就不用调用close（）
  ```

#### Json 文件存储

---

json.dumps()

- sort_keys是告诉编码器按照字典key排序(a到z)输出

  ```python
  >>> import json
  >>> data = [{'c': 'C', 'b':(1, 6), 'a': 'A'}]
  >>> print(data)
  [{'a': 'A', 'c': 'C', 'b': (1, 6)}]
  >>> print(json.dumps(data,sort_keys=True))
  [{"a": "A", "b": [1, 6], "c": "C"}]
  ```

- indent参数根据数据格式缩进显示，读起来更加清晰, indent的值，代表缩进空格式

  ```python
  >>> print(json.dumps(data,sort_keys=True))
  [{"a": "A", "b": [1, 6], "c": "C"}]
  >>> print(json.dumps(data,sort_keys=True,indent=4))
  [
      {
          "a": "A", 
          "b": [
              1, 
              6
          ], 
          "c": "C"
      }
  ]
  ```

- separators参数的作用是去掉‘，’ ‘：’后面的空格，在传输数据的过程中，越精简越好，冗余的东西全部去掉

  ```PYTHON
  >>> print(json.dumps(data,sort_keys=True))
  [{"a": "A", "b": [1, 6], "c": "C"}]
  >>> print(json.dumps(data,sort_keys=True,separators=(',',':')))
  [{"a":"A","b":[1,6],"c":"C"}]
  ```

- skipkeys参数，在encoding过程中，dict对象的key只可以是string对象，如果是其他类型，那么在编码过程中就会抛出ValueError的异常。skipkeys可以跳过那些非string对象当作key的处理

  ```python
  print(json.dumps(data2, separators=(',', ':')))
  >>>TypeError: keys must be str, int, float, bool or None, not tuple
  print(json.dumps(data2, separators=(',', ':'), skipkeys=True))
  >>>[{"a":"A","b":[1,6],"c":"C"}]
  ```

- 输出真正的中文需要指定ensure_ascii=False

  json.dumps 序列化时对中文默认使用的ascii编码，处理中文是会出现乱码，

  ```python
  >>> print(json.dumps('中国'))
  "\u4e2d\u56fd"
  >>> print(json.dumps('中国',ensure_ascii=False))
  "中国"
  ```

---



- 对象和数组

  javaScript object notation 语言中，一切都是对象，任何支持的类型都可通过JSON来表示，例如字符串、数字、对象、数组等

  对象和数组是特殊且常用的

  - 对象：使用{ } 包裹起来的key:value键值对，键名可使用整数和字符串，值可以是任意类型
  - 数组：使用[] 包裹起来的['java', 'vb',...] 索引结构，值可以是任意类型

  json可由以上两种自由组合而成，可无限嵌套，结构清晰，是数据交换极佳方式

- 读取JSON

  - loads() 将json文本转为json对象

  - dumps() 将json对象转为文本字符串
    - 获取键值时有两种方式：

      - 中括号加键名

      - get()方法传入键名

        如果键名不存在，不会报错，会返回none

        get()方法可传入==第二个参数，即默认值==

- 输出JSON

  利用dumps方法将json对象转为字符串，然后调用 write() 方法写入文本

  ```python
  with open('data.json','w') as file:
      file.write(json.dumps(data))
  ```

  JSON的数据需要用双括号来包围，不能使用单引号，否则 loads() 会解析失败

  - 写入数据中有中文

    ```python
    import json
    
    data = [{
        'name': '王伟',
        'gender': '男',
        'birthday': '1992-10-18'
    }]
    with open('json_dumps_data.json', 'w') as file:
        file.write(json.dumps(data))
    # 写入的结果
    '''
    [{"name": "\u738b\u4f1f", "gender": "\u7537", "birthday": "1992-10-18"}]
    '''
    # 中文的字符都变成了Unicode字符，并不是我们要的结果
    # 为了正常输出中文，还需要指定参数 ensure_ascii = False ,还要指定文件输出的编码
    with open('json_dumps_data.json','w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False))
    ```

#### csv  文件存储

csv 全称 comma-separated values

中文叫做逗号分隔值或字符分隔值，文件以纯文本形式存储表格数据

文件是字符序列，可以由任意数目的记录组成，记录间以某种换行符分隔

每条记录由字段组成，字段间的分隔符是其他字符或字符串，常见的是逗号或制表符 

- 写入

  - 单行，多行列表

    - writer = ==csv.writer==(csvfile)
      - writer.==writerow==(['id','name','age'])
      - writer.==writerows==([['10001','Mike',20], ['10002','Bob', 22]])

  - 写入字典对象

    - writer = csv.DictWriter(csvfile)
      - writer.writerow()

  - pandas写入

    - to_csv()

    ```python
    import pandas as pd
    df = pd.Dataframe(data)
    df.to_csv('test.csv',header=True, index=True)
    ```

  单行，多行列表例子：

  ```python
  # 修改列与列之间的分隔符，可以传入 delimiter 参数
  with open('./exercise/csv_data.csv','w') as csvfile:
      # 定义写入对象
      writer = csv.writer(csvfile, delimiter=' ')
      # 调用 writerow（）方法传入每行的数据即可完成写入
      writer.writerow(['id', 'name', 'age'])
  
  # 以调用 writerows（）方法同时写入多行, 此时参数就需要为二维列表
  with open('./exercise/data.csv','w') as csvfile:
      # 创建对象
      writer = csv.writer(csvfile)
      # 写入头部
      writer.writerow(['id','name','age'])
      # 写入数据
      writer.writerows([['10001','Mike',20], ['10002','Bob', 22]])
  ```

  字典对象例子：

  ```python
  import csv
  # 追加写入 with open('./exercise/data_.csv', 'w') as csvfile:
  with open('./exercise/data_.csv', 'w') as csvfile:
      # 头部
      fieldnames = ['id', 'name', 'age']
      # 写入对象
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      # 写入头部
      writer.writeheader()
      # 写入数据
      writer.writerow({'id': '10001', 'name': 'Mike', 'age': 10})
      writer.writerow({'id':'10002 ', 'name': 'Bob', 'age': 22}) 
  ```

- 读取

  - csv读取数据

    - 对打开的文件使用csv库的 ==reader== 构造读取对象
    - 如果csv文件中包含==中文==，需要指定==文件编码==

    ```python
    with open('./exercise/data.csv', 'r', encoding='utf-8') as csvfile:
        # 读操作：对打开的文件使用csv库的 reader 构造读取对象
        # 写操作：对打开的文件使用csv库的 writer, DictWriter 构造写对象
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    ```

  - pandas读取

    - read_csv()

    ```python
    import pandas as pd
    df = pd.read_csv('./exercise/data.csv')
    print(df)
    ```

### 5.2 关系型数据库

python2中，连接mysql大多使用 ==MySQLdb==，不支持python3

python3中，推荐使用 ==PyMySQL==库

```python
# 安装方法
# version:pymysql-0.9.3
pip install pymysql
```

database = db

password = passwd

```python
import pymysql

# 参数
user = 'root'
password = 'devil'
port = 3308
host = 'localhost'
db = 'easysql'
# 连接数据库
db = pymysql.connect(host=host, user=user, 
                     passwd=password, port=port, db = db)
# 创建游标
cursor = db.cursor()
# 执行命令 execute()
cursor.execute('select version()')
data = cursor.fetchone()
print(data)
tables = cursor.execute('show tables')
print(tables)
db.close()

# 创建表
import pymysql

db = pymysql.connect(host='localhost', user='root',
                     passwd='devil', port=3308, db='easysql')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS test (id VARCHAR(25) NOT NULL , name VARCHAR(25) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()

# 插入数据
import pymysql

db = pymysql.connect(host='localhost', user='root', passwd='devil', 
                     port=3308, db='test_db')
cursor = db.cursor()
# 格式化符%s ，有几个 Value 写几个
sql = 'insert into students(id, name, age) values(%s, %s,  %s)'
# 如果执行失败，则调用 rollback（）执行数据回滚，相当于什么 都没有发生
try:
    cursor.execute(sql,(id, name, age))
    db.commit()
except:
    db.rollback()
finally:
    cursor.close()
    db.close()
```

- 事务的四个属性

  MySQL 事务主要用于处理操作量大，复杂度高的数据。比如说，在人员管理系统中，你删除一个人员，你既需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等，这样，这些数据库操作语句就构成一个事务

  - 在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
  - 事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。
  - 事务用来管理 insert,update,delete 语句

事务是必须满足4个条件（ACID）：：原子性（**A**tomicity，或称不可分割性）、一致性（**C**onsistency）、隔离性（**I**solation，又称独立性）、持久性（**D**urability）

**原子性：**一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样

**一致性：**在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作

**隔离性：**数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）

**持久性：**事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

```python
# 插入数据实例
import pymysql

# data示例
name = '二黑'
hobby = '抽烟'
professional = '菜贩子'
adress = '奈何桥'

db = pymysql.connect(host='localhost', port='33080', user='root',
                     passwd='devil', db='test_db')
cursor = db.cursor()
# 构造sql语句，使用 %s 格式化符来实现， 有几个 value 写几个 %s
# 然后再execute()方法第二个参数用元组传入value
sql = 'insert into fatboy_hobby(name,hobby,professional,adress) values(%s,%s,%s)'
try:
    cursor.execute(sql,(name,hobby,professional,adress))
    # 执行commit才可实现数据插入，真正将数据提交到数据库
    db.commit()
except:
    db.rollback()
db.close()

# 该操作有一个不足，比如突然增加了gender字段，此时句需要改为：
sql = 'insert into fatboy_hobby(name,hobby,professional,adress,gender)\
                   values(%s,%s,%s,%s)'
# execute的传入参数也会变


# 很多情况下，我们要达到的效果是不做改变，需要做成一个通用方法
# 只需要传入一个动态字典就，sql语句根据字典动态构造，元组也动态构造
data = {
    'name':'新管病毒',
    'hobby':'飞行',
    'professional':'杀人',
    'gender':'NP'
}
table = 'fatboy_hobby'
keys = ','.join(data.keys())
# 当时出错的地方，多加注意
value = ','.join(['%s']*len(data))
sql = 'insert into {} ({}) values({})'.format(table, keys, values)
try:
    if cursor.execute(sel):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
```

- 更新数据

  ```python
  sql = 'updata sutdents set age = %s where name = %s'
  try:
      cursor.execute(sql)
      db.commit()
  except:
      db.rollback()
  db.close()
  
  # 利用占位符构造SQL，简单的数据更新可以用此方法
  # 实际使用中，大部分的情况需要插入数据，我们关心的是会不会出现重复数据
  # 如果出现了我们希望更新数据（不存在插入，存在就更新）
  data = {
      'id': '20120001',
      'name': 'Bob',
      'age': 21
  }
  
  table = 'students'
  keys = ','.join(data.keys())
  values = ','.join(['%s']*len(data))
  sql = 'insert into {table} ({keys}) values ({values}) on duplicate key update'.format(
      table=table, keys=keys, values=values)
  # ON DUPLICATE KEY UPDATE
  # 如果主键存在就更新操作
  update = ','.join(["{key} = %s".format(key=key)for key in data])
  sql += update
  try:
      # 元组和数字相乘是扩展
      if cursor.execute(sql,tuple(data.values())*2):
          print('successful')
          db.commit()
  except:
      print('Faild')
      db.rollback()
  db.close()
  ```

- 删除数据

  ```python
  import pymysql
  
  db = pymysql.connect(
      host='localhost',
      port=3308,
      user='root',
      passwd='devil',
      db='test_db',
      charset='utf8'
  )
  cursor = db.cursor()
  table = 'students'
  condition = 'age > 20'
  
  sql = 'DELETE from {table} where {condition}'.format(table,condition)
  try:
      cursor.execute(sql)
      db.commit()
  except:
      db.rollback()
  db.close()
  ```

### 5.3非关系型数据库

NoSQL，全称为 Not Noly SQL,不仅仅是SQL，泛指非关系型数据库，NoSQL是基于键值对的，不需要sql层的解析，数据之间没有耦合性，性能高

模块间联系越多，其耦合性越强，同时表明其独立性越差( 降低耦合性，可以提高其独立性)。软件设计中通常用==耦合度==和==内聚度==作为衡量模块独立程度的标准

划分模块的一个准则就是==高内聚低耦合==

非关系型数据库分类：

- 键值存储数据库：Redis, Voldemort, Oracle BDB 等
- 列存储数据库： Cassandra, HBase， Riak
- 文档型数据库： CouchDB, MongoDB
- 图形数据库： Neo4J, InfoGrid, Infinite Graph

对于爬虫数据来说，数据可能存在字段提取失败而缺失的情况，而且数据随时可能调整，数据间还有嵌套关系，需要序列化操作才可存储，非常不方便，如果用了非关系型数据库就可避免一些麻烦，简单高效

下面主要介绍MongoDB和Redis:

#### 5.3.1MongoDB

MongoDB 由c++编写的NoSQL，是一个基于分布式文件存储的开源数据库系统，内容存储类是json对象，字段可包含其他文档，数组及文档数组

```python
import pymongo

# 创建连接
client = pymongo.MongoClient(host='localhost', port=27017)
# 另外一中连接方式，也是mongdb compass的连接方式
# client = MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# 数据库的另外一种指定方式
db = client['test']

# 指定集合
# 数据库包含很多集合（collection），类似sql中的表
# 两种指定方式
collection = db.students
collection = db['students']

# 插入数据
# 字典形式数据
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
# 使用insert方法即可插入
result = collection.insert(student)
print(result)
# mongodb中每个数据都有一个 _id属性来唯一标识，没有显式的指定该属性
# mongodb会自动产生一个objectId类型的_id属性，insert方法执行后返回id值

# 也可插入多条，只需要以list形式传入即可
result = collection.insert([student1, student2])
# 返回结果是_id的集合

# 官方推荐使用insert_one() 和 insert_many() 分别插入一条和多条
# insert 不同的是此两个方法返回InsertOneResult对象，
# 我们可以调用其inserted_id获取_id
posts = db.posts
post_id = posts.insert_one(post).inserted_id

# insert_many()方法，我们可以将数据以列表方式传入
result = collection.insert_many([student1, student2])


# 查询
# 插入数据后可以使用find_one() 和 find() 方法查询
# find_one()返回单个结果，find()查多条数据，返回一个生成器对象
result = collection.find_one({'name':'mike'})
# 返回字典类型，会多一条_id属性，是自动添加的

# 也可以通过ObjectId 结合 _id 来查询数据
# 此时需要调用bson库里的objectid
from bson.objectid import ObjectId
result = collection.find_one({'_id':ObjectId('_id_numbers')})
# 返回同样的结果，不存在则返回None
```

![016](D:\project\pycon\web scrapy\img\016.png)

```python
# 利用find方法查询多条数据
# 返回结果是Cursor类型，相当于一个生成器，我们需要遍历获取结果
results = collection.find({'age':20})
print(result)
>>> <pymongo.cursor.Cursor object at 0x1032d1528>
for result in results:
    print(result)
    # 得到多个字典

# 查询年龄大于20的数据
results = collection.find({'age':{'$gt':20}})
# 查询条件是一个嵌套字典
```

- 比较符号归纳

  $lt 		小于		{'age':{'$lt':20}}

  $gt 		大于		{'age':{'$gt':20}}

  $lte		小于等于		{'age':{'$lte':20}}

  $gte 	大于等于		{'age':{'$gte':20}}

  $ne 	不等于		{'age':{'$ne':20}}

  $in 		在范围内		{'age':{'$in':[20, 23]}}

  $nin	不在范围		{'age':{'$nin':[20, 23]}}

```python
# 还可以通过正则匹配查询，例如，查询名字以M开头的学生数据
result = collection.find({'name':{'$regex':'^M.*'}})
```

- 符号归纳

  $regex			匹配正则表达式		{'name': {'$regex':'^M.*'}}		name以M开头

  $exists		        属性是否存在		        {'name': {'$exists': True}}		 name属性存在

  $type 		        类型判断                         {‘age': {'$type': 'int'}}                         age的类型为int

  $mod                      数字模操作                     {’age‘: {'$mod': [5, 0]}}                      年龄模5余0

  $text                       文本查询                         {’$text‘: {'$search': 'Mike'} }          text类型的属性中包含Mike的str

  $where                   高级条件查询                 {'$where': 'obj.fans_count == obj.follows_count'}

  ​                                                                                                                                 自身粉丝数等于关注数

- 计数

  ```python
  # 计数
  # 要统计查询结果有多少条，可以使用count()
  count = collection.find().count()
  ```

- 排序

  ```python
  # cursor 的 sort 方法
  sort(key_or_list, direction=None)
  # Pass a field name and a direction (pymongo.ASCENDING, pymongo.DESCENDING)
  for doc in collection.find().sort([
                  ('field1', pymongo.ASCENDING),
                  ('field2', pymongo.DESCENDING)]):
              print(doc)
  ```

- 偏移

  ```python
  # 某些情况下我们可能只想取某几个元素，这时可使用skip偏移几个位置
  # 比如偏移2就忽略两个元素，得到后面的元素
  results = collection.find().skip(2)
  # 可以使用limit方法指定要获取的元素个数
  results = collection.find().skip(2).limit(3)
  # 在数据库非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量查询数据
  # 这样可能导致内存溢出，可以使用如下操作查询
  from bson.objectid import ObjectId
  collection.find({'_id': {'$gt': ObjectId('id_num')}})
  # 需要记录好上次查询的id
  ```

- 更新

  ```python
  # 方法一：
  # 对于数据更新我们可以使用update,指定更新条件和数据
  condition = {'name': 'Kevin'}
  student = collection.find_one(condition)
  student['age'] = 25
  result = collection.update(condition, student)
  # 先指定查询条件，对查询的数据做修改，调用update更新数据
  # 方法二：
  # 使用$set操作符
  result = collection.update(condition, {'$set': student})
  
  # 使用$set只更新字典内存在的字段，如果之前有其他字段则不会更新不会删除
  # 而不使用$set会把之前的数据全部用student字典替换，如果之前存在其他字段，则会删除
  # update也不是官方推荐的方法，这里也分 update_one, update_many,用法更严格
  result = collection.find({'name':'Jordan'}).skip(1)
  collection.update_one({'_id': ObjectId(result[0]['_id'])}, 
                        {'$set': {'name':'Bob'}})
  # update_one 第二个参数不能再直接传入修改后的字典，而是需要{'$set':student}这样
  # 返回结果是updateResult类型，可调用 matched_count 和 modified_count属性
  # 获取匹配的数据条数和影响的数据条数
  
  # 例子
  condition = {'age': {'$gt': 20}}
  result = collection.update_one(condition, {'$inc': {'age': 1}})
  # 查询条件为年龄大于20，修改条件为年龄加1
  print(result.matched_count, result.modified_count)
  # 得到匹配和修改的条数都为1
  
  # 如果使用update_many() 则会将所有匹配的都更新
  ```

- 删除

  ```python
  # 调用remove()指定删除条件即可，符合条件的均被删除
  result = collection.remove({'name': 'Kevin'})
  # 这里有两个新的推荐方法 delete_one() 和 delete_many()
  result = collection.delete_one({'name': 'Kevin'})
  result2 = collection.delete_many({'age': {'$lt': 25}})
  # delete_one() 删除符合条件的第一条
  # delete_many() 删除符合条件的全部
  # 返回结果是DeleteResult,可调用delete_count获取删除的条数
  ```

- 其他操作

  ```python
  find_one_and_delete()
  find_one_and_replace()
  find_one_and_update()
  # 详细参见官网
  ```

#### 5.3.2 Redis存储

Redis是一个基于内存的高效的键值型非关系型数据库，存取效率极高，支持多种存储数据结构

下面主要介绍redis-py库

##### Redis 和 StrictRedis

redis-py提供两个类来实现redis的命令操作

StrictRedis实现了大部分官方命令，参数也一一对应，官方推荐使用StrictRedis

##### 连接redis

```python
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='devil')
redis.set('name','Bob')
print(redis.get('name'))from redis import StrictRedis
```

这样的连接效果是一样的，观察源码可发现，StrictRedis内其实就是用host和port等参数又构造了一个ConnectionPool,所以直接将ConnectionPool当作参数传给StrictRedis也一样，另外也通过url来构造，url的格式支持如下三种：

redis://[:password]@host:port/db

rediss://[:password]@host:port/db

unix://[:password]@/path/to/socket.sock?db=db

这里传入了Redis的地址，运行端口，使用的数据库和密码信息，在默认情况下4个参数分别为localhost,6379,0和None.

这三种url分别表示创建==RedisTCP==连接，==RedisTCP + SSL==连接，==RedisUNIXsocket==连接，我们只需要构造上面任意一种URL即可，其中password部分如果有则可以写，没有则可以忽略，url的连接演示：

使用第一种方式，申明一个redis连接字符串，调用from_url()方法创建connectionPool,接着将其传给strictredis

```
url = 'redis://:devil@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redi = StrictRedis(connection_pool=pool)
```

##### 键操作

| 方法               | 作用                                          | 参数                            | 示例                         | 示例说明                    | 结果      |
| ------------------ | --------------------------------------------- | ------------------------------- | ---------------------------- | --------------------------- | --------- |
| exists（name）     | 判断键是否存在                                | name:键名                       | redis.exists('name')         | 是否存在键                  | True      |
| delete（name）     | 删除一个键                                    | name:键名                       | redis.delete('name')         | 删除键                      | 1         |
| type（name）       | 判断键类型                                    | name:键名                       | redis.type('name')           | 判断键类型                  | b'string' |
| keys(pattern)      | 获取符合的键                                  | pattern:匹配规则                | redis.keys('n*')             | 获取所有以n开头的键         | b'name'   |
| randomkey()        | 随机获取一个键                                |                                 | randomkey()                  |                             |           |
| rename(src, dst)   | 重命名                                        | src:原键名           dst:新键名 | redis.rename(name, nickname) | 将name重命名nickname        | True      |
| dbsize()           | 获取当前数据库中键的数目                      |                                 | dbsize()                     |                             |           |
| expire(name, time) | 设定键的过期时间，单位为秒                    | name:键名           time:秒数   | redis.expire('name', 2)      | 将name键的过期时间设置为2秒 | True      |
| ttl(name)          | 获取键的过期时间，单位为秒，-1 表示永久不过期 | name:键名                       | redis.ttl('name')            | 获取name这个键的过期时间    | -1        |
| move(name, db)     | 将键移动到其他数据库                          | name:键名    db:数据库代号      | move('name', 2)              | 将name移动到2号数据库       | True      |
| flushdb()          | 删除当前选择数据库中的所有键                  | flushdb()                       | 删除当前选择数据库中的所有键 | flushdb()                   | True      |
| flushall()         | 删除所有数据库中的所有键                      | flushall()                      |                              |                             | True      |

##### 字符串操作

Redis支持最基本的键值对形式存储

| 方法                          | 参数说明                                                     | 作用                                                         | 示例说明                                         | 示例结果                                        | 示例                                                         |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------ |
| set(name, value)              | name:键名   value:值                                         | 给name键赋值value                                            | 给name键赋值为Bob                                | True                                            | redis.set('name','Bob')                                      |
| get(name)                     | name:键名                                                    | 返回数据库中键为name的string的value                          | 返回neme这个键的value                            | b'Bob'                                          | redis.get('name')                                            |
| getset(name,value)            | name:键名     value:新值                                     | 给数据库中键为name的string赋予值value并返回上次value         | 赋值name为Mike并得到上次的value                  | b'Bob'                                          | redis.getset('name', 'Mike')                                 |
| mget(keys, *args)             | keys:键的列表                                                | 返回多个键对应的value                                        | 返回name和nickname的value                        | [b'Mike', b'Miker']                             | redis.mget(['name', 'nickname'])                             |
| setnx(name, value)            | name:键名                                                    | 如果不存在这个键值对，则更新value,否则不变                   | 如果newname这个键不存在，则设置为James           | 第一次运行结果为True，第二次运行结果为False     | redis.setnx('newname','James')                               |
| setex(name,time,value)        | name:键名 time：有效期  value：值                            | 设置可以对应的值为string类型的value，并设置此键值对应的有效期 | 将name这个键的值设为James,有效期为1秒            | True                                            | redis.setex('name',1,'James')                                |
| setrange(name, offset, value) | name:键名，offset:偏移量，value：值                          | 设置指定键的value值的子字符串                                | 设置name为hello字符串，并在index为6的位置补world | 11,==修改后的字符串长度==，True                 | redis.set('name', 'hello')     redis.setrange('name',6, 'world') |
| mset(mapping)                 | mapping:字典                                                 | 批量赋值                                                     | 将name1设为Durant, name2设为James                | True                                            | redis.mset({'name1':'Durant', 'name2':'James'})              |
| msetnx(mapping)               | mapping：字典                                                | 键均不存在时才批量赋值                                       | 在name3和name4均不存在的情况下才设置二者值       | True                                            | redis.msetnx({'name3':'Smith', 'name4':'Curry'})             |
| incr(name, amount=1)          | name:键名   amount:增长的值                                  | 键为name的value增值操作，默认为1，键不存在则被创建并设为amount | age对应的值增1，若不存在，则会创建并设置为1      | redis.incr('age', 1)                            | 返回修改后的值                                               |
| decr(name, amount=1)          | name:键名  amount：减少的值                                  | 键为name的value减值操作，默认为1，键不存在则被创建并将value设置为-amount | age对应的值减1，若不存在，则会创建并设置为-1     | redis.decr('age', 1)                            | -1, 即修改后的值                                             |
| append(key, value)            | key:键名                                                     | 键为name的string的值附加value                                | 向键为nickname的值后追加ok                       | redis.append('nickname', 'ok')                  | 13, 即修改后的字符串长度                                     |
| substr(name, start, end= -1)  | name:键名   start:起始索引；end:终止索引，默认为-1，表示截取到末尾 | 返回键为name的string的子串                                   | 返回键为name的值的字符串，截取索引为 1~4 的字符  | redis.substr('name', 1, 4)                      | b'ello'                                                      |
| getrange(key, start, end)     | 获取键的value值，从start到end的子字符串                      | key:键名；start：起始索引；end:终止索引                      | redis.getrange('name', 1, 4)                     | 返回键为name的值的字符串，截取索引为 1~4 的字符 | b'ello'                                                      |

##### 列表操作

Redis提供了列表存储，列表内的元素可以重复，可以从两端存储

| 方法                      | 作用                                                         | 参数说明                                       | 示例                        | 示例说明                                   | 示例结果         |
| ------------------------- | ------------------------------------------------------------ | ---------------------------------------------- | --------------------------- | ------------------------------------------ | ---------------- |
| rpush(name,*values)       | 在键为name的列表末尾添加值为value的元素，可以传多个          | name:键名 values:值                            | redis.rpush('list',1, 2, 3) | 向键为list的列表尾添加1，2，3              | 3，列表大小      |
| lpush(name,*values)       | 在键为name的列表头添加值为value的元素，values:值可以传多个   | name:键名，values：值                          | redis.lpush('list', 0)      | 向键为list的列表头部添加0                  | 4，列表大小      |
| llen(name)                | 返回键为name的列表的长度                                     | name:键名                                      | redis.llen('list')          |                                            |                  |
| lrange(name, start, end)  | 返回键为name的列表中start至end之间的元素                     | name:键名；start:起始索引；end:终止索引        | redis.lrange(list, 1, 3)    | 返回起始索引为1，终止索引为3范围对应的列表 | [b'3',b'2',b'1'] |
| ltrim(name,start,end)     | 截取键为name的列表，保留索引为start到end的内容               | name：键名;start:起始索引；end:终止索引        | ltrim('list', 1, 3)         | 保留键为list是索引为1到3的元素             | True             |
| lindex(name, index)       | 返回键为name的列表中index位置的元素                          | name:键名  index:索引                          | redis.index('list', 2)      | 返回列表中索引为2的元素                    |                  |
| lset(name, index, value ) | 给键为name的列表中index位置的元素赋值                        |                                                |                             |                                            |                  |
| lrem(name,count, value)   | 删除count个键对应的列表中值为value的元素                     |                                                |                             |                                            |                  |
| lpop(name)                | ==返回并删除==键为name的列表中的==首元素==                   |                                                |                             |                                            |                  |
| rpop(name)                | 返会并删除键为name的列表中的==尾元素==                       |                                                |                             |                                            |                  |
| blpop(keys, timeout=0)    | 返回并删除名称在keys中的list中的首个元素，如果列表为空，则会阻塞 | keys:键列表，timeout:超时等待时间，0为一直等待 |                             |                                            |                  |
| brpop(keys, timeout=0)    | 返回并删除键为name的列表中的尾元素，如果list为空，会一直阻塞， | keys:键列表timeout:超时等待时间，0为一直等待   | redis.brpop('list')         |                                            |                  |
| rpoplpush(src, dst)       | 返回并删除名称为src的列表的尾元素，并将该元素添加到名称为dst的列表头部 | src:源列表的键；dst:目标列表的key              |                             |                                            |                  |

##### 有序集合

有序集合比集合多了一个分数字段，利用它对集合排序

| 方法                                                    | 作用                                                         | 参数说明                            | 示例                          | 示例说明 | 示例结果           |
| ------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------- | ----------------------------- | -------- | ------------------ |
| zadd(name,*args,**args)                                 | 添加元素，score用于排序，存在则更新                          | name:键名,score:分数，member:元素值 | redis.zadd('grade',100,'bob') |          | 返回添加的元素个数 |
| zrem(name, *values)                                     | 删除键为name的zset中的元素                                   | name:键名 values:元素               | redis.zset('grade','Mike')    |          | 返回删除的元素个数 |
| zincrby(name, value, amount=1)                          | 如果在键为name的zset中已经存在元素value,则将该元素的score增加amount，否则向该集合中添加该元素，其score的值为amount | value:元素amount:增长的score值      |                               |          |                    |
| zrank(name, value)                                      | 返会键为name的zset中元素的排名，按score从小到大排序，即==名次== |                                     |                               |          |                    |
| zrevrank(name,value)                                    | 返会键为name的zset中元素的倒数排名                           |                                     |                               |          |                    |
| zrevrange(name,start,end,withscores=Flse)               | 返回键为name的zset中index从start到end的所有元素              |                                     |                               |          |                    |
| zrangebyscore(name,min,max,start=None,withscores=False) | 返回键为name的zset中==score在给定区间的元素==                |                                     |                               |          |                    |
| zcount(name, min, max)                                  | 返回键为name的zset中==score在给定区间的数量==                |                                     |                               |          |                    |
| zcard(name)                                             | 返回键为name的zset的元素个数                                 |                                     |                               |          |                    |
| zremrangebyrank(name,min,max)                           | 删除键为name的zset中排名在给定区间的元素                     |                                     |                               |          |                    |
| zremrangebyscore(name, min,max)                         | 删除键为name的zset中score在给定区间的元素                    |                                     |                               |          |                    |

##### 散列操作

name指定散列表的名称，表内存储各个键值对

| 方法                       | 作用                                             | 参数说明                              | 示例                                       | 示例说明 | 示例结果           |
| -------------------------- | ------------------------------------------------ | ------------------------------------- | ------------------------------------------ | -------- | ------------------ |
| hset(name,key,value)       | 向键为name的散列中添加映射                       | name:键名，key：映射键；value：映射值 | hset('price','cake',5)                     |          | 1,即添加的映射个数 |
| hsetnx(name,key,value)     | 如果映射键名不存在，则向键为name的散列中添加映射 |                                       |                                            |          |                    |
| hget(name, key)            | 返回键为name的散列中key对应的值                  |                                       |                                            |          |                    |
| hmget(name,keys,*agrs)     | 返回键为name的散列中各个键对应的值               |                                       | redis.hmget('price',['apple','orange'])    |          |                    |
| hmset(name,mapping)        | 向键为name的散列中添加映射                       |                                       | redis.hmset('price',{'banana':2,'pear':6}) |          |                    |
| hincrby(name,key,amount=1) | 将键为name的散列中映射的值增加amount             |                                       | redis.hincrby('price','banana')            |          |                    |
| hexists(name,key)          | 键为name的散列中是否存在键名为key的键            |                                       | redis.hexists('price', 'banana')           |          |                    |
| hdel(name, *keys)          | 在键为name的散列中删除键名为key的映射            |                                       | redis.hdel('price', 'banana')              |          |                    |
| hlen(name)                 | 从键为name的散列中获取映射个数                   |                                       |                                            |          |                    |
| hkeys(name)                | 从键为name的散列中获取所有映射键名               |                                       |                                            |          |                    |
| hvals(name)                | 从键为name的散列中获取所有映射键值               |                                       |                                            |          |                    |
| hgetall(name)              | 获取所有键值对                                   |                                       |                                            |          |                    |

##### RedisDump

redisdump提供了强大的redis数据的导入和导出功能

首先安装RedisDump

提供了两个命令：redis-dump用于导出数据；redis-load用于导入数据

- redis-dump

  redis-dump -h 查看所有可选项

- redis-load

  redis-load -h











## 第六章 Ajax数据爬取

有时候requests获取页面的时候，得到的结果和浏览器不一致，因为requests获取的是原始的html文档，浏览器中的页面是经过javascript处理过的，这些数据来源有多种，可能是通过ajax加载，可能是含在html文档中，可能是经过javascript和特定算法后生成的。

ajax:数据是异步加载方式，最初页面不包含某些数据，原始页面加载完后，会再向服务器请求某个接口获取数据

这样在web上可以做到前后端分离，降低服务器直接渲染页面带来的压力。

解决方法：分析网页后台向接口发送的ajax请求，用requests模拟ajax请求

### 什么是Ajax

Ajax,全称 Asynchronous JavaScript and Xml,即异步的javascript 和 xml,利用JavaScript在保证页面不被刷新、页面链接不改变的情况下于服务器交换数据并更新部分网页的技术。

传统网页要更新其内容，必须刷新整个页面，有了Ajax，便可以在页面不被刷新的情况下更新其内容。页面实际是在后台于服务器进行了数据交换，获取数据后，通过javascript改变网页

#### 基本原理：

ajax 请求到网页更新过程：

​	==发送请求---解析内容---渲染网页==

- 发送请求：

  javascript可以实现页面交互功能，这里请求是javascript发送的

- 解析内容

  返回内容可能是html,可能是json,接下来只需在javascript中处理即可

- 渲染网页

  比如通过`document.getElementById().innerHTML`可以对某个元素内的源代码进行更改，这样的操作也称为DOM操作，即对Document网页进行操作（更改，删除等）

要获取这些数据，需要知道，请求怎么发的，发往哪里，发了哪些参数，知道这些，就可用python模拟发送获取结果

#### Ajax分析方法：

借助浏览器的开发者工具，在Network选项卡刷新页面，可以看到页面加载过程中浏览器和服务器之间发送请求和接受响应的所有记录

ajax有其特殊的请求类型==xhr==(XML HTTP Request)

![014](D:\project\pycon\web scrapy\img\014.png)

打开微博向下滑动网页，在network下找到ajax链接，选中后在headers选项的request headers对象中可以看到__X-Requested-With:XMLHttpRequest__,标记了此请求是ajax请求，javaScript接受数据后，执行相应的渲染方法，页面就出来了

#### 过滤请求

chrome开发者工具中network下的xhr选项可以筛选出所有的ajax请求

![015](D:\project\pycon\web scrapy\img\015.png)

### Ajax爬取今日头条关键字图片

在网页源代码中搜索关键字发现没有或只有不符合条件的一两条，可以初步断定是ajax加载

接下来我们切换到XHR过滤选项卡进行查看分析

#### 保存图片

获取图片的二进制数据并写入文件，图片的名称可以使用内容的MD5值，用于去重

```python
import hahslib

def img_id(img_content):
    '''用图片内容的md5值作为图片名，用于去重'''
    # 将数据生成128位的二进制串
    img_name = hashlib.md5(img_content)
    # 十六进制显示二进制数据
    img_name = img_name.hexdigest()
```

#### 利用线程池实现多线程下载
```
# 打包页面图片抓取
def main(offset):
    pageUrls = get_ajax_url(base, offset, keyword='街拍')
    for pageurl in pageUrls:
        get_page(pageurl)
        time.sleep(random.uniform(1,3))


if __name__ == '__main__':
    # Apply func to each element in iterable, collecting the results in a list that is returned.
    pool = Pool()
    groups = (i*20 for i in range(100))
    # 传入函数和参数
    pool.map(main, groups)
    # close要在join之前调用
    pool.close()
    # 让主线程等待子线程结束
    pool.join()
```
http://codingdict.com/questions/1325
- Pool有一个processes参数，这个参数可以不设置，如果不设置函数会跟根据计算机的实际情况来决定要运行多少个进程，我们也可自己设置，但是要考虑自己计算机的性能




## 第七章 动态渲染页面爬取

ajax也是javaScript动态渲染页面的一种，简单的情形可以通过requests和urllib实现

对于比较复杂的网页，有些图形是经过javascript计算生成，淘宝的页面即使是ajax获取数据，其接口含有很多加密参数，难以找出规律

对于这种我们可以模拟浏览器运行的方式来解决，这样我们就不用管网页内部的javascript用了什么算法渲染页面，不用管后台ajax接口到底有那些参数，在浏览器中看到什么，抓取的源码就是什么，可见即可爬

python提供了许多模拟浏览器的库，如 Selenium（硒）、splash、PyV8、Ghost等，本章主要学习Selenium和Splash的用法

### 7.1Selenium
Selenium是一个自动化测试工具，可以驱动浏览器执行特定的动作，如点击、下拉等，同时还可以获取浏览器当前呈现页面的源代码，做到可见即可爬，对于一些JavaScript动态渲染的页面，这种方式非常有效
#### 准备工作
确保安装了Chrome浏览器并配置号了ChromeDriver,另外还需安装Python的Selenium库
- 安装selenium :`pip install selenium`

- 验证安装: `import selenium`

- 安装ChromeDriver:
  - 查看浏览器版本号
  
  - 下载对应版本的ChromeDriver
  
  - 将存放的路径加入环境变量
  
  - cmd中输入 chromedriver 弹出证明环境变量配置完成
  
    ![017](D:\project\pycon\web scrapy\img\017.png)
  
  - 随后再python窗口中写入
  
    ```python
    from selenium import webdriver
    browser = webdriver.Chrome()
    ```
  
    运行后弹出空白的Chrome则证明配置完成
  
- 对于Firefox 浏览器，要安装GeckoDriver

  ### PhantomJS的安装   （phantom---幽灵）

  PhantomJS是一个无界面的、可脚本编程的WebKit浏览器引擎，原生支持多种Web标准，DOM操作、CSS选择器、JSON、Canvas、SVG

  selenium支持phantomjs,这样运行的时候就不会出现一个浏览器了，PJS的运行效率高，支持各种参数配置
#### 基本使用
用selenium驱动加载网页的话，就可以拿到js渲染的结果了

- 声明浏览器对象

  selenium支持多种浏览器，如chrome、Firefox、Edge等, 初始化浏览器

  ```python
  from selenium import webdriver
  
  browser = webdriver.Chrome()
  browser = webdriver.Firefox()
  browser = webdriver.Edge()
  browser = webdriver.PhantomJS()
  browser = webdriver.safari()
  ```

- 访问页面

  使用get方法请求，传入url即可

  ```python
  browser.get('https://www.taobao.com')
  print(browser.page_source)
  browser.close()
  ```

- 查找节点

  selenium可以驱动浏览器完成各种操作，比如填充表单、模拟点击。

  - 单个节点

    ```python
    browser.get('https://www.taobao.com')
    input_first = browser.find_element_by_id("q")
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first, input_second, input_third, sep='\n')
    browser.close()
    ```

    ```
    DevTools listening on ws://127.0.0.1:1875/devtools/browser/0b0305ed-40ab-4144-b56b-545369ad6cce
    <selenium.webdriver.remote.webelement.WebElement (session="9834e05b5c3ccfb072b85d95a478ab0c", element="2ed8b6fa-c2ca-44ae-9d9d-dac3a2b53f85")>
    <selenium.webdriver.remote.webelement.WebElement (session="9834e05b5c3ccfb072b85d95a478ab0c", element="2ed8b6fa-c2ca-44ae-9d9d-dac3a2b53f85")>
    <selenium.webdriver.remote.webelement.WebElement (session="9834e05b5c3ccfb072b85d95a478ab0c", element="2ed8b6fa-c2ca-44ae-9d9d-dac3a2b53f85")>
    ```

    获取方法：

    - find_element_by_id
    - find_element_by_name
    - find_element_by_xpath
    - find_element_by_link_text
    - find_element_by_partial_link_text
    - find_element_by_tag_name
    - find_element_by_class_name
    - find_element_by_css_selector

    还提供了find_element() 方法，需要传入查找方式by和值

    就是find_element_by_xxx这中方法的函数版本，`find_element(By.ID, id)`

  - 多个节点

    如果查找目标有多个节点要使用find_elements()方法

    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    
    # 生成浏览器对象
    browser = webdriver.Chrome()
    # 发起请求
    browser.get('https://www.taobao.com/')
    # 获取对象
    # lis = browser.find_elements(By.XPATH, '//ul[@class="service-bd"]//a')
    lis = browser.find_elements(By.CSS_SELECTOR, 'ul.service-bd li a')
    print(lis)
    browser.close()
    ```

    获取方法：

    - find_elements_by_id
    - find_elements_by_name
    - find_elements_by_xpath
    - find_elements_by_link_text
    - find_elements_by_partial_link_text
    - find_elements_by_tag_name
    - find_elements_by_class_name
    - find_elements_by_css_selector

    也可以使用find_elements()方法来传参

- 节点交互

  Selenium可以驱动浏览器来执行一些操作，常见 的用法有：输入文字时用 send_keys（）方法，清空文字时用 clear（）方法，点击按钮时用 click（）方法

  ```python
  # 打开网站，find_element获取输入框，send_keys输入文字，find_elements获取搜索结果，click完成搜索
  
  from selenium import webdriver
from selenium.webdriver.common.by import By
  import time
  
  brower = webdriver.Chrome()
  brower.get('https://www.taobao.com')
  input = brower.find_element(By.ID, 'q')
  input.send_keys('灯具')
  time.sleep(2)
  input.clear()
  input.send_keys('iPad')
  button = brower.find_element(By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')
  button.click()
  ```

- 动作链

  之前的交互动作针对的是单个节点执行，比如，输入框，我们就调用输入文字和清空文字的方法，对于按钮，我们调用点击方法

  还有一些操作，没有特定的执行对象，比如拖拽鼠标，键盘按钮等，需要另外一种方式执行——动作链

- 执行js

  对于某些操作，selenium没有提供api,比如下拉进度条，可以直接模拟javaScript

  使用execute_script() 实现

  ```python
  from selenium import webdriver
  
  browser = webdriver.Chrome()
  browser.get('https://www.zhihu.com/explore')
  browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  browser.execute_script('alert("To Bottom")')
  ```

  **scrollTo(*xpos,ypos*)**

  browser.maximize_window()

- 获取节点信息

  page_source获取网页的源代码，接着就可以使用解析库来提取信息了

  selenium提供了节点选择方法，返回webElement类型，也有相关的方法和属性来提取节点信息，如属性和文本，这样就不用通过解析源代码来提取信息了

  - 获取属性

    使用get_attribute()获取节点属性

    ```
    logo = browser.find_element_by_css_selector('a[aria-label="知乎"] > svg')
    print(logo.get_attribute('width'))
    ```

  - 获取文本

    每个webelement都有==text==属性，直接调用获取内部文本信息

    相当于BeautifulSoup的get_text() 和 pyquery 的text()方法

    ```
    button = browser.find_element_by_css_selector('a.ExploreSpecialCard-title')
    print(button.text)
    ```

  - 获取id、位置、标签名和大小

    webElement还有其他的属性，比如location获取节点在页面相对位置，tab_name获取标签名称，size属性可以获取节点大小（宽高），这些属性有时候很有用

    ```python
    button = browser.find_element_by_css_selector('a.ExploreSpecialCard-title')
    print(button.text)
    # button.click()
    print(button.id)
    print(button.location)
    print(button.size)
    print(button.tag_name)
    
    >>>
    电竞每日赛事速递
    303c2e9b-a1ad-48a9-86b8-256f84ba7515
    {'x': 534, 'y': 374}
    {'height': 28, 'width': 330}
    a
    ```

- 切换frame

  

[参数](https://zhuanlan.zhihu.com/p/60852696)






## 第八章 验证码识别



## 第九章 代理的使用



## 第十章 模拟登录



## 第十一章 App的爬取



## 第十二章 pyspider 框架的使用



## 第十三章 Scrapy 框架的使用



## 第十四章 分布式爬虫



## 第十五章 分布式爬虫的部署









### aiohttp

requests库是一个阻塞式HTTP请求库，发出请求后，程序会一直等待服务器响应，直到响应后才会进行下一步处理，这个过程比较耗时。如果程序再这个过程中做些其他的事情，比如请求的调度，响应的处理，那么爬取效率会大大提升。

aiohttp就是一个这样提供异步web服务的库，从py3.5开始，加入了async/await关键字，使得回调的写法直观和人性化，aiohttp异步操作借助async/await关键字的写法更加简洁。

用法：维护一个代理池时，利用异步的方式检测大量代理的运行状况，极大提升效率

- 安装：`pips install aiohttp`

  - 官方推荐安装：字符编码检测库cchardet、加速DNS 的解析库 aiodns

    `pips install cchardet aiodns`

- 测试安装：

  `import aiohttp`