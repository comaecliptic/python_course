import sqlite3
import pandas as pd


conn = sqlite3.connect('test.db')
conn.execute('PRAGMA foreign_keys = ON;')

conn.execute('''CREATE TABLE IF NOT EXISTS artists (
    artist_id INTEGER PRIMARY KEY,
    artist_name TEXT,
    genre TEXT
)''')

conn.execute('''CREATE TABLE IF NOT EXISTS albums (
    album_id INTEGER PRIMARY KEY,
    album_name TEXT,
    issue_year INTEGER
)''')

conn.execute('''CREATE TABLE IF NOT EXISTS mapping (
    mapping_id INTEGER PRIMARY KEY,
    artist_id INTEGER,
    album_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id) ON DELETE CASCADE,
    FOREIGN KEY (album_id) REFERENCES albums (album_id) ON DELETE CASCADE
)''')

artists = [
    ('Opeth', 'progressive death metal'),
    ('Haken', 'heavy prog'),
    ('Tiamat', 'gothic rock'),
    ('Summoning', 'atmospheric black metal'),
    ('Between the Buried and Me', 'technical death metal'),
    ('Sigh', 'avant-garde black metal'),
    ('Ayreon', 'progressive metal')
]

albums = [
    ('Ghost Reveries', 2005),
    ('Blackwater Park', 2001),
    ('Oath Bound', 2006),
    ('Heir To Despair', 2018),
    ('In Somniphobia', 2012),
    ('Imaginary Sonicscape', 2001),
    ('Coma Ecliptic', 2015),
    ('The Parallax II: Future Sequence', 2012),
    ('The Great Misdirect', 2009),
    ('Colors', 2007),
    ('Prey', 2003),
    ('A Deeper Kind of Slumber', 1997),
    ('The Source', 2017),
    ('The Human Equation', 2004),
    ('Into the Electric Castle', 1998),
    ('Aquarius', 2010),
    ('Visions', 2011),
    ('The Mountain', 2013)
]

query = 'INSERT INTO artists (artist_name, genre) VALUES (?, ?)'
conn.executemany(query, artists)
query = 'INSERT INTO albums (album_name, issue_year) VALUES (?, ?)'
conn.executemany(query, albums)

mapping = [
    (1, 1), (1, 2), (4, 3), (6, 4), (6, 5), (6, 6),
    (5, 7), (5, 8), (5, 9), (5, 10), (3, 11), (3, 12),
    (7, 13), (7, 14), (7, 15), (2, 16), (2, 17), (2, 18)
]

query = 'INSERT INTO mapping (artist_id, album_id) VALUES (?, ?)'
conn.executemany(query, mapping)
conn.commit()

print('First look:')
query = '''SELECT artist_name, album_name FROM mapping
JOIN artists USING (artist_id)
JOIN albums USING (album_id)
'''
res = conn.execute(query)
for row in res.fetchall():
    print(row)

# Now, we discover that Opeth is death metal no more. Too bad.((
conn.execute('UPDATE artists SET genre="progressive rock" WHERE artist_name="Opeth"')
# Then we don't want to see albums after 2010
conn.execute('DELETE FROM albums WHERE issue_year > 2010')
conn.commit()

print('Second look:')
query = '''SELECT artist_name, album_name FROM mapping
JOIN artists USING (artist_id)
JOIN albums USING (album_id)
'''
res = conn.execute(query)
for row in res.fetchall():
    print(row)

conn.close()
