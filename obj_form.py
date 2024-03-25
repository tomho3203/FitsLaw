import tkinter as tk
import time
import random
import math
from stopwatch import Stopwatch
from result_form import ResultsForm

class GameStart:
    def __init__(self, master, main_menu):
        self.master_window = master
        self.main_menu = main_menu
        self.stopwatch = Stopwatch()
        self.click_timestamps = []
        self.box_clicks = 0
        self.left_click_count = 0
        self.right_click_count = 0
        self.recorded_time = 0
        self.prev_timestamp = None
        self.trial_count = 1
        self.max_trials = 3
        self.difficulty_multiplier = 1 

        self.master_window.title("Fitts Law Experiment")
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self.master_window.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        
        self.quit_button = tk.Button(self.master_window, text="Quit", command=self.return_to_main_menu)
        self.quit_button['font'] = ("Arial", 13)
        self.quit_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=15)

        self.title_label = tk.Label(self.master_window, text=f"Level of Difficulty {self.difficulty_multiplier+1}: Trial 1", font=("Arial", 40))
        self.title_label.pack(pady=10)
        
        self.left_box_pos_label = tk.Label(self.master_window, text="", font=("Arial", 13))
        self.right_box_pos_label = tk.Label(self.master_window, text="", font=("Arial", 13))
        self.distance_label = tk.Label(self.master_window, text="", font=("Arial", 13))
        self.elapsed_time_label = tk.Label(self.master_window, text="", font=("Arial", 20))
        self.clicks_label = tk.Label(self.master_window, text="", font=("Arial", 20))
        
        self.left_box_pos_label.pack(pady=5)
        self.right_box_pos_label.pack(pady=5)
        self.distance_label.pack(pady=5)
        self.elapsed_time_label.pack(pady=10)
        self.clicks_label.pack(pady=10)
        
        self.create_boxes()

        self.master_window.protocol("WM_DELETE_WINDOW", self.return_to_main_menu)
    
    def return_to_main_menu(self):
        self.master_window.destroy()
        self.main_menu.master.deiconify()
    
    def show_results(self):
        self.result_window = tk.Toplevel(self.master_window)
        self.master_window.withdraw()
        ResultsForm(self.result_window, self, self.recorded_time, self.click_timestamps, self.difficulty_multiplier, self.trial_count)
        
        if self.trial_count <= self.max_trials:
            self.trial_count += 1
            self.title_label.config(text=f"Level of Difficulty {self.difficulty_multiplier+1}: Trial {self.trial_count}")
            self.start_new_trial()
        
        if self.trial_count > self.max_trials:
            self.trial_count = 1
            self.difficulty_multiplier += 1
            self.title_label.config(text=f"Level of Difficulty {self.difficulty_multiplier+1}: Trial {self.trial_count}")
            self.start_new_trial()

    def create_boxes(self):
        
        self.left_box = tk.Label(self.master_window, text="Left Box", bg="Gray")
        self.left_box.place(x=self.screen_width - 1200, y=self.screen_height - 500, width=350, height=350)
        self.left_box.bind('<Button-1>', lambda event: self.start_stopwatch_left())
        
        self.right_box = tk.Label(self.master_window, text="Right Box", bg="Gray")
        self.right_box.place(x=self.screen_width - 500, y=self.screen_height - 500, width=350, height=350)
        self.right_box.bind('<Button-1>', lambda event: self.record_right_press())
        
    
    def start_stopwatch_left(self):
        if self.left_click_count == 0:
            self.stopwatch.startTime()
            self.timer()
        else:
            self.record_clicks()
            self.record_timestamp()

        self.left_click_count += 1

    def record_right_press(self):
        if self.left_click_count > self.right_click_count:
            self.right_click_count += 1
            self.record_clicks()
            self.record_timestamp()
        
        if self.right_click_count > 5:
            self.stopwatch.stopTime()
            self.recorded_time = self.stopwatch.elapsed_time()
            self.reset_timer()
            self.show_results()
    
    def record_clicks(self):
        self.box_clicks += 1
        self.clicks_label.config(text=f"Clicks: {self.box_clicks}")
    
    def timer(self):
        if self.stopwatch.start_time:
            elapsed_time = time.time() - self.stopwatch.start_time
            self.elapsed_time_label.config(text="Time: {:.2f} seconds." .format(elapsed_time))
            self.master_window.after(100, self.timer)
    
    def reset_timer(self):
        self.left_click_count = 0
        self.right_click_count = 0
        self.box_clicks = 0
        self.stopwatch.reset()
        self.elapsed_time_label.config(text="")
        self.clicks_label.config(text="Clicks: 0")

    def record_timestamp(self):
        timestamp = time.time()
        self.click_timestamps.append(timestamp)

        if self.prev_timestamp is not None:
            time_interval = timestamp - self.prev_timestamp
            print(f"Time Interval {len(self.click_timestamps) - 2}-{len(self.click_timestamps) - 1}: {time_interval:.2f} seconds")

        self.prev_timestamp = timestamp
    
    def start_new_trial(self):
        new_left_x = (1/self.difficulty_multiplier) * random.randint(200, self.screen_width - 1000)
        new_left_y = random.randint(self.screen_height - 600, self.screen_height - 300)
        
        new_right_x = (self.difficulty_multiplier*75) + random.randint(self.screen_width - 600, self.screen_width - 400)
        new_right_y = random.randint(self.screen_height - 600, self.screen_height - 300)
        
        new_width = (1/self.difficulty_multiplier) * random.randint(250, 300) + 10
        new_height = (1/self.difficulty_multiplier)* random.randint(250, 300) + 10
        
        self.left_box.place_configure(x=new_left_x, y=new_left_y, width=new_width, height=new_height) 
        self.right_box.place_configure(x=new_right_x, y=new_right_y, width=new_width, height=new_height)
    
        
        self.reset_timer()
        self.recorded_time = 0
        self.click_timestamps = []
        self.prev_timestamp = None
