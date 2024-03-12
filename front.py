import tkinter as tk
import customtkinter
from tkinter import filedialog as fd
import APS_API as aps


class Front_app:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('400x400')

        self.label1 = tk.Label(text='Podaj date kampani YYYY/MM/DD: ')
        self.dateforCatalog_ = tk.Entry()
        self.label1.grid(row=1, column=0)
        self.dateforCatalog_.grid(row=1, column=1)
        self.var = tk.IntVar()
        self.var.trace_add("write", self.update_cam_data)
        self.R1 = tk.Radiobutton(self.window, text="610x242", variable=self.var, value=610)
        self.R1.grid(row=2, column=0)
        self.R2 = tk.Radiobutton(self.window, text="650x490", variable=self.var, value=650)
        self.R2.grid(row=2, column=1)
        self.button_1 = tk.Button(text='Make a Banner', width=20, bg="green", fg="yellow", command=self.get_banner_dir)
        self.button_1.grid(row=3, column=0)
        self.button_2 = tk.Button(text='Make a Banner', width=20, bg="green", fg="yellow", command=self.resize_banner)
        self.button_2.grid(row=3, column=1)
        self.window.mainloop()
        self.ban_dir = None
        self.baner_size_data = None

    def update_cam_data(self, *args):
        # Get the selected value from the variable
        self.baner_size_data = self.var.get()
    def get_banner_dir(self):
        self.ban_dir = fd.askdirectory()  # Get the directory from button_1
        #self.button_2.config(state='normal')   Enable button_2 after directory selection

    def resize_banner(self):
        if self.ban_dir is not None and self.baner_size_data is not None:  # Check if a directory is selected
            # Use the retrieved ban_dir from button_1
            dimensions = self.baner_size_data
            aps.psBannerResizer(self.ban_dir, '2', int(dimensions) )





















