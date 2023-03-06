from main import db_name, sprint2
import sqlite3


# original tutorial https://eliran9692.medium.com/build-an-application-with-fastapi-from-scratch-9654e0e4476f
# modified here to work with sprint2 needs
def does_table_exists() -> bool:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        """
    SELECT count(*) FROM sqlite_master WHERE type='table' AND name='WuFooData'
    """
    )
    return cursor.fetchone()[0]  # in python zero==False, and any positive number == True


class CubesDB:
    def __init__(self, file=db_name):
        self.db_file = file
        if not does_table_exists():
            sprint2()

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.commit()
        self.conn.close()
