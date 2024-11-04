# main.py
from database import create_database
from gui import create_gui

if __name__ == "__main__":
    create_database()  # Set up the database
    create_gui()       # Start the GUI
