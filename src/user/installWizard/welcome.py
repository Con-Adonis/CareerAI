import tkinter as tk

def welcomeScreen():
    root = tk.Tk()
    root.title("CareerAI")
    root.geometry("400x200")

    #welcome - welcome
    welcome_label = tk.Label(root, text="Test", font=("Helvetica", 30, "bold", "italic"))
    welcome_label.pack(pady=10, padx=20)

    #subheader
    instruction_label = tk.Label(root, text="Apply to jobs smarter. Press any button to continue...", font=("Helvetica", 12))
    instruction_label.pack(pady=10, padx=20)

    API = ''
    def promptAPI(root):
        tk.simpledialog.askstring(API, "Please enter API key: ")

    def on_key_press(event):
        root.destroy()

    root.bind("<Key>", on_key_press)
    root.mainloop()

def main():
    welcomeScreen()

main()