import tkinter as tk
import app_logic

class completionForm:
    def __init__(self, master):
        self.master = master
        master.title("The End")
        master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}+0+0")
        
        exit_button = tk.Button(master, text="Quit", command=self.exit_app, font=("Arial", 20))
        exit_button.pack(pady=15)
        
        master.protocol("WM_DELETE_WINDOW", self.exit_app)
    
    def exit_app(self):
        app_logic.stop_program()
