import datetime


class Message:
    def __init__(self, content: str, sender: str, recipient: str):
        self.content = content
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.meta_data = {'sender': sender, 'recipient': recipient, 'time': current_time}

    def __str__(self):
        return self.content

    def get_sender(self) -> str:
        return self.meta_data['sender']

    def get_recipient(self) -> str:
        return self.meta_data['recipient']

    def get_message_time(self) -> str:
        return self.meta_data['time']


"""
notes:
with pickle module, sent the entire message object (dumps and loads)
"""