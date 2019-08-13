import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',6666))
print('服务器已启动...')

# 从客户端接收数据
data,client_address=s.recvfrom(1024)                    # 注意服务器地址是个元组，包含IP和端口
print('从客户端发来的数据是：%s' % data.decode())

# 发送数据给客户端
msg2='你好呀！'
s.sendto(msg2.encode(),client_address)
print('向客户端发送的数据是：%s' %msg2)
s.close()