from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('wines.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    password = CharField(unique=True)
    image = CharField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    print("TABLES Created")
    DATABASE.close()