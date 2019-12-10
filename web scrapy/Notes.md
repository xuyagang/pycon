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

  - 之间附加到链接中`r = requests.get('http://httpbin.org/get?name=adam&age=22')`

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

  



















