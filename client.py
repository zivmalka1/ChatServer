import UI
import msgSocket


def client_program():
    # UI.opening()
    host = msgSocket.get_hostname()  # for now, it's the same pc
    server_port = 5000

    client_socket = msgSocket.MsgSocket()  # instantiate
    client_socket.connect(host, server_port)  # connect to the server

    while True:
        user_input = input(">> ")
        client_socket.send_msg(user_input, "client", "server")
        received = client_socket.receive_msg()
        print("from server:", received)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()