from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("100x100")
def handle_geometry(event):
    """Print the charecter asssociated to the key pressed"""
    print(event.char)
window.bind("<Key>", handle_geometry)
def handle_click(event):
    print("\nThe button was clicked!")
button=Button(text="Click me")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()