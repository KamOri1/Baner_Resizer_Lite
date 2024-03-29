import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import filedialog as fd
import APS_API as aps
import os
#import serverConnection as sC
#import pngTowebp as ptw

class App(ctk.CTk):
    def __init__(self):
        #main setup
        super().__init__()
        self.title("Banner Resizer")
        self.geometry('500x300')
        self.resizable(False, False)

        # widgets
        self.create_widgets()
        self.create_layout()
        # run
        self.mainloop()






    def create_widgets(self):
        self.label1 = ctk.CTkLabel(master=self, text='Campaign date YYYYMMDD: ', font=('Open Sans', 16))
        self.dateforCatalog_ = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1,
                                              width=200, height=10)
        self.var = tk.IntVar()
        self.var.trace_add("write", self.update_cam_data)
        self.R1 = ctk.CTkRadioButton(master=self, text="610x242", variable=self.var, value=610, hover_color='#d11507',
                                     radiobutton_width=15, radiobutton_height=15, font=('Open Sans', 14))
        self.R2 = ctk.CTkRadioButton(master=self, text="650x490", variable=self.var, value=650, hover_color='#d11507',
                                     radiobutton_width=15, radiobutton_height=15, font=('Open Sans', 14))
        self.button_1 = ctk.CTkButton(master=self, text='Select folder', width=100, fg_color="green", hover_color='#34661e',
                                      font=('Open Sans', 14), command=self.get_banner_dir)
        self.button_2 = ctk.CTkButton(master=self, text='Resize', width=100, fg_color="green", hover_color='#34661e',
                                      font=('Open Sans', 14), command=self.resize_banner)
        self.button_3 = ctk.CTkButton(master=self, text='Exit', width=100, fg_color="red", hover_color='#d11507',
                                      font=('Open Sans', 14), command=self.quite_app)

        self.ban_dir = None
        self.baner_size_data = None

    def create_layout(self):
        self.label1.place(x=120, y=40, anchor='center')
        self.dateforCatalog_.place(x=350, y=40, anchor='center')
        self.R1.place(x=68, y=80, anchor='center')
        self.R2.place(x=160, y=80, anchor='center')
        self.button_1.place(x=60, y=120, anchor='center')
        self.button_2.place(x=60, y=160, anchor='center')
        self.button_3.place(x=60, y=200, anchor='center')

    def update_cam_data(self, *args):
        # Get the selected value from the variable
        self.baner_size_data = self.var.get()

    def get_banner_dir(self):
        self.ban_dir = fd.askdirectory()  # Get the directory from button_1
        #self.button_2.config(state='normal')   Enable button_2 after directory selection
        if self.ban_dir is not None:
            self.dateforCatalog1_ = ctk.CTkTextbox(master=self, corner_radius=5, border_color='red', width=300, height=10)
            self.dateforCatalog1_.place(x=300, y=120, anchor='center')
            self.dateforCatalog1_.insert('0.0', self.ban_dir)
            self.dateforCatalog1_.configure(state="disabled")

    def resize_banner(self):
        if self.ban_dir is not None and self.baner_size_data is not None:  # Check if a directory is selected
            # Use the retrieved ban_dir from button_1
            dimensions = self.baner_size_data
            if os.path.exists(f"{self.ban_dir}\\Banner") == False:
                os.makedirs(f"{self.ban_dir}\\Banner")
            print(f"To jest to: {self.dateforCatalog_.get('0.0', 'end')}")
            aps.PhotoshopAPI(self.ban_dir, self.dateforCatalog_.get('0.0', 'end').strip(), int(dimensions)).psBannerResizer()
            # ptw.convertToWebp(self.ban_dir)
            # ptw.convertToWebp2(self.ban_dir)

            # sC.connectToServer(f"{self.ban_dir}\\Banner")
    def quite_app(self):
        self.quit()
App()


