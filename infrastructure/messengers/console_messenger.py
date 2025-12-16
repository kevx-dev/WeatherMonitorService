from core.protocols.protocols import MessengerProtocol


class ConsoleMessenger(MessengerProtocol):

    def send_message(self, message:str) -> None:
        print(message)