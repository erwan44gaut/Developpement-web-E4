import hashlib

class Config:
    DATABASE = '../db/database.db'
    SECRET_KEY = 'ThomasLeRageux'
    SECRET_KEY_HASH = hashlib.md5(SECRET_KEY.encode()).hexdigest()
