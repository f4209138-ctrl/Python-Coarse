import tkinter as tk
from datetime import date

def check_in():
    name = name_entry.get().strip()
    if not name:
        name = "Participant"
    
    today = date.today().strftime("%B %d, %Y")
    message = f"Welcome, {name}!\nThank you for checking in to today's workshop.\nDate: {today}\nPlease take your seat and enjoy the session!"
    
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, message)
    output_text.config(state="disabled")

root = tk.Tk()
root.title("Workshop Check-In")
root.geometry("450x380")
root.resizable(False, False)

instruction_label = tk.Label(
    root, 
    text="Welcome to the Workshop!\nPlease enter your name below and click Check In.", 
    font=("Arial", 11),
    justify="center"
)
instruction_label.pack(pady=12)

name_label = tk.Label(root, text="Participant Name:", font=("Arial", 10, "bold"))
name_label.pack()

name_entry = tk.Entry(root, width=32, font=("Arial", 10))
name_entry.pack(pady=6)

checkin_button = tk.Button(
    root, 
    text="Check In", 
    command=check_in, 
    font=("Arial", 10, "bold"),
    bg="#2b8a3e",
    fg="white",
    padx=10,
    pady=3
)
checkin_button.pack(pady=10)

output_text = tk.Text(root, height=6, width=44, font=("Arial", 10), state="disabled", wrap="word")
output_text.pack(pady=10)

root.mainloop()