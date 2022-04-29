from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def make():
    settings_window = Tk()
    settings_window.title("Settings")
    settings_window.minsize(width=300, height=300)
    settings_window.config(padx=50, pady=55, bg=YELLOW)



    work_min_entry = Entry(settings_window, width=10)
    work_min_entry.grid(column=2, row=2)
    work_min_label = Label(settings_window, text="Working Minutes", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
    work_min_label.grid(column=4, row=2)



    short_min_entry = Entry(settings_window, width=10)
    short_min_entry.grid(column=2, row=8)
    short_min_label = Label(settings_window, text="Short Break Minutes", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
    short_min_label.grid(column=4, row=8)



    long_min_entry = Entry(settings_window, width=10)
    long_min_entry.grid(column=2, row=14)
    long_min_label = Label(settings_window, text="Long Break Minutes", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
    long_min_label.grid(column=4, row=14)

    
    def change_settings():
        global WORK_MIN
        global SHORT_BREAK_MIN
        global LONG_BREAK_MIN

        WORK_MIN = int(work_min_entry.get())
        SHORT_BREAK_MIN = int(short_min_entry.get())
        LONG_BREAK_MIN = int(long_min_entry.get())

    confirm = Button(settings_window, text="Confirm",command=change_settings)
    confirm.grid(column=5, row=20)

