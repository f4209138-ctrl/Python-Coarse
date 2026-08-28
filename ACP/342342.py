import tkinter as tk

def append_key(digit):
    pin_entry.insert(tk.END, digit)

def clear_pin():
    pin_entry.delete(0, tk.END)

def setup_pin():
    acc_num = acc_entry.get().strip()
    pin = pin_entry.get().strip()
    
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    
    if not acc_num or not pin:
        output_text.insert(tk.END, "Error: Both Account Number and PIN are required.")
    elif len(pin) != 4 or not pin.isdigit():
        output_text.insert(tk.END, "Error: PIN must be exactly 4 digits.")
    else:
        output_text.insert(tk.END, f"Success!\nAccount: {acc_num}\nStatus: PIN updated successfully.\nEncrypted PIN: {'*' * len(pin)}")
    
    output_text.config(state="disabled")

root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("460x520")
root.resizable(False, False)

account_frame = tk.LabelFrame(root, text="Account Information", relief="raised", bd=3, font=("Arial", 10, "bold"))
account_frame.place(x=20, y=15, width=420, height=130)

acc_label = tk.Label(account_frame, text="Account Number:", font=("Arial", 9))
acc_label.place(x=15, y=15)

acc_entry = tk.Entry(account_frame, font=("Arial", 10))
acc_entry.place(x=140, y=15, width=240)

pin_label = tk.Label(account_frame, text="New 4-Digit PIN:", font=("Arial", 9))
pin_label.place(x=15, y=55)

pin_entry = tk.Entry(account_frame, show="*", font=("Arial", 10))
pin_entry.place(x=140, y=55, width=240)

keypad_frame = tk.LabelFrame(root, text="Keypad", relief="sunken", bd=3, font=("Arial", 10, "bold"))
keypad_frame.place(x=110, y=155, width=240, height=190)

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('Clear', 3, 0), ('0', 3, 1), ('Submit', 3, 2)
]

for text, row, col in buttons:
    if text == 'Clear':
        btn = tk.Button(keypad_frame, text=text, width=5, height=1, relief="raised", bd=2, command=clear_pin)
    elif text == 'Submit':
        btn = tk.Button(keypad_frame, text=text, width=5, height=1, relief="raised", bd=2, command=setup_pin)
    else:
        btn = tk.Button(keypad_frame, text=text, width=5, height=1, relief="raised", bd=2, command=lambda d=text: append_key(d))
    btn.grid(row=row, column=col, padx=8, pady=5)

output_frame = tk.Frame(root, relief="sunken", bd=2)
output_frame.place(x=20, y=360, width=420, height=135)

output_text = tk.Text(output_frame, font=("Arial", 9), state="disabled", wrap="word")
output_text.pack(fill="both", expand=True, padx=5, pady=5)

root.mainloop()