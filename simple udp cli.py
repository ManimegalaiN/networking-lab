import socket
UDP_IP_ADDRESS="10.1.24.120"
UDP_PORT_NO=6600
Message=("hello,server")
bytesToSend=str.encode(Message)
clientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.sendto(bytesToSend,(UDP_IP_ADDRESS,UDP_PORT_NO))
