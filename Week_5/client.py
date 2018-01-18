import time
import socket

class Client:
    curent_time = time.time()
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(self, key):
        with socket.create_connection((self.host, self.port),self.timeout) as sock:
            sock.sendall(key.encode("utf8"))
        #print(self.host, self.port ,self.timeout)

    def put(self, key, value, timestamp=curent_time):
        with socket.create_connection((self.host, self.port),self.timeout) as sock:
            message = b'{} {} {}\n'.format(key, value, int(timestamp))
            #print(message)
            sock.sendall(message.encode("utf8"))
        
class ClientError():
    pass


#client = Client("127.0.0.1", 10001, timeout=15)
#client.put("palm.cpu", 0.5)
        