import socket
import msgSocket
import threading
from addressBook import AddressBook
from msgSocket import MsgSocket


def check_user_validity(address_book, username):
    return username in address_book.book['UserName']


def handle_new_clients(client_sock: MsgSocket, client_address: str, book: AddressBook, lock: threading.Lock):
    """
    UNDER CONSTRUCTIONS
    :param client_sock:
    :param client_address:
    :param book:
    :param lock:
    :return:
    """
    # rec = client_sock.receive_text()
    # while not check_user_validity(address_book=book, username=rec):
    #     # send the recipient an error msg and try again
    #     pass
    while True:
        lock.acquire()
        msg_received = client_sock.receive_msg()
        # CHECK IF REC == MSG_RECEIVED.RECIPIENT
        print("from " + str(client_address) + ": ", str(msg_received))
        # print(msg_received)
        server_response = input(">> ")
        client_sock.send_msg(server_response, "server", client_address)
        lock.release()
    client_sock.close()


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
    lock = threading.Lock()
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))

        client_handling = threading.Thread(target=handle_new_clients, args=(conn, address, users_book, lock))
        client_handling.start()
        # received = server_socket.receive_msg()
        # print("from client:")
        # print(received)
        # server_socket.send_msg("hello client", "server", "client")

    conn.close()


if __name__ == '__main__':
    server_program()
