def opening():
    command = input("Welcome! Press C to connect to the chat server, or Q to quit -> ")
    while True:
        if command == 'C':
            print("Great! Have fun!")
            return 1
        elif command == 'Q':
            print("OK, Bye!")
            exit()
        else:
            command = input("Bad input. Please try again -> ")


def ending():
    pass

