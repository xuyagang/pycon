# 作为客户端与 HTTP 服务交互
# 使用requests发送请求

# 关于 requests 库，一个值得一提的特性就是它能以多种方式从请求中返回响应结果
# 的内容。从上面的代码来看， resp.text 带给我们的是以 Unicode 解码的响应文本。
# 但是，如果去访问 resp.content ，就会得到原始的二进制数据。另一方面，如果访问
# resp.json ，那么就会得到 JSON 格式的响应内容