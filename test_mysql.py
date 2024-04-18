import unittest
import mysql.connector  # Assuming you're using mysql.connector instead of MySQLdb

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_testing_database"
        )
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_create_state_adds_record(self):
        initial_count = self.cursor.execute("SELECT COUNT(*) FROM states").fetchone()[0]
        self.cursor.execute("CREATE TABLE IF NOT EXISTS states (name VARCHAR(255))")
        self.cursor.execute("INSERT INTO states (name) VALUES (%s)", ("California",))
        self.conn.commit()
        final_count = self.cursor.execute("SELECT COUNT(*) FROM states").fetchone()[0]
        self.assertEqual(final_count - initial_count, 1)

if __name__ == "__main__":
    unittest.main()
