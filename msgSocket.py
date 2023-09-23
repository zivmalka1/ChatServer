import socket
import sys
from message import Message
import struct
import pickle


def get_hostname():
    return socket.gethostname()


class MsgSocket:
    def __init__(self, is_server=False, sock=None):
        self.is_server = is_server
        self.conn = None
        self.address = None
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def bind(self, host, port):
        self.sock.bind((host, port))

    def listen(self, max_clients=5):
        self.sock.listen(max_clients)

    def accept(self):
        conn, address = self.sock.accept()
        self.conn = conn
        self.address = address
        return self, address

    def send_msg(self, content: str, sender: str, recipient: str):
        """
        This method send a message with its metadata.
        socket.sendall() sends all the data to the socket which is connected to a remote machine.
        It will carelessly transfers the data until an error occurs,
        and if it happens then it uses socket.close() method to close the socket'\
        :param content: The message's content
        :param sender: The message's sender (ideally - client's username)
        :param recipient: The message's recipient (ideally - a username)
        :return:
        """
        new_message = Message(content, sender, recipient)
        dumped = pickle.dumps(new_message)

        msg = struct.pack('>I', len(dumped)) + dumped
        # self.sock.sendall(msg)
        # print("msg: ", msg)
        if self.is_server:
            self.conn.sendall(msg)
        else:
            self.sock.sendall(msg)

        # make a return statement for success or exception handling?

    def _receive_all(self, msg_len):
        """
        This method ge a msg length and receives an amount of byte equal to that length.
        :param msg_len: The length of the message to receive
        :return: the message received, or None if EOF is hit.
        """
        msg = bytearray()
        while len(msg) < msg_len:
            if self.is_server:
                packet = self.conn.recv(msg_len - len(msg))
            else:
                packet = self.sock.recv(msg_len - len(msg))
            if not packet:
                return None
            msg.extend(packet)
        return msg

    def receive_msg(self) -> Message:
        """
        This method receives a Message object of any length, and returns it.
        :return: The message received in a form of a Message object.
        """
        encoded_msglen = self._receive_all(4)
        if not encoded_msglen:
            return None
        msg_len = struct.unpack('>I', encoded_msglen)[0]
        # Decode it bacK to a Message object
        return pickle.loads(self._receive_all(msg_len))

    def receive_text(self) -> str:
        """
        this method is supposed to receive an entire text input, which isn't a Message object
        :return: the received text
        """
        encoded_txtlen = self._receive_all(4)
        if not encoded_txtlen:
            return ''
        txt_len = struct.unpack('>I', encoded_txtlen)[0]
        # Decode it bacK to a Message object
        return self._receive_all(txt_len).decode()

    def close(self):
        self.sock.close()





