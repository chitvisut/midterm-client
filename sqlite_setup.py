import sqlite3

con = sqlite3.connect("midterm.db")
cur = con.cursor()

cur.execute(''' CREATE TABLE data (
                        uuid TEXT PRIMARY KEY UNIQUE,
                        author TEXT NOT NULL,
                        message TEXT NOT NULL,
                        likes INTEGER NOT NULL
                        )''')

cur.execute(''' CREATE TABLE count (
                        mark TEXT PRIMARY KEY UNIQUE,
                        count INTEGER NOT NULL
                        )''')

cur.execute("INSERT INTO count VALUES ('current', 0)")
con.commit()


if __name__ == "__main__":

    print("SQLite Set up complete!")