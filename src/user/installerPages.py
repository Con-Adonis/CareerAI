import tkinter as tk
import tkinter.ttk as ttk
from installerLogic import apiEntry, infoEntry

class installer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self, padx=10, pady=100)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (welcomeScreen, survey, quit):
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
        
        #header - careerAI
        label = ttk.Label(self, text ="CareerAI", font = ("Helvetica", 30, "bold", "italic"))
        label.pack(side="top", pady=10, padx=20)

        #subheader - welcome
        instruction_label = ttk.Label(self, text="Welcome to CareerAI, your smart application assistant!", font=("Helvetica", 12))
        instruction_label.pack(pady=10, padx=20)

        #subheader - survey explination
        instruction_label = ttk.Label(self, text="Let's first start off with a general survey in order to gauge your personal details and the kind of candidate you are!", font=("Helvetica", 12))
        instruction_label.pack(pady=10, padx=20)

        #continue button
        button = ttk.Button(self, text="Click to Continue", command=lambda: controller.show_frame(survey))
        button.pack()

class survey(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #header - careerAI
        label = ttk.Label(self, text ="CareerAI", font = ("Helvetica", 30, "bold", "italic"))
        label.pack(pady=10, padx=20)

        #SURVEY
        #Q1 - name
        instruction_label = ttk.Label(self, text="Please enter your full name", font=("Helvetica", 12))
        instruction_label.pack()
        nameEntry = ttk.Entry(self, width=50)
        nameEntry.pack()

        #Q2 - email
        Frame = ttk.Frame(self)
        Frame.pack(pady=10)
        instruction_label = ttk.Label(self, text="Please enter your email address", font=("Helvetica", 12))
        instruction_label.pack()
        emailEntry = ttk.Entry(self, width=50)
        emailEntry.pack()

        #Q3 - project
        Frame = ttk.Frame(self)
        Frame.pack(pady=10)
        instruction_label = ttk.Label(self, text="Please describe a project you are proud of", font=("Helvetica", 12))
        instruction_label.pack()
        projectEntry = ttk.Entry(self, width=50)
        projectEntry.pack()

        #Q4 - difficulty
        Frame = ttk.Frame(self)
        Frame.pack(pady=10)
        instruction_label = ttk.Label(self, text="Please describe a chalenging technical problem you overcame", font=("Helvetica", 12))
        instruction_label.pack()
        challengeEntry = ttk.Entry(self, width=50)
        challengeEntry.pack()

        #Q5 - salary
        Frame = ttk.Frame(self)
        Frame.pack(pady=10)
        instruction_label = ttk.Label(self, text="What salary range are you looking for?", font=("Helvetica", 12))
        instruction_label.pack()
        salaryEntry = ttk.Entry(self, width=50)
        salaryEntry.pack()

        #submit button
        button = ttk.Button(self, text="Submit Survey", command=lambda: controller.show_frame(quit))
        button.pack(pady=20)

class quit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #header - welcome
        label = ttk.Label(self, text ="CareerAI", font = ("Helvetica", 30, "bold", "italic"))
        label.pack(pady=10, padx=20)

        #subheader - thanks
        instruction_label = ttk.Label(self, text="Thank you for filling out your information! We will now begin filling out applications on your behalf, and will prompt you with any questions we come across that we don't know.", font=("Helvetica", 12))
        instruction_label.pack(pady=10, padx=20)

        #quit button
        button = ttk.Button(self, text="Quit", command=self.quit)
        button.pack()

app = installer()
app.mainloop()