import tkinter as tk

def welcomeScreen(stdscr):
    root = tk.Tk()
    root.title("Welcome Screen")

    welcome_label = tk.Label(root, text="Welcome to the Application!", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    instruction_label = tk.Label(root, text="Press any key to continue...", font=("Helvetica", 12))
    instruction_label.pack(pady=10)

    def on_key_press(event):
        root.destroy()

    root.bind("<Key>", on_key_press)
    root.mainloop()

def main():
    welcomeScreen(None)