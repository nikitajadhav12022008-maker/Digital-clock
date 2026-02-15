import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.resizable(False, False)
root.configure(bg="black")

# Function to update time
def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)

# Clock Label
label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    background="black",
    foreground="cyan"
)

label.pack(anchor="center")

update_time()

root.mainloop()