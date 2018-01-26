import asyncio



def run_server(host, port):
    loop = asyncio.get_event_loop()
    # Each client connection will create a new protocol instance
    coro = loop.create_server(EchoServerClientProtocol, host, port)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


def command_hendler(string):
    data_sring = string.replace("ok\n","").replace("\n\n","").split()
    print(data_sring)
    try:
        if data_sring[0] == "put":
            print("It's put")
        elif data_sring[0] == "get":
            print("It's get")
        else:
            print("error\n wrong command")
    except IndexError:
        raise ServerError("error\nwrong command\n\n")


def _parser(self, inner_message):
        """Convert inner bite string to dictionary"""
        inner = inner_message.decode("utf8")
        new_dict = dict()
        try:
            if inner == 'ok\n\n':
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
        except IndexError:
            raise ServerError("error\nwrong command\n\n")

def get(self, key):
        try:
            with socket.create_connection((self.host, self.port),self.timeout) as sock:
                message = 'get {}\n'.format(key)
                sock.sendall(message.encode("utf8"))
                received_data = sock.recv(1024)
                return self._parser(received_data)
        except socket.error:
            raise ServerError("error\nwrong command\n\n")

def put(self, key, value, timestamp=curent_time):
        try:
            with socket.create_connection((self.host, self.port),self.timeout) as sock:
                message = 'put {} {} {}\n'.format(key, value, int(timestamp))
                sock.sendall(message.encode("utf8"))
                received_data = sock.recv(1024)
                return received_data.decode("utf8")
        except socket.error:
            raise ServerError("error\nwrong command\n\n")    

class ServerError(Exception):
    pass


class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        


if __name__ == "__main__":
    run_server("127.0.0.1", 8888)