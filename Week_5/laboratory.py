inner = "ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n"
# print(inner)
new_dict = dict()
if inner is "ok\n\n":
    print(new_dict)
else:
    new_data1 = inner.replace("ok\n","").replace("\n\n","").splitlines()
    print(new_data1)
    new_data3 = []
    for line in new_data2:
        line1 = line.lstrip().split()
        new_data3.append(line1)
    print(new_data3)
    
    for string in new_data3:
        val = (int(string[2]), float(string[1]),)
        if string[0] in new_dict:
            new_dict[string[0]].append(val)
        else:
            new_dict[string[0]] = [val]

    print(new_dict)



outer = {
    "test": [(1, .5), (2, .4)],
    "load": [(3, 301.0)]
    }