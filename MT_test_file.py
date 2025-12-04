import time
import tkinter as tk
import random
from PIL import Image, ImageTk
import json
import os

# Score Saver ###########################################################
SCORE_FILE = "scores.json"

if not os.path.exists(SCORE_FILE):
    with open(SCORE_FILE, "w") as f:
        f.write("[]")

def load_scores():
    """Load scores from disk; return empty list if file doesn't exist or is invalid."""
    if not os.path.exists(SCORE_FILE):
        return []
    try:
        with open(SCORE_FILE, "r") as f:
            data = f.read().strip()
            if not data:
                return []
            return json.loads(data)
    except json.JSONDecodeError:
        return []

def save_scores(scores):
    """Save the list of scores to disk, keeping top 5 only."""
    # Keep only top 5 scores
    top_scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:5]
    with open(SCORE_FILE, "w") as f:
        json.dump(top_scores, f, indent=4)
#########################################################################

# App and Page Switcher##################################################
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

        self.scores = load_scores()

    def show_frame(self, page): #method to switch between frames
        frame = self.frames[page] #looks up the frame from the self.frames dictionary
        frame.tkraise() #raises that frame to the top
#########################################################################

# Pages #################################################################
class Menu_page(tk.Frame): # Initial page
    def __init__(self, parent, controller): #parent is the container frame where it will live, and controller is the App instance (used to switch pages)
        super().__init__(parent)

        # Logo Display ##########################################################
        img = Image.open("new_image.png")  # supports PNG transparency
        img = img.resize((250, 250), Image.LANCZOS)  # resizes the image
        self.logo = ImageTk.PhotoImage(img)

        logo_label = tk.Label(self, image=self.logo, bg=self["bg"])  
        logo_label.pack(pady=20)
        #########################################################################

        # 'Start' and 'Leaderboard' Buttons #####################################
        tk.Button(self, text="Start",
                  command=lambda: controller.show_frame(Typing_page)).pack()
        tk.Button(self, text="See Leaderboard",
                  command=lambda: controller.show_frame(Leaderboard_page)).pack()
        #########################################################################

