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



start_time = time.time()


#GRABBING END TIME
end_time = time.time()
elapsed_time = end_time - start_time
elapsed_minutes = elapsed_time / 60

#CALCULATING WORD COUNT
character_count = len(typed_paragraph)
wpm = (character_count / 5) / elapsed_minutes


#FOR STARTING STOPWATCH ON TYPING: entry.bind("<Key>", start_timer_once)


class Stopwatch:
    def __init__(self):
        pass

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.start_time = time.time()
        self.elapsed_time = 0
        self.label.config(text="0.00")

    def update_clock(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.label.config(text=f"{self.elapsed_time:.2f}")
        self.window.after(50, self.update_clock)
Stopwatch()