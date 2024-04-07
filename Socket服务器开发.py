import socket
# 创建Socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost", 8888))
# 监听端口
socket_server.listen(1)
# listen方法内接受一个整数传参数，表示接受的链接数量
# 等待客户端链接
result: tuple = socket_server.accept()
conn = result[0]    # 客户端和服务器的连接对象
address = result[1]    # 客户端的地址信息
# accept方法返回的是二元元组
# conn, address = socket_server.accept()
# 接受客户端信息，要使用客户端和服务端的本次链接对象，而非socket_server对象
print(f"接收到了客户端的链接，客户端的信息是：{address}")
while True:
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的消息是{data}")
    # recv接受的参数是缓冲区大小，一般给1024即可
    # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法进行UTF-8编码，将字节数组转换为字符串对象
    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息").encode("UTF-8")  # encode可以将字符串编码为字节数组对象
    if msg =="exit":
        break
    conn.send(msg)
# 关闭链接
conn.close()
socket_server.close()
