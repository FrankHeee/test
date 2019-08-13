# coding=utf-8
import socket

HOST='127.0.0.1'
PORT=6666
sever_address=(HOST,PORT)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg1='你好'
# 向服务器发送信息
s.sendto(msg1.encode(),sever_address)
print('向服务器发送了数据：%s' % msg1)
# 接收服务器返回信息
data,_=s.recvfrom(1024)                     # recvfrom接收的结果是一个元组，第1个元素是数据包data，第2个元素是address，这里用下划线表示不接收
print('从服务器端接收的数据：%s' % data.decode())       #使用decode给二进制数据解码
