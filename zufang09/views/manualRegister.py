import hashlib
import config

password = 'fanxiaoye'
password = hashlib.sha256((config.passwdHashKey + password).encode('utf-8')).hexdigest()
print(password)