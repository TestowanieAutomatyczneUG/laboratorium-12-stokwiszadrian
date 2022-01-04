from src.MailServer import MailServer
from src.TemplateEngine import TemplateEngine

class Messenger:
    def __init__(self):
        self.template_engine = TemplateEngine()
        self.mail_server = MailServer()

    def sendMessage(self, client, message):
        if not isinstance(client, str):
            raise Exception("Client must be a string")
        elif not isinstance(message, str):
            raise Exception("Message must be a string")
        else:
            data = self.template_engine.new_message(client, message)
            self.mail_server.send_message(client, data)
            return f"Message has ben sent to ${client}"

    def receiveMessage(self, client):
        if not isinstance(client, str):
            raise Exception("Client must be a string")
        else:
            data = self.mail_server.get_message(client)
            return f"Received message from ${client}: ${data}"
