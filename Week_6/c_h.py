def command_hendler(string):
    data_list = string.replace("ok\n","").replace("\n\n","").split()
    print(data_list)
    try:
        if data_list[0] == "put":
            print("It's put")
            print(_put(data_list))
        elif data_list[0] == "get":
            print("It's get")
            print(_get(data_list))
        else:
            print("error\n wrong command")
    except IndexError:
        raise ServerError("error\nwrong command\n\n")

class ServerError(Exception):
    pass

def _put(string):
        """Convert inner string to dictionary"""
        val = (int(string[3]), float(string[2]),)
        if string[1] in new_dict:
            new_dict[string[1]].append(val)
        else:
            new_dict[string[1]] = [val]
        return "ok\n\n"

def _get(string):
    message = "ok\n"
    if string[1] == "*":
        for key, value in new_dict.items():
            for val in value:
                message += "{} {} {}\n".format(key, val[0], val[1])
    else:
        value = new_dict.get(string[1], "\n")
        if value != "\n":
            for val in value:
                message += "{} {} {}\n".format(string[1], val[0], val[1])
        else:
            message += value

    return message






# new_dict = dict()
new_dict = {'palm.cpu':[(1150864247, 0.5),(1150864248, 0.5)],'eardrum.cpu':[(1150864250, 3.0),(1150864251, 4.0)],'eardrum.memory':[(1503320872, 4200000.0)]}


if __name__ == "__main__":
    command_hendler("put palm.cpu 1501864247\n")