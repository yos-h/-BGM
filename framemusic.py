import tkinter as tk

class Frame_Music(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        label = tk.Label(self, text='framemusic', font=("MSゴシック", "40"))
        label.pack()

        button = tk.Button(self, text='framehome', font=("MSゴシック", "20"), command=lambda: self.scenechange(master.framehome))
        button.pack()


    def scenechange(self,page):
        page.tkraise()