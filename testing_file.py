import time

start_time = time.time()


#GRABBING END TIME
end_time = time.time()
elapsed_time = end_time - start_time
elapsed_minutes = elapsed_time / 60

#CALCULATING WORD COUNT
wpm = word_count / elapsed_minutes


#FOR STARTING STOPWATCH ON TYPING: entry.bind("<Key>", start_timer_once)