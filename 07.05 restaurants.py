
import sqlite3


conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT NOT NULL,
    michelin_stars INTEGER,
    rating REAL,
    cuisine TEXT
)
''')
conn.commit()

restaurants = [
    ('Rome, Via Veneto 45', 3, 4.9, 'Italian'),
    ('Florence, Piazza della Signoria 2', 2, 4.7, 'Tuscan'),
    ('Venice, Calle Larga XXII Marzo 2398', 1, 4.4, 'Venetian'),
    ('Milan, Via Monte Napoleone 18', 2, 4.8, 'Lombard'),
    ('Naples, Via Toledo 256', 0, 4.2, 'Neapolitan')
]

cursor.executemany('''
INSERT INTO restaurants (address, michelin_stars, rating, cuisine)
VALUES (?, ?, ?, ?)
''', restaurants)
conn.commit()

cursor.execute('SELECT * FROM restaurants')
for row in cursor.fetchall():
    print(row)

conn.close()


