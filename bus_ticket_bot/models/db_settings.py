from peewee import SqliteDatabase

from bus_ticket_bot.config.settings import DATABASE_PATH

db = SqliteDatabase(DATABASE_PATH, pragmas={"foreign_keys": 1})
