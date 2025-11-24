import time
import tkinter as tk

#CREATES A FULL APP

class App(tk.Tk): # Defines new class that inherits from tk.Tk
    def __init__(self):
        super().__init__() # Calls hidden init methods from tk.Tk, which initializes a window
        self.title("Typing Test")

        container = tk.Frame(self) # This is a frame called "container" that will hold all the other frames (pages)
        container.pack(fill="both", expand=True)

        self.frames = {} # This creates a dictionary that will store all the pages. The keys are the classes and the values are the objects.

        for page in (Menu_page, Typing_page, Result_page, Leaderboard_page): #loops through all the pages
            frame = page(container, self) #makes a new frame. The frame will live in "container", and
            self.frames[page] = frame #stores frame in the self.frames dictionary
            frame.grid(row=0, column=0, sticky="nsew") #stacks all the pages in the same grid

        self.show_frame(Menu_page)  #displays Menu page first

    def show_frame(self, page): #method to switch between frames
        frame = self.frames[page] #looks up the frame from the self.frames dictionary
        frame.tkraise() #raises that frame to the top

#CREATES SEPARATE PAGES

class Menu_page(tk.Frame): # makes this a child class of tk.Frame
    def __init__(self, parent, controller): #parent is the container frame where it will live, and controller is the App instance (used to switch pages)
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
        #Paragraph
        paragraph = """Macaroni and cheese is one of those classic comfort foods that almost everyone enjoys. The warm cheese sauce blends perfectly with the tender pasta, creating a simple but incredibly satisfying dish. Some people prefer the boxed version for its nostalgic flavor, while others take pride in making it from scratch with real cheese and baked breadcrumbs on top. No matter how it’s prepared, mac and cheese has a way of bringing people together, especially on cold days or during family gatherings. Its versatility also makes it fun to experiment with, whether by adding spices, vegetables, or even different types of cheese. It’s a dish that feels familiar, cozy, and endlessly customizable."""
        tk.Label(self, text="Type the paragraph below:").pack(pady=20)
        self.paragraph_label = tk.Label(self, text=paragraph, wraplength=500, justify="left") #displays paragraph
        self.paragraph_label.pack(pady=20)
        self.text_box = tk.Text(self, height=10, width=60) #box to type in
        self.text_box.pack(pady=15)
        
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