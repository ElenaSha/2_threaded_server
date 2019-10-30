import socket

sock = socket.socket()

port = 1024

while True:
	try:
		sock.bind(('',port))
		break
	except:
			port+=1

print("Порт №", port)

sock.listen(1)
print("Ау")

while True:
	conn, addr = sock.accept()
	print("Поймал клиента")
	print(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		print("Получил инфу")

		if not data:
			break
		else:
			msg += data.decode()
			conn.send(data)
			print("Отправил инфу")

	conn.close()
	print("Пока, клиент")

sock.close()