import hashlib
_hash = hashlib.md5()
_hash.update(file('C:\\Users\\x\\Downloads\\python-3.6.4-amd64 (1).exe','rb').read())
print _hash.hexdigest()
