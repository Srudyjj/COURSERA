import os
import tempfile
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
answer = [args.key ,args.val]
print(answer)


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
print(storage_path)
with open(storage_path, 'w') as f:
    pass
