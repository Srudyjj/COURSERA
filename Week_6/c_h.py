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
        raise ClientError("error\nwrong command\n\n")

class ClientError(Exception):
    pass



if __name__ == "__main__":
    command_hendler("")