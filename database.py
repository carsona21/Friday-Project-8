# database.py
import sqlite3

def create_database():
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def submit_feedback(name, email, feedback):
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)', (name, email, feedback))
    conn.commit()
    conn.close()

def retrieve_feedback():
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('SELECT * FROM feedback')
    entries = c.fetchall()
    conn.close()
    return entries
