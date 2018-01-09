#!/usr/bin/python

import sqlite3

class FitStudioDB:
    """Class that controls access to SQLite DB."""

    name = "fitstudio.db"
    connection = sqlite3.connect(name)
    cursor = connection.cursor()

    def __init__(self, dbName):
        self.name = name
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.connection.close()

    def createDB(self):
        cursor.execute("CREATE TABLE coach(name TEXT NOT NULL, alias TEXT,
                description TEXT)")
        connection.commit()

    def addCoach(self, name, alias, description):
        cursor.execute("INSERT INTO coach VALUES(name, alias, description)")

