import socket
import _thread

HOST = "127.0.0.1"  # Endereco IP do S
PORT = 5000  # Porta que o Servidor esta


def receber_mensagem(udp):
    while True:
        msg, cliente = udp.recvfrom(1024)
        msg_decoded = msg.decode("utf-8")
        print(f"{cliente} {msg_decoded}")


def client():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", PORT))
    _thread.start_new_thread(receber_mensagem, (udp,))
    dest = (HOST, PORT)
    print("Type q to exit")
    message = None
    while message != "q":
        message = input("-> ")
        udp.sendto(message.encode("utf-8"), dest)
        # data = udp.recv(1024).decode("utf-8")
        # print("Received from server: " + data)
    udp.close()


if __name__ == "__main__":
    client()
