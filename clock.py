import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Clock")
label = tk.Label(root, font=("Arial", 80), bg="black", fg="cyan")
label.pack()

def update_clock():
	label.config(text=strftime("%H:%M:%S"))
	label.after(1000, update_clock)

update_clock()
root.mainloop()
