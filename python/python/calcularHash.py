import hashlib

with open(file,"rb") as f:
    hash = hashlib.sha256(f.read()).hexdigest()
    print(hash)