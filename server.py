import socket
import threading

#для создания потока создадим функцию, отвечающую за обмен информацией с клиентом
def ech(conn,addr):
	print(addr[0])
	msg = ''
	while True:
		data = conn.recv(1024)
		print("Получил инфу")

		if not data:
			break
		elif data == "exit":
			print("Что ж ты, фраер, сдал назад")
			conn.close()
		else:
			msg += data.decode()
			conn.send(data)
			print("Отправил инфу")
	#conn.close()
	print("Пока, клиент")


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
	print(addr[0])
	client_thr = threading.Thread(target = ech, args=[conn,addr]).start()
	print("Поток создан")



sock.close()