import tkinter as tk
from tkinter import messagebox

routine_tasks = [
    "Unpack school bag and wash hands",
    "Have a healthy afternoon snack",
    "Complete homework and assignments",
    "30 minutes of outdoor play or exercise",
    "Read a book chapter",
    "Help set the dinner table",
    "Prepare backpack and clothes for tomorrow"
]

current_task_index = 0

def on_key_press(event):
    if event.char and event.char.isprintable():
        char_label.config(text=f"Last typed character: '{event.char}'")

def on_area_click(event):
    click_label.config(text=f"Routine area clicked at: (X: {event.x}, Y: {event.y})")

def add_task():
    global current_task_index
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Warning", "Please enter a task before submitting!")
        return
    
    routine_tasks.append(task)
    task_entry.delete(0, tk.END)
    update_display(f"Added new task: '{task}'")

def show_next_task():
    global current_task_index
    if not routine_tasks:
        display_text.config(state="normal")
        display_text.delete("1.0", tk.END)
        display_text.insert(tk.END, "No tasks left in the routine!")
        display_text.config(state="disabled")
        return
    
    task = routine_tasks[current_task_index]
    current_task_index = (current_task_index + 1) % len(routine_tasks)
    update_display(f"Next Routine Task:\n-> {task}")

def update_display(message):
    display_text.config(state="normal")
    display_text.delete("1.0", tk.END)
    display_text.insert(tk.END, message)
    display_text.config(state="disabled")

root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("480x470")
root.resizable(False, False)

header_label = tk.Label(
    root, 
    text="After-School Routine Checker", 
    font=("Arial", 14, "bold"),
    fg="#1e3a8a"
)
header_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

entry_label = tk.Label(input_frame, text="Enter a Task:", font=("Arial", 10))
entry_label.pack(side="left", padx=5)

task_entry = tk.Entry(input_frame, width=28, font=("Arial", 10))
task_entry.pack(side="left", padx=5)
task_entry.bind("<KeyRelease>", on_key_press)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(
    btn_frame, 
    text="Add Task", 
    command=add_task, 
    font=("Arial", 9, "bold"), 
    bg="#0284c7", 
    fg="white", 
    padx=8, 
    pady=2
)
add_btn.pack(side="left", padx=6)

next_btn = tk.Button(
    btn_frame, 
    text="Show Next Task", 
    command=show_next_task, 
    font=("Arial", 9, "bold"), 
    bg="#16a34a", 
    fg="white", 
    padx=8, 
    pady=2
)
next_btn.pack(side="left", padx=6)

routine_frame = tk.LabelFrame(
    root, 
    text="Routine Display Area (Click Inside)", 
    font=("Arial", 10, "bold"), 
    relief="groove", 
    bd=2
)
routine_frame.pack(padx=20, pady=10, fill="both", expand=True)
routine_frame.bind("<Button-1>", on_area_click)

display_text = tk.Text(
    routine_frame, 
    height=6, 
    width=45, 
    font=("Arial", 10), 
    wrap="word", 
    state="normal"
)
display_text.insert(tk.END, "Click 'Show Next Task' to begin your routine checker.")
display_text.config(state="disabled")
display_text.pack(padx=10, pady=10, fill="both", expand=True)
display_text.bind("<Button-1>", on_area_click)

status_frame = tk.Frame(root, relief="sunken", bd=1)
status_frame.pack(fill="x", side="bottom", padx=10, pady=8)

char_label = tk.Label(
    status_frame, 
    text="Last typed character: None", 
    font=("Arial", 9), 
    anchor="w"
)
char_label.pack(fill="x", padx=5, pady=2)

click_label = tk.Label(
    status_frame, 
    text="Routine area clicked at: Not clicked yet", 
    font=("Arial", 9), 
    anchor="w"
)
click_label.pack(fill="x", padx=5, pady=2)

root.mainloop()