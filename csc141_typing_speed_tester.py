import time
import tkinter as tk

#CREATES A FULL APP

class App(tk.Tk): # Defines new class that inherits from tk.Tk
    def __init__(self):
        super().__init__() # Calls from tk.Tk, which initializes a window
        self.title("Typing Test")

        container = tk.Frame(self) # This is a frame called "container" that will hold all the other frames (pages)
        container.pack(fill="both", expand=True)

        self.frames = {} # This creates a dictionary that will store all the pages. The keys are the classes and the values are the objects.

        for page in (Menu_page, Typing_page, Result_page, Leaderboard_page): #loops through all the pages
            frame = page(container, self) #makes a new frame. The frame will live in "container", and
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu_page)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

#CREATES SEPARATE PAGES

class Menu_page(tk.Frame): # Menu page, first to appear
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE START MENU").pack(pady=20)
        tk.Button(self, text="Start",
                  command=lambda: controller.show_frame(Typing_page)).pack()
        tk.Button(self, text="See Leaderboard",
                  command=lambda: controller.show_frame(Leaderboard_page)).pack()


class Typing_page(tk.Frame): # Page on which the typing is completed
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE TYPING PAGE").pack(pady=20)
        tk.Button(self, text="THIS BUTTON FINISHES",
                  command=lambda: controller.show_frame(Result_page)).pack()
        
class Result_page(tk.Frame): # When the timer runs out, this page appears with the results
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE RESULTS PAGE").pack(pady=20)
        tk.Button(self, text="See Leaderboard",
                  command=lambda: controller.show_frame(Leaderboard_page)).pack()

class Leaderboard_page(tk.Frame): # Leaderboard page, displays your score at the top along with other saved scores beneath it.
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE LEADERBOARD PAGE").pack(pady=20)
        tk.Button(self, text="Menu",
                  command=lambda: controller.show_frame(Menu_page)).pack()
        tk.Button(self, text="Try Again",
                  command=lambda: controller.show_frame(Typing_page)).pack()


app = App()
app.mainloop()