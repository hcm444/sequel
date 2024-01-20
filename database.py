import sqlite3

# Function to create a database and populate it with movie data
def create_and_populate_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    # Create a movies table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT,
            release_year INTEGER,
            rating REAL
        )
    ''')

    # Sample movie data
    movies_data = [
        ('Inception', 'Sci-Fi', 2010, 8.8),
        ('The Shawshank Redemption', 'Drama', 1994, 9.3),
        ('The Dark Knight', 'Action', 2008, 9.0),
        ('Pulp Fiction', 'Crime', 1994, 8.9),
        ('Forrest Gump', 'Drama', 1994, 8.8),
        ('The Matrix', 'Action', 1999, 8.7),
        ('The Godfather', 'Crime', 1972, 9.2),
        ('Titanic', 'Romance', 1997, 7.8),
        ('Avatar', 'Sci-Fi', 2009, 7.8),
        ('Jurassic Park', 'Adventure', 1993, 8.1),
    ]

    # Insert movie data into the movies table
    cursor.executemany('INSERT INTO movies (title, genre, release_year, rating) VALUES (?, ?, ?, ?)', movies_data)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_and_populate_database()
    print('Database created and populated with movie data.')
