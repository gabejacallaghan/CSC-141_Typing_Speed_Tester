import time


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