import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.create_table() 

    def create_connection(self):
        return sqlite3.connect(self.db_file)

    def create_table(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS images
                          (id INTEGER PRIMARY KEY, keyword TEXT, filename TEXT)''')
        conn.commit()
        conn.close()

    def insert_image_records(self, records):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO images (keyword, filename) VALUES (?, ?)", records)
        conn.commit()
        conn.close()

    def search_image(self, keyword):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT filename FROM images WHERE keyword=?", (keyword,))
        result = cursor.fetchall()
        conn.close()
        return [row[0] for row in result]


if __name__ == "__main__":
    db_file = "image_metadata.db"  # Set the database file name here
    db_manager = DatabaseManager(db_file)
    records = [
        ("dog", "dog5.jpg"),
        ("dog", "dog6.jpg"),
        ("cat", "cat3.jpg"),
        ("cat", "cat4.jpg"),
        ("cat", "cat5.jpg"),
        ("cat", "cat6.jpg"),
        ("horse", "horse3.jpg"),
        ("horse", "horse4.jpg"),
        ("horse", "horse5.jpg"),
        ("horse", "horse6.jpg"),
        ("bird", "bird3.jpg"),
        ("bird", "bird4.jpg"),
        ("bird", "bird5.jpg"),
        ("bird", "bird6.jpg"),
        
    ]
    db_manager.insert_image_records(records)