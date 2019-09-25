import os
import sys
sys.dont_write_bytecode = True
class appConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

Config = appConfig