from peewee import *
from flask_login import UserMixin

# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('wine_app')

class BaseModel(Model):
	"""A base Model that will use our psql database"""
	class Meta: database = DATABASE



class User(UserMixin, BaseModel):
    username = CharField(unique=True)
    password = CharField(unique=True)
    profile_img = CharField()


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    print("TABLES Created")
    DATABASE.close()