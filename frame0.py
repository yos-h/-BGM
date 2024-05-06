#frame0.py
import tkinter as tk
from getdata import GetData


class Frame_0(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        label = tk.Label(self, text='frame0', font=("MSゴシック", "40"))
        label.pack()

        button0 = tk.Button(self, text='option0(frame1)', font=("MSゴシック", "20"), command=lambda: self.scenechange1(master.frame1))
        button0.pack()
        button0 = tk.Button(self, text='option1(frame1)', font=("MSゴシック", "20"), command=lambda: self.scenechange2(master.frame1))
        button0.pack()

    def scenechange1(self, page):
        data = GetData()
        data.set_q_list(0,0)
        page.tkraise()

    def scenechange2(self, page):
        data = GetData()
        data.set_q_list(0,1)
        page.tkraise()