from tkinter import *
from google_sheets import update_today

STUDYING_COL = 3
DIET_COL = 5
EXERCISE_COL = 6
READING_COL = 8
MUSIC_COL = 10


# COLORS
BG_COLOR = '#FBF8F1'
FG_COLOR = '#54BAB9'
SELECT_COLOR = '#54BAB9'

# FONTS
TITLE_FONT = ("Helvetica", 25, 'bold')
LABEL_FONT = ("Helvetica", 13)
BUTTON_FONT = ("Helvetica", 13, 'bold')


class App():
    def __init__(self):
        self.window = Tk()
        self.window.title("Scoreboard Update")
        # self.window.geometry('300x480')
        self.window.configure(bg=BG_COLOR)

        self.label = Label(text="Scoreboard Update", bg=BG_COLOR, font=TITLE_FONT, fg=FG_COLOR)
        self.label.grid(row=0, column=0, columnspan=2, padx=40, pady=20)

        self.study_label = Label(text='Studying', bg=BG_COLOR, font=LABEL_FONT)
        self.study_label.grid(row=1, column=0)

        self.diet_label = Label(text='Diet', bg=BG_COLOR, font=LABEL_FONT)
        self.diet_label.grid(row=2, column=0)

        self.exercise_label = Label(text='Exercise', bg=BG_COLOR, font=LABEL_FONT)
        self.exercise_label.grid(row=3, column=0)

        self.reading_label = Label(text='Reading', bg=BG_COLOR, font=LABEL_FONT)
        self.reading_label.grid(row=4, column=0)

        # haha
        self.music_label = Label(text='Music', bg=BG_COLOR, font=LABEL_FONT)
        self.music_label.grid(row=5, column=0)

        # Variables

        self.study_var = IntVar()
        self.diet_var = IntVar()
        self.exercise_var = IntVar()
        self.reading_var = IntVar()
        self.music_var = IntVar()

        # Checkboxes


        self.study_check = Checkbutton(var=self.study_var, bg=BG_COLOR)
        self.study_check.grid(row=1, column=1)

        self.diet_check = Checkbutton(var=self.diet_var, bg=BG_COLOR)
        self.diet_check.grid(row=2, column=1)

        self.exercise_check = Checkbutton(var=self.exercise_var, bg=BG_COLOR)
        self.exercise_check.grid(row=3, column=1)

        self.reading_check = Checkbutton(var=self.reading_var, bg=BG_COLOR)
        self.reading_check.grid(row=4, column=1)

        self.music_check = Checkbutton(var=self.music_var, bg=BG_COLOR)
        self.music_check.grid(row=5, column=1)

        # Update Button

        self.update = Button(text='Update', command=self.update_scoreboard, font=BUTTON_FONT, fg=FG_COLOR, activeforeground=SELECT_COLOR, bd=5)
        self.update.grid(row=6, column=0, columnspan=2, pady=50)

        self.window.mainloop()

    def update_scoreboard(self):
        print(f"Studying: {self.study_var.get()}")
        print(f"Exercise: {self.exercise_var.get()}")
        print(f"Diet: {self.diet_var.get()}")
        print(f"Reading: {self.reading_var.get()}")
        print(f"Music: {self.music_var.get()}")

        # =================
        update_today(STUDYING_COL, self.study_var.get())
        update_today(DIET_COL, self.diet_var.get())
        update_today(EXERCISE_COL, self.exercise_var.get())
        update_today(READING_COL, self.reading_var.get())
        update_today(MUSIC_COL, self.music_var.get())