import tkinter as tk
window = tk.Tk()
window.title("Typing Speed Tester")

paragraph = """The morning air was cool and refreshing as sunlight filtered through the tall trees lining the quiet path. Birds were beginning to stir, filling the forest with soft, cheerful sounds that blended with the distant rustle of leaves. As the breeze swept across the landscape, it carried the earthy scent of damp soil and fresh pine needles. The world felt calm and unhurried, as if nature itself had paused to take a slow, peaceful breath. It was the kind of morning that invited anyone passing by to stop for a moment, listen closely, and appreciate the simple beauty of the day."""

label = tk.Label(window, text=paragraph, wraplength=400, justify="left")
label.pack()

text_box = tk.Text(window, height=10, width=50)
text_box.pack()



window.mainloop()