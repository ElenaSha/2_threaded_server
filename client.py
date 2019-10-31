import socket
from time import sleep 


sock = socket.socket()
sock.setblocking(1)

host = 'localhost'
msg = ""

mark = 0
#проверка порта
while mark == 0:
	print("Введите номер порта")
	port = int(input())
	if 1024<=port<=49151:
		mark = 1
		break
	else:
		print("Ошибка ввода. Номер порта должен принадлежать промежутку [1024;49151]")
		print("Если вы хотите еще раз ввести номер порта, введите 1. Если нет - любую другую строку.")
		ind = input()
		if ind != "1":
			port = 1024
			mark = 1

sock.connect((host, port))
print("Соединение с сервером")

while (msg != "exit"):

	msg = input()

	print("Отправка данных серверу")
	sock.send(msg.encode())

	print("Прием данных от сервера")

	#data = sock.recv(1024)

	data = sock.recv(1024)
	print(data.decode())
	print("Если вы хотите прервать соединение с сервером, введите \"exit\"")
	
	if msg == "exit":
		sock.close()