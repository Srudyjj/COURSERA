import os
import tempfile
import argparse
from collections import OrderedDict
import json

#Path to temp directory
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#print(storage_path)

#Take argument from shell
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
answer = [args.key ,args.val]
#print(answer)


def store(st, key, val):
    """Save to dictionary key with value. If key in dictionary, append to list."""
    store_dict = OrderedDict(st)
    if key in store_dict:
        store_dict[key].append(val)
    else:
        store_dict[key] = [val]
    return store_dict


def file_r_w(path, key, val):
    """Open file and write dictionary to file in json_format"""
    if os.path.exists(path)==False:
        with open(path, 'w') as f:
            dictionary=store({}, key, val)
            json.dump(dictionary, f)
    else:
        with open(path, 'r+') as f:
            data = json.load(f)
            with open(path, 'w+') as f:
                json.dump(store(data, key, val), f)
                f.seek(0)

if args.val is None:
    if os.path.exists(storage_path)==False:
        print(None)
    else:
        with open(storage_path, 'r+') as f:
            data = json.load(f)
            smth = (data.get(args.key, None))
            if smth is None:
                print(None)
            else:
                for val in smth:
                    print(val, end=', ')
		
else:
    print(store({'name':['Alex'], 'surname':['Alexsandr'], 'nick':['Alex444']}, args.key, args.val))
    print(file_r_w(storage_path, args.key, args.val))
