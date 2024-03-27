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
        ("dog", "dog.jpg"),
        ("dog", "dog2.jpg"),
        ("cat", "cat.jpg"),
        ("cat", "cat2.jpg"),
        ("horse", "horse.jpg"),
        ("horse", "horse2.jpg"),
        ("bird", "bird.jpg"),
        ("bird", "bird2.jpg"),
    ]
    db_manager.insert_image_records(records)