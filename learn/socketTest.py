import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 1. 与服务器建立连接
    s.connect(("www.seriot.ch", 80))
    # 2. 构建请求行，请求资源是 index.php
    request_line = b"GET /index.php HTTP/1.1"
    # 3. 构建请求首部，指定主机名
    headers = b"Host: seriot.ch"
    # 4. 用空行标记请求首部的结束位置
    blank_line = b"\r\n"

    # 请求行、首部、空行这3部分内容用换行符分隔，组成一个请求报文字符串
    # 发送给服务器
    message = b"\r\n".join([request_line, headers, blank_line])
    s.send(message)

    # 服务器返回的响应内容稍后进行分析
    response = s.recv(1024)
    print(response)
    s.close()


#第二  浏览器访问地址：http://localhost:8000

if __name__ == '__main__':
    PORT = 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', PORT))
    sock.listen(1)
    print('Serving HTTP on port %s ...' % PORT)

    while 1:
        conn, addr = sock.accept()
        print(conn, addr)
        request = conn.recv(1024)
        # HTTP响应消息
        response = "HTTP/1.1 200 OK\nContent-Type:text/html\nServer:myserver\n\nHello, World!\n来了"
        conn.sendall(response.encode(encoding='utf-8'))
        conn.close()



    #第3个
#   mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# mysock.send("GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n")
 
 
# while True:
#     data =mysock.recv(512)
#     if (len(data)<1):
#         break
#     print(data)
 
# mysock.close() 