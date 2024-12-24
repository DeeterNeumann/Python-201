'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:PASSWORD@localhost/sakila")
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload_with = engine)

pprint(film.columns.keys())
pprint(repr(metadata.tables['film']))



