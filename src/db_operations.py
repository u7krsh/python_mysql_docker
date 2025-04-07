import mysql.connector

class ClassicModelsDB:
    def __init__(self, host, user, password, database):
        """
        Initialize the connection to the MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Connected to the database successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None

    def create_record(self, table, data):
        """
        Insert a new record into the specified table.
        :param table: Table name.
        :param data: Dictionary of column names and values.
        """
        try:
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            print("Record inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error inserting record: {err}")

    def read_records(self, table, limit=10):
        """
        Fetch records from the specified table.
        :param table: Table name.
        :param limit: Number of records to fetch.
        """
        try:
            query = f"SELECT * FROM {table} LIMIT %s"
            self.cursor.execute(query, (limit,))
            records = self.cursor.fetchall()
            return records
        except mysql.connector.Error as err:
            print(f"Error fetching records: {err}")
            return []

    def update_record(self, table, data, condition):
        """
        Update a record in the specified table.
        :param table: Table name.
        :param data: Dictionary of column names and new values.
        :param condition: WHERE clause condition as a string.
        """
        try:
            updates = ", ".join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE {table} SET {updates} WHERE {condition}"
            self.cursor.execute(query, tuple(data.values()))
            self.connection.commit()
            print("Record updated successfully!")
        except mysql.connector.Error as err:
            print(f"Error updating record: {err}")

    def delete_record(self, table, condition):
        """
        Delete a record from the specified table.
        :param table: Table name.
        :param condition: WHERE clause condition as a string.
        """
        try:
            query = f"DELETE FROM {table} WHERE {condition}"
            self.cursor.execute(query)
            self.connection.commit()
            print("Record deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error deleting record: {err}")

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")