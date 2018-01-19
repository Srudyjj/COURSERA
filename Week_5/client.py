import time
import socket
import json

class Client:
    curent_time = time.time()
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        with socket.create_connection((self.host, self.port),self.timeout) as sock:
            message = 'get {}\n'.format(key)
            print(message)
            sock.sendall(message.encode("utf8"))
            received_data = sock.recv(1024)
            #print(received_data.decode("utf8"))
            data = json.loads(received_data.decode("utf8"))
            #print(data, type(data))
            return data

    def put(self, key, value, timestamp=curent_time):
        with socket.create_connection((self.host, self.port),self.timeout) as sock:
            message = 'put {} {} {}\n'.format(key, value, int(timestamp))
            #print(message)
            sock.sendall(message.encode("utf8"))
            
        
class ClientError():
    pass


client = Client("127.0.0.1", 10001, timeout=150)
print(client.get("*"))
        