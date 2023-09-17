import socket
import msgSocket
import threading
from addressBook import AddressBook
from msgSocket import MsgSocket


def check_user_validity(address_book, username):
    return username in address_book.book['UserName']


def handle_new_clients(client_sock: MsgSocket, book: AddressBook):
    """
    UNDER CONSTRUCTIONS
    :param client_sock:
    :param book:
    :return:
    """
    rec = client_sock.receive_text()
    while not check_user_validity(address_book=book, username=rec):
        # send the recipient an error msg and try again
        pass
    while True:
        msg_received = client_sock.receive_msg()
        # CHECK IF REC == MSG_RECEIVED.RECIPIENT


def handle_chat():
    """
    UNDER CONSTRUCTIONS
    This function will get 2 clients, receive a msg from one and send to the other
    :return:
    """
    pass


def server_program():
    """
    UNDER CONSTRUCTIONS
    The main program
    :return:
    """
    users_book = AddressBook()
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = msgSocket.MsgSocket(is_server=True)
    server_socket.bind(host, port)

    server_socket.listen(5)

    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))

        threading.Thread(target=handle_new_clients, args=(conn, users_book))

        # received = server_socket.receive_msg()
        # print("from client:")
        # print(received)
        # server_socket.send_msg("hello client", "server", "client")

    conn.close()


if __name__ == '__main__':
    server_program()
