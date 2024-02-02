import sqlite3
from datetime import datetime

# Connect to the SQLite database (you can replace it with your preferred database)
conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Registration (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL,
        DateOfBirth DATE,
        CONSTRAINT unique_email UNIQUE (Email)
    )
''')
conn.commit()

def create_record(name, email, dob):
    try:
        cursor.execute('''
            INSERT INTO Registration (Name, Email, DateOfBirth)
            VALUES (?, ?, ?)
        ''', (name, email, dob))
        conn.commit()
        print("Record created successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email address must be unique. Record not created.")

def read_records():
    cursor.execute('SELECT * FROM Registration')
    records = cursor.fetchall()
    if not records:
        print("No records found.")
    else:
        for record in records:
            print(record)

def update_record(record_id, new_name, new_email, new_dob):
    try:
        cursor.execute('''
            UPDATE Registration
            SET Name=?, Email=?, DateOfBirth=?
            WHERE ID=?
        ''', (new_name, new_email, new_dob, record_id))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.IntegrityError:
        print("Error: Email address must be unique. Record not updated.")

def delete_record(record_id):
    cursor.execute('DELETE FROM Registration WHERE ID=?', (record_id,))
    conn.commit()
    print("Record deleted successfully.")

# Example usage:
create_record("John Doe", "john@example.com", "1990-01-01")
read_records()
update_record(1, "John Updated", "john@example.com", "1990-01-01")
delete_record(1)
read_records()

# Close the connection
conn.close()
