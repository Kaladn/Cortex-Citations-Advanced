import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DATABASE_PATH = 'citations.db'

def connect_db():
    """
    Establishes a connection to the SQLite database and returns the connection and cursor.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        logging.info(f"Connected to database at {DATABASE_PATH}")
        return conn, cur
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        return None, None

def create_tables(cur):
    """
    Creates the necessary tables in the database if they do not exist.
    """
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS citations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT,
                title TEXT,
                year TEXT,
                journal TEXT,
                publisher TEXT
            )
        ''')
        logging.info("Tables created successfully or already exist.")
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")

def create_citation(cur, conn, entities):
    """
    Inserts a new citation into the database.
    """
    try:
        cur.execute('''
            INSERT INTO citations (author, title, year, journal, publisher)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            entities.get('author'), 
            entities.get('title'), 
            entities.get('year'), 
            entities.get('journal'), 
            entities.get('publisher')
        ))
        conn.commit()
        citation_id = cur.lastrowid
        logging.info(f"Citation inserted with ID: {citation_id}")
        return citation_id
    except sqlite3.Error as e:
        logging.error(f"Error inserting citation: {e}")
        return None

if __name__ == "__main__":
    # Example Usage
    conn, cur = connect_db()
    if conn and cur:
        create_tables(cur)
        
        # Example citation entities
        entities = {
            "author": "Doe, J. and Smith, A.",
            "title": "The Impact of AI on Society",
            "year": "2022",
            "journal": "Journal of Artificial Intelligence",
            "publisher": None
        }
        
        # Insert citation
        citation_id = create_citation(cur, conn, entities)
        print(f"Inserted Citation ID: {citation_id}")
        
        cur.close()
        conn.close()
