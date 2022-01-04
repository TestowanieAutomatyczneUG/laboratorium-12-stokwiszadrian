class Subscriber:
    def __init__(self):
        self.clients = []

    def addClient(self, client: str):
        if not isinstance(client, str):
            raise Exception("Client must be a string")
        elif client in self.clients:
            raise Exception("Client already in the database")
        else:
            self.clients.append(client)
            return client

    def deleteClient(self, client: str):
        if not isinstance(client, str):
            raise Exception("Client must be a string")
        elif client not in self.clients:
            raise Exception("Client doesn't exist in the database")
        else:
            self.clients.remove(client)
            return client

    def messageClient(self, client: str, msg: str):
        if not isinstance(client, str):
            raise Exception("Client must be a string")
        elif client not in self.clients:
            raise Exception("Client doesn't exist in the database")
        elif not isinstance(msg, str):
            raise Exception("Message must be a string")
        else:
            pass
