import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('Verdana', 40, 'bold'), background='black', foreground='white')

label.pack(anchor='center')

update_time()
root.mainloop()