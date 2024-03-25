import tkinter as tk
from obj_form import GameStart

class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Fitts Law Experiment")

        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        master.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        
        title_label = tk.Label(master, text="Welcome to the Fitts Law Experiment", font=("Arial", 24), pady=50)
        title_label.pack()
        title_label = tk.Label(master, text="by Tom Ho", font=("Arial", 15), pady=10)
        title_label.pack()

        start_btn = tk.Button(master, text="Start", font=("Arial", 20), command=self.startGame, padx=20, pady=10)
        start_btn.pack(pady=20)
        exit_btn = tk.Button(master, text="Exit", font=("Arial", 20), command=self.exit_app, padx=20, pady=10)
        exit_btn.pack()

    def startGame(self):
        self.obj_form = tk.Toplevel(self.master)
        self.master.withdraw()
        GameStart(self.obj_form, self)
    
    def exit_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()
