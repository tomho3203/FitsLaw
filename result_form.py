import tkinter as tk
from completion_form import completionForm

class ResultsForm:
    def __init__(self, master, obj_form, recorded_time, click_timestamps, difficulty_level, trial_number):
        self.master = master
        self.obj_form = obj_form
        self.recorded_time = recorded_time
        self.click_timestamps = click_timestamps
        
        master.title("Fitts Law Experiment - Results")
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        master.geometry(f"{screen_width}x{screen_height}+0+0")

        master.protocol("WM_DELETE_WINDOW", self.return_to_object)

        back_button = tk.Button(master, text="Next Trial", command=self.return_to_object)
        back_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=15)
        
        if (difficulty_level == 5) & (trial_number == 3):
            back_button.config(text="Next", command=self.show_completion_screen)

        result_label = tk.Label(master, text=f"Results (Difficulty {difficulty_level+1}: Trial {trial_number})", font=("Consolas", 13))
        result_label.pack(pady=10)

        intervals_label = tk.Label(master, text="Time Intervals:", font=("Consolas", 13))
        intervals_label.pack(pady=10)

        for i in range(1, len(self.click_timestamps)):
            time_interval = self.click_timestamps[i] - self.click_timestamps[i - 1]
            interval_label = tk.Label(master, text=f"{i}-{i+1}. {time_interval:.2f} seconds", font=("Consolas", 13))
            interval_label.pack()

        recorded_time_label = tk.Label(master, text=f"Trial Time: {recorded_time:.2f} seconds", font=("Consolas", 13))
        recorded_time_label.pack(pady=5)

    def return_to_object(self):
        self.master.destroy()
        self.obj_form.master.deiconify()
    
    def show_completion_screen(self):
        self.completion_form = tk.Toplevel(self.master)
        self.master.withdraw()
        completionForm(self.completion_form)
