import tkinter as tk

window = tk.Tk()
window.title("my first App")
window.geometry("500x500")

def greet():
    name = entry.get()
    label2.config(text=f"Hello {name}!!")

label = tk.Label(
    window,
    text="what is your name?",
    font=("Arial", 20)
)

label.pack(pady=20)

# Entry - input
entry = tk.Entry(
    window,
    font=("Arial", 18)
)

entry.pack()

button = tk.Button(
    window,
    text="Greet me",
    font=("Arial", 16),
    command=greet
)

button.pack()

label2 = tk.Label(
    window,
    text="welcome to my App!!",
    font=("Arial", 25)
)

label2.pack(pady=20)

window.mainloop()