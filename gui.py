from tkinter import *
from google_sheets import update_today

STUDYING_COL = 3
DIET_COL = 5
EXERCISE_COL = 6
READING_COL = 8
MUSIC_COL = 10

class App():
    def __init__(self):
        self.window = Tk()
        self.window.title("Scoreboard Update")
        self.window.geometry('600x480')

        self.label = Label(text="Scoreboard Update")
        self.label.grid(row=0, column=0, columnspan=2)

        self.study_label = Label(text='Studying')
        self.study_label.grid(row=1, column=0)

        self.diet_label = Label(text='Diet')
        self.diet_label.grid(row=2, column=0)

        self.exercise_label = Label(text='Exercise')
        self.exercise_label.grid(row=3, column=0)

        self.reading_label = Label(text='Reading')
        self.reading_label.grid(row=4, column=0)

        # haha
        self.music_label = Label(text='Music')
        self.music_label.grid(row=5, column=0)

        # Variables

        self.study_var = IntVar()
        self.diet_var = IntVar()
        self.exercise_var = IntVar()
        self.reading_var = IntVar()
        self.music_var = IntVar()

        # Checkboxes


        self.study_check = Checkbutton(var=self.study_var)
        self.study_check.grid(row=1, column=1)

        self.diet_check = Checkbutton(var=self.diet_var)
        self.diet_check.grid(row=2, column=1)

        self.exercise_check = Checkbutton(var=self.exercise_var)
        self.exercise_check.grid(row=3, column=1)

        self.reading_check = Checkbutton(var=self.reading_var)
        self.reading_check.grid(row=4, column=1)

        self.music_check = Checkbutton(var=self.music_var)
        self.music_check.grid(row=5, column=1)

        # Update Button

        self.update = Button(text='Update', command=self.update_scoreboard)
        self.update.grid(row=6, column=0, columnspan=2)

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