import tkinter as tk
import tkinter.ttk as ttk
from installerLogic import apiEntry

class installer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (welcomeScreen, apiPrompt, done):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        
        self.show_frame(welcomeScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class welcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #header - welcome
        label = ttk.Label(self, text ="Startpage", font = ("Helvetica", 30, "bold", "italic"))
        label.pack(pady=10, padx=20)

        #subheader
        instruction_label = ttk.Label(self, text="Press any button to continue...", font=("Helvetica", 12))
        instruction_label.pack(pady=10, padx=20)

        #continue button
        button = ttk.Button(self, text="Click to Continue", command=lambda: controller.show_frame(apiPrompt))
        button.pack()

class apiPrompt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # API Prompt Header
        label = ttk.Label(self, text ="API Prompt", font = ("Helvetica", 30, "bold", "italic"))
        label.pack(pady=10, padx=20)

        # API Prompt Instruction Subheader
        instruction_label = ttk.Label(self, text="Enter your API key below:", font=("Helvetica", 12))
        instruction_label.pack(pady=10, padx=20)

        # API Key Text Entry
        self.api_entry = ttk.Entry(self, width=50)
        self.api_entry.pack(pady=10, padx=20)

        # Submit Button
        submit_button = ttk.Button(self, text="Submit", command=lambda: (apiEntry(self.api_entry.get()), controller.show_frame(done)))
        submit_button.pack(pady=10, padx=20)

class done(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Done Header
        label = ttk.Label(self, text ="Done", font = ("Helvetica", 30, "bold", "italic"))
        label.pack(pady=10, padx=20)

        # Done Instruction Subheader
        instruction_label = ttk.Label(self, text="Installation Complete!", font=("Helvetica", 12))
        instruction_label.pack(pady=10, padx=20)

app = installer()
app.mainloop()