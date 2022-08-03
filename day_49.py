# Day 49: Create a Database
# For this challenge, you are going to create a database using
# Python’s SQLite. You will import SQLite into your script. Create a
# database called movies.db. In that database, you are going to
# create a table called movies. In that table, you are going to save
# the following movies:
# 2009 Brothers     Drama
# 2002 Spider-Man   Sci-fi
# 2009 WatchMen     Drama
# 2010 Inception    Sci-fi
# 2009 Avatar       Fantasy
import sqlite3

con = sqlite3.connect('movies.db')
cur = con.cursor()

movies = [  (2009, 'Brothers',      'Drama'),
            (2002, 'Spider-man',    'Sci-Fi'),
            (2009, 'Watch-Man',     'Drama'),
            (2010, 'Inception',     'Sci-Fi'),
            (2009, 'Avatar',        'Fantasy')]
      
cur.execute('DROP TABLE IF EXISTS movies')

cur.execute('CREATE TABLE movies (year,name,genre)')

cur.executemany('INSERT OR IGNORE INTO movies VALUES(?, ?, ?);', movies)

print("table is set")

con.commit()
con.close()

# good to learn execute vs. executemany