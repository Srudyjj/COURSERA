import os
import tempfile
import argparse
from collections import OrderedDict
import json
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
answer = [args.key ,args.val]
print(answer)

def store(st, key, val):
	store_dict = OrderedDict(st)
	if key in store_dict:
		store_dict[key].append(val)
	else:
		store_dict[key] = [val]
	return store_dict
	
print(store({'name':['Alex'], 'surname':['Alexsandr'], 'nick':['Alex444']}, args.key, args.val))
	
	
"""
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
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





