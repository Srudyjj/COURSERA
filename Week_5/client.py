import time

class Client:
    curent_time = time.time()
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def get(key):
        pass

    def put(key, value, timestamp=time.time()):
        pass


class ClientError():
    pass

        