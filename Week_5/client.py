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
            return self._parser(received_data)
            

    def _parser(self, inner_message):
        """Convert inner bite string to dictionary"""
        inner = inner_message.decode("utf8")
        new_dict = dict()
        if inner is "ok\n\n":
            return new_dict
        else:
            data_sring = inner.replace("ok\n","").replace("\n\n","").splitlines()
            data_list = []
            for line in data_sring:
                splitted_line = line.lstrip().split()
                data_list.append(splitted_line)
            for string in data_list:
                val = (int(string[2]), float(string[1]),)
                if string[0] in new_dict:
                    new_dict[string[0]].append(val)
                else:
                    new_dict[string[0]] = [val]
            return new_dict



            

    def put(self, key, value, timestamp=curent_time):
        with socket.create_connection((self.host, self.port),self.timeout) as sock:
            message = 'put {} {} {}\n'.format(key, value, int(timestamp))
            #print(message)
            sock.sendall(message.encode("utf8"))
            received_data = sock.recv(1024)
            print(received_data.decode("utf8"))            
        
class ClientError():
    pass


client = Client("127.0.0.1", 10001, timeout=150)
print(client.get("*"))
