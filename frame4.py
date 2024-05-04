import tkinter as tk


class Frame_4(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        label = tk.Label(self, text='frame4', font=("MSゴシック", "40"))
        label.pack()
        
        button = tk.Button(self, text='framemusic', font=("MSゴシック", "20"), command=lambda: self.scenechange(master.framemusic))
        button.pack()

    def scenechange(self, page):
        page.tkraise()
