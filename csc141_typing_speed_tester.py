import time
import tkinter as tk
import random

# App and Page Switcher

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

# Pages

class Menu_page(tk.Frame): # Initial page
    def __init__(self, parent, controller): #parent is the container frame where it will live, and controller is the App instance (used to switch pages)
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE START MENU").pack(pady=20)
        tk.Button(self, text="Start",
                  command=lambda: controller.show_frame(Typing_page)).pack()
        tk.Button(self, text="See Leaderboard",
                  command=lambda: controller.show_frame(Leaderboard_page)).pack()

class Typing_page(tk.Frame): # Contains paragraph and entry box
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Paragraphs
        paragraph_1 = """Macaroni and cheese is one of those classic comfort foods that almost everyone enjoys. The warm cheese sauce blends perfectly with the tender pasta, creating a simple but incredibly satisfying dish. Some people prefer the boxed version for its nostalgic flavor, while others take pride in making it from scratch with real cheese and baked breadcrumbs on top. No matter how it’s prepared, mac and cheese has a way of bringing people together, especially on cold days or during family gatherings. Its versatility also makes it fun to experiment with, whether by adding spices, vegetables, or even different types of cheese. It’s a dish that feels familiar, cozy, and endlessly customizable."""
        paragraph_2 = """On quiet autumn mornings, there’s a particular stillness that seems almost intentional, as if the world is pausing just long enough for anyone paying attention to notice the small details usually lost in the rush of everyday life. The light filters through thinning leaves at an angle that feels softer than summer sunlight, carrying a faint golden tint that settles gently on everything it touches. Even the sounds shift: birds call in slower, clearer rhythms, and distant traffic seems muffled, as though wrapped in a blanket of cool air. People walking through a park at this hour often move with a kind of unspoken agreement not to disturb the calm, taking slower steps, breathing a little deeper, and letting their thoughts drift without urgency. It’s in these moments that the mind seems to reorder itself naturally, drawing connections between memories, hopes, and half-formed ideas, creating a rare sense of clarity that lingers quietly throughout the rest of the day."""
        paragraph_3 = """Sometimes I imagine what it would be like to spend a full day inside an old, quiet library—the kind with tall wooden shelves, a faint smell of paper and dust, and large windows that let in soft, filtered light even on cloudy afternoons. There’s something soothing about the way sound behaves in spaces like that, as if footsteps and whispers are automatically lowered out of respect for the thousands of stories resting on the shelves. You can wander past rows of books without any particular plan and still feel a sense of purpose, because every spine you pass represents a small doorway into someone else’s imagination or memory. Finding a seat at a heavy wooden table, you might open a random volume and discover a topic you’ve never thought about before, letting your curiosity lead you from one idea to the next. Hours can slip by almost unnoticed in such a place, leaving you with a pleasant sense of quiet accomplishment, even if all you did was read, think, and breathe in the calm."""
        paragraph_4 = """Under the flicker of a dying streetlamp, I found myself staring at the kind of scene that makes a man question whether he’s dreaming or just losing his grip on the edges of reality. The rain had turned the cracked pavement behind the Walmart into a slick sheet of shadow and reflection, and through the mist lumbered three pink elephants—yes, pink, like bubblegum dipped in moonlight—moving with the heavy confidence of creatures who knew nobody would dare cross them. Their tusks glinted like ivory switchblades as they guarded the entrance to a rusted loading bay, where muffled grunts and the dull thud of fists against flesh leaked out between the metal slats. Word on the street was that they ran the roughest underground fight club in the county, the kind of joint where a man could lose his wallet, his dignity, or his last good tooth in under ten minutes if he wasn’t careful. As I watched them size me up with small, knowing eyes, I realized I had two choices: turn around and forget what I’d seen, or step inside and find out why even the bravest folks in town whispered about this place only after dark."""
        random_paragraph = random.choice([paragraph_1, paragraph_2, paragraph_3, paragraph_4]) # chooses a random paragraph (using import random) from 1-4
        self.random_paragraph = random_paragraph


        tk.Label(self, text="Test your typing speed below").pack(pady=20)
        self.paragraph_label = tk.Label(self, text=self.random_paragraph, wraplength=500, justify="left")
        self.paragraph_label.pack(pady=20) # displays paragraph
        self.text_box = tk.Text(self, height=10, width=60)
        self.text_box.pack(pady=15) # entry box
        self.text_box.bind("<KeyRelease>", self.check_text) 
        
    # Timer
    
        self.timer_label = tk.Label(self, text="60", font=("Arial", 40))
        self.timer_label.pack(pady=20)
        self.time_left_ms = 60000
        self.timer_started = False

        self.text_box.bind("<KeyPress>", self.start_timer)
        self.text_box.bind("<KeyRelease>", self.check_text)

        tk.Button(self, text="RESULTS (WILL BE TRIGGERED BY TIMER)",
                  command=lambda: controller.show_frame(Result_page)).pack()

    def start_timer(self, event=None):
        if not self.timer_started:
            self.timer_started = True
            self.update_timer()

    def update_timer(self, event=None): #updates the text as the timer runs
        if self.time_left_ms > 0:
            seconds = (self.time_left_ms // 1000) % 60
            ms = (self.time_left_ms % 1000) // 10

            self.timer_label.config(text=f"{seconds:02d}.{ms:02d}")
            self.time_left_ms -= 10
            self.after(10, self.update_timer)  # call again in 1 second
        else:
            self.timer_label.config(text="Time: 0")
            self.text_box.config(state="disabled")   # stop typing
            wpm = self.calculate_wpm()
            self.controller.frames[Result_page].update_result(wpm)
            self.controller.show_frame(Result_page)

    def calculate_wpm(self):
        typed = self.text_box.get("1.0", "end-1c")
        words = typed.split() # splits text into words
        return len(words) # num of words typed in the min
    


    
    # Text Checker
    def check_text(self, event=None): # checks text to make sure it's correct
        typed_text = self.text_box.get("1.0", "end-1c")
        original_text = self.random_paragraph
        self.text_box.tag_remove("wrong", "1.0", "end") 
        for i in range(len(typed_text)): # loops through each character in typed_text
            if i >= len(original_text): 
                break
            if typed_text[i] != original_text[i]:# compares each character to original_text
                start = f"1.0 + {i} chars" # calculates start position for tagging
                end = f"1.0 + {i+1} chars" # ends tagging one character after start
                self.text_box.tag_add("wrong", start, end) # adds "wrong" tag to incorrect characters
        
        self.text_box.tag_config("wrong", background="red", foreground="white") # configures "wrong" tag to have red background
        
class Result_page(tk.Frame): # Contains results, appears at end of timer
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE RESULTS PAGE").pack(pady=20)
        self.result_label = tk.Label(self, text="You Typed 0 WPM", font=(30))
        self.result_label.pack(pady=10)
        tk.Button(self, text="See Leaderboard",
                  command=lambda: controller.show_frame(Leaderboard_page)).pack()
        
    def update_result(self, wpm):
        self.result_label.config(text=f"You Typed {wpm} WPM") # Updates label with your score

class Leaderboard_page(tk.Frame): # Contains saved scores
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="THIS IS THE LEADERBOARD PAGE").pack(pady=20)
        tk.Button(self, text="Menu",
                  command=lambda: controller.show_frame(Menu_page)).pack()
        tk.Button(self, text="Try Again",
                  command=lambda: controller.show_frame(Typing_page)).pack()

app = App()
app.mainloop()