class Typing_page(tk.Frame): # Contains paragraph and entry box
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Random Paragraph Selector #############################################
        paragraph_1 = """Macaroni and cheese is one of those classic comfort foods that almost everyone enjoys. The warm cheese sauce blends perfectly with the tender pasta, creating a simple but incredibly satisfying dish. Some people prefer the boxed version for its nostalgic flavor, while others take pride in making it from scratch with real cheese and baked breadcrumbs on top. No matter how it's prepared, mac and cheese has a way of bringing people together, especially on cold days or during family gatherings. Its versatility also makes it fun to experiment with, whether by adding spices, vegetables, or even different types of cheese. It's a dish that feels familiar, cozy, and endlessly customizable."""
        paragraph_2 = """On quiet autumn mornings, there's a particular stillness that seems almost intentional, as if the world is pausing just long enough for anyone paying attention to notice the small details usually lost in the rush of everyday life. The light filters through thinning leaves at an angle that feels softer than summer sunlight, carrying a faint golden tint that settles gently on everything it touches. Even the sounds shift: birds call in slower, clearer rhythms, and distant traffic seems muffled, as though wrapped in a blanket of cool air. People walking through a park at this hour often move with a kind of unspoken agreement not to disturb the calm, taking slower steps, breathing a little deeper, and letting their thoughts drift without urgency. It's in these moments that the mind seems to reorder itself naturally, drawing connections between memories, hopes, and half-formed ideas, creating a rare sense of clarity that lingers quietly throughout the rest of the day."""
        paragraph_3 = """Sometimes I imagine what it would be like to spend a full day inside an old, quiet library--the kind with tall wooden shelves, a faint smell of paper and dust, and large windows that let in soft, filtered light even on cloudy afternoons. There's something soothing about the way sound behaves in spaces like that, as if footsteps and whispers are automatically lowered out of respect for the thousands of stories resting on the shelves. You can wander past rows of books without any particular plan and still feel a sense of purpose, because every spine you pass represents a small doorway into someone else's imagination or memory. Finding a seat at a heavy wooden table, you might open a random volume and discover a topic you've never thought about before, letting your curiosity lead you from one idea to the next. Hours can slip by almost unnoticed in such a place, leaving you with a pleasant sense of quiet accomplishment, even if all you did was read, think, and breathe in the calm."""
        paragraph_4 = """Under the flicker of a dying streetlamp, I found myself staring at the kind of scene that makes a man question whether he's dreaming or just losing his grip on the edges of reality. The rain had turned the cracked pavement behind the Walmart into a slick sheet of shadow and reflection, and through the mist lumbered three pink elephants—yes, pink, like bubblegum dipped in moonlight—moving with the heavy confidence of creatures who knew nobody would dare cross them. Their tusks glinted like ivory switchblades as they guarded the entrance to a rusted loading bay, where muffled grunts and the dull thud of fists against flesh leaked out between the metal slats. Word on the street was that they ran the roughest underground fight club in the county, the kind of joint where a man could lose his wallet, his dignity, or his last good tooth in under ten minutes if he wasn't careful. As I watched them size me up with small, knowing eyes, I realized I had two choices: turn around and forget what I'd seen, or step inside and find out why even the bravest folks in town whispered about this place only after dark."""
        random_paragraph = random.choice([paragraph_1, paragraph_2, paragraph_3, paragraph_4]) # chooses a random paragraph (using import random) from 1-4
        self.random_paragraph = random_paragraph
        #########################################################################

        tk.Label(self, text="Test your typing speed below", font=("Arial", 25)).pack(pady=20)

        # Paragraph Display and Entry Box #######################################
        self.paragraph_display = tk.Text(self, height=12, width=70, wrap="word", font=("Arial", 11))
        self.paragraph_display.insert("1.0", self.random_paragraph)
        self.paragraph_display.config(state="disabled")
        self.paragraph_display.tag_config("correct", background="#7bf47b")
        self.paragraph_display.pack(pady=10)

        self.text_box = tk.Text(self, height=10, width=60, wrap="word")
        self.text_box.pack(pady=15)
        self.text_box.tag_config("wrong", background="#fc4848")
        self.text_box.bind("<KeyRelease>", self.check_text)
        #########################################################################
        
    # Timer and Related Functions ###############################################
        self.timer_label = tk.Label(self, text="60", font=("Arial", 40))
        self.timer_label.pack(pady=20)
        self.time_left_ms = 60000
        self.timer_started = False

        self.text_box.bind("<KeyPress>", self.start_timer)
        self.text_box.bind("<KeyRelease>", self.check_text)

        tk.Button(self, text="RESULTS (WILL BE TRIGGERED BY TIMER)", # DELETE EVENTUALLY
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
            wpm = self.calculate_wpm() # calls function that calculates the words per minute
            self.controller.frames[Result_page].update_result(wpm)
            self.controller.show_frame(Result_page)
    #########################################################################

    # WPM Calculator ########################################################
    def calculate_wpm(self):
        typed = self.text_box.get("1.0", "end-1c").strip()
        target_words = self.random_paragraph.split()
        typed_words = typed.split()
        
        correct = 0
        
        for i in range(min(len(target_words), len(typed_words))):
            if typed_words[i] == target_words[i]:
                correct += 1

        wpm = correct
       
        return wpm
    #########################################################################
    
    # Text Checker ##########################################################
    def check_text(self, event=None): # checks text to make sure it's correct
        typed_text = self.text_box.get("1.0", "end-1c")
        original_text = self.random_paragraph
        
        self.paragraph_display.config(state="normal")
        self.paragraph_display.tag_remove("correct", "1.0", "end")
        for i in range(min(len(typed_text), len(original_text))):
            if typed_text[i] == original_text[i]:
                start = f"1.0 + {i} chars"
                end = f"1.0 + {i+1} chars"
                self.paragraph_display.tag_add("correct", start, end)
            else:
                break
        self.paragraph_display.config(state="disabled")
        
        self.text_box.tag_remove("wrong", "1.0", "end") 
        for i in range(len(typed_text)): # loops through each character in typed_text
            if i >= len(original_text): 
                break
            if typed_text[i] != original_text[i]: # compares each character to original_text
                start = f"1.0 + {i} chars" # calculates start position for tagging
                end = f"1.0 + {i+1} chars" # ends tagging one character after start
                self.text_box.tag_add("wrong", start, end) # adds "wrong" tag to incorrect characters
    #########################################################################
        
class Result_page(tk.Frame): # Contains results, appears at end of timer
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # WPM Result Display ####################################################
        self.you_typed_label = tk.Label(self, text="You Typed", font=("Helvetica", 30))
        self.you_typed_label.pack(pady=10)
        self.result_label = tk.Label(self, text="0 WPM", font=("Helvetica", 80))
        self.result_label.pack()
        #########################################################################

        # Buttons to Save Score and Go To Leaderboard #############################
        tk.Label(self, text="Enter your name to save your score").pack(pady=(20,5))
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        tk.Button(self, text="Save",
                  command=self.save_score).pack()
        tk.Button(self, text="See Leaderboard",
                  command=lambda: controller.show_frame(Leaderboard_page)).pack(pady=10)
        #########################################################################
        
    # 'WPM Result Display' Updater and Save #################################
    def update_result(self, wpm):
        self.wpm = wpm
        self.result_label.config(text=f"{wpm} WPM")
    #########################################################################

    # Score Saves to Dictionary #############################################
    def save_score(self):
        name = self.name_entry.get().strip() or "Anonymous"
        score_entry = {"name": name, "score": self.wpm}
        self.controller.scores.append(score_entry)
        save_scores(self.controller.scores)
        self.name_entry.delete(0, "end") # clears entry box
    #########################################################################

class Leaderboard_page(tk.Frame): # Contains saved scores
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Leaderboard ###########################################################
        leaderboard_label = tk.Label(self, text="Local Leaderboard", font=("Helvetica", 40)).pack(pady=20)
        self.list_label = tk.Label(self, text="")
        self.list_label.pack(pady=10)
        #########################################################################

        # 'Menu' Button ########################################
        tk.Button(self, text="Menu",
                  command=lambda: controller.show_frame(Menu_page)).pack()
        #########################################################################

    def tkraise(self):
        super().tkraise()
        sorted_scores = sorted(self.controller.scores, key=lambda x: x["score"], reverse=True)[:10]
        scores_text = "\n".join(f"{i+1}. {s['name']}: {s['score']} WPM" for i, s in enumerate(sorted_scores))
        self.list_label.config(text=scores_text)
#########################################################################

app = App()
app.mainloop()