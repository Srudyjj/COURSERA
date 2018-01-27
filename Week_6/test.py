def _put(string):
        """Convert inner string to dictionary"""
        val = (int(string[3]), float(string[2]),)
        print(val)
        if string[1] in new_dict:
            k = new_dict[string[1]]
            if string[3] in k[0]:
                a = new_dict[string[1]]
                print(a)
                b = a.index(val)
                a.pop(b)
                print(new_dict)
                new_dict[string[1]].append(val)
            else:
                new_dict[string[1]].append(val)
                print(new_dict)
        else:
            new_dict[string[1]] = [val]
            print(new_dict)
        return "ok\n\n"


new_dict = {'eardrum.memory': [(1517063008, 4200000.0)],
            'eardrum.cpu': [(1150864250, 3.0)],
            'palm.cpu': [(1150864247, 0.5),
                         (1150864248, 2.0)]}


_put(['put', 'eardrum.memory', 4200000.0, 1517063008])
