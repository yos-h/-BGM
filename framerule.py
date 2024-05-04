import tkinter as tk

class Frame_Rule(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        label = tk.Label(self, text='rule', font=("MSゴシック", "40"))
        label.pack()

        button0 = tk.Button(self, text='frame0', font=("MSゴシック", "20"), command=lambda: self.scenechange(master.frame0))
        button0.pack()

    def scenechange(self, page):
        page.tkraise()