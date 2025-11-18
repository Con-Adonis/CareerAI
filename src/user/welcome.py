import tkinter as tk

def welcomeScreen():
    root = tk.Tk()
    root.title("CareerAI")
    root.geometry("400x200")

    welcome_label = tk.Label(root, text="CareerAI", font=("Helvetica", 30, "bold", "italic"))
    welcome_label.pack(pady=10, padx=20)

    instruction_label = tk.Label(root, text="Apply to jobs smarter. Press any button to continue...", font=("Helvetica", 12))
    instruction_label.pack(pady=10, padx=20)

    def on_key_press(event):
        root.destroy()

    root.bind("<Key>", on_key_press)
    root.mainloop()

def main():
    welcomeScreen(None)