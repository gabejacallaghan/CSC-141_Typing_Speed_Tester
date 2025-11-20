import time
import tkinter as tk

# CREATING MULTIPLE PAGES
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Test")

        container = tk.Frame(self) # Container holds all frames
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (Menu_page, Typing_page, Result_page, Leaderboard_page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu_page)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class Menu_page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE START MENU").pack(pady=20)
        tk.Button(self, text="Start",
                  command=lambda: controller.show_frame(Typing_page)).pack()


class Typing_page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE TYPING PAGE").pack(pady=20)
        tk.Button(self, text="Leaderboard",
                  command=lambda: controller.show_frame(Leaderboard_page)).pack()
        
class Result_page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE RESULTS PAGE").pack(pady=20)
        # tk.Button

class Leaderboard_page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE LEADERBOARD PAGE").pack(pady=20)


app = App()
app.mainloop()