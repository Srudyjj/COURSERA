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

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))
        message_received = command_hendler(message)
        print('Send: {!r}'.format(message_received))
        self.transport.write(message_received.encode("utf8"))
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def command_hendler(string):
    data_list = string.replace("ok\n","").replace("\n\n","").split()
    print(data_list)
    try:
        if data_list[0] == "put":
            print("It's put")
            return _put(data_list)
        elif data_list[0] == "get":
            print("It's get")
            return _get(data_list)
        else:
            return "error\n wrong command"
    except IndexError:
        raise ServerError("error\nwrong command\n\n")
        

class ServerError(Exception):
    pass

def _put(string):
        """Convert inner string to dictionary"""
        val = (int(string[3]), float(string[2]),)
        print(val)
        if string[1] in new_dict:
            k = new_dict[string[1]]
            if string[3] in k[0]:
                a = new_dict[string[1]]
                b = a.index(val)
                a.pop(b)
                new_dict[string[1]].append(val)
            else:
                new_dict[string[1]].append(val)
        else:
            new_dict[string[1]] = [val]
        return "ok\n\n"

def _get(string):
    message = "ok\n"
    if string[1] == "*":
        for key, value in new_dict.items():
            for val in value:
                message += "{} {} {}\n".format(key, val[1], val[0])
    else:
        value = new_dict.get(string[1], "\n")
        if value != "\n":
            for val in value:
                message += "{} {} {}\n".format(string[1], val[1], val[0])
        else:
            message += value

    return message

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
new_dict = {}

if __name__ == "__main__":
    run_server("127.0.0.1", 8888)