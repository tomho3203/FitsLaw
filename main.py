# main.py
# Tom Ho
import tkinter as tk
from main_menu import MainMenu
import app_logic

# Global variables for root and forms
globalRoot = None
globalMM = None
globalStart = None
globalResult = None
globalEnd = None

# Function to create the root window
def create_root():
    global globalRoot
    globalRoot = tk.Tk()
    globalRoot.title("Fitts Law Experiment")

# Function to create the main menu form
def create_main_menu():
    global globalMM
    globalMM = MainMenu(globalRoot)

# Function to run the application
def run_application():
    create_root()
    create_main_menu()
    # Set forms for app logic
    app_logic.set_forms(globalRoot, globalMM, globalStart, globalResult, globalEnd)
    globalRoot.mainloop()

# Entry point of the application
if __name__ == "__main__":
    run_application()
