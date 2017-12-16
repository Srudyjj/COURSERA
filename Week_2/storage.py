import os
import tempfile
import argparse
from collections import OrderedDict
import json

#Path to temp directory
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
print(storage_path)

#Take argument from shell
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
answer = [args.key ,args.val]
print(answer)


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
    with open(path, 'a+') as f:
        fff = f.read()
        print('In file: ', fff)
        if len(fff) < 2:
            print(len(fff))
            dictionary=store({}, key, val)
            f.seek(0)
            json.dump(dictionary, f)
        else:
            data = json.loads(fff)
            with open(path, 'w') as f:
                json.dump(store(data, key, val), f)
        f.close()
print(store({'name':['Alex'], 'surname':['Alexsandr'], 'nick':['Alex444']}, args.key, args.val))
print(file_r_w(storage_path, args.key, args.val))	    

		
		
"""
print(storage_path)

with open(storage_path, 'a') as empty_file:
    pass

if os.stat(storage_path).st_size != 0:
    with open(storage_path) as old_file:
        old_store = json.load(old_file)
        print (old_store)
        store(old_store)
else:
    with open(storage_path, 'w') as new_file:
        new_store=store(new_file)
        json.dump(new_store, new_file)
"""





