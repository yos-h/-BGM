import tkinter as tk


class Frame_Home(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        label = tk.Label(self, text='home', font=("MSゴシック", "40"))
        label.pack()
        
        button0 = tk.Button(self, text='framerule', font=("MSゴシック", "20"), command=lambda: self.scenechange(master.framerule))
        button0.pack()

        buttonex = tk.Button(self, text='exit', font=("MSゴシック", "20"), command=lambda: master.destroy())
        buttonex.pack()

    def scenechange(self, page):
        page.tkraise()
