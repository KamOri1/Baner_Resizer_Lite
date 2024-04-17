import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import filedialog as fd
import APS_API as aps
import os
import serverConnection as sC
# import pngTowebp as ptw

class ServerLogView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.ftpOrSftp = None
        self.var = tk.StringVar()
        self.var.trace_add("write", self.update_radio_button_data)
        self.create_widgets()
        self.create_layout()
        self.tabb = self.passToServerChecker()






    def create_widgets(self):
        self.label1 = ctk.CTkLabel(master=self, text='Server: ', font=('Open Sans', 16))
        self.label2 = ctk.CTkLabel(master=self, text='User Name: ', font=('Open Sans', 16))
        self.label3 = ctk.CTkLabel(master=self, text='Password: ', font=('Open Sans', 16))
        self.label4 = ctk.CTkLabel(master=self, text='Path: ', font=('Open Sans', 16))
        self.serverDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1, width=200, height=10)
        self.userNameDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1, width=200, height=10)
        self.passwordDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1, width=200, height=10)
        self.pathDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1, width=200, height=10)
        self.R1 = ctk.CTkRadioButton(master=self, text="FTP", variable=self.var, value="ftp", hover_color='#d11507',
                                     radiobutton_width=15, radiobutton_height=15, font=('Open Sans', 14))
        self.R2 = ctk.CTkRadioButton(master=self, text="SFTP", variable=self.var, value="sftp", hover_color='#d11507',
                                     radiobutton_width=15, radiobutton_height=15, font=('Open Sans', 14))
        self.button_1 = ctk.CTkButton(self, text='Connect', width=100, fg_color="#0033FF", hover_color='#0000FF',
                                      font=('Open Sans', 14), command=self.fun)
        self.button_2 = ctk.CTkButton(self, text='Close', width=100, fg_color="red", hover_color='#d11507',
                                      font=('Open Sans', 14), command=self.close_frame)

    def create_layout(self):
        self.label1.place(x=60, y=40, anchor='center')
        self.label2.place(x=60, y=80, anchor='center')
        self.label3.place(x=60, y=120, anchor='center')
        self.label4.place(x=60, y=160, anchor='center')
        self.serverDate.place(x=220, y=40, anchor='center')
        self.userNameDate.place(x=220, y=80, anchor='center')
        self.passwordDate.place(x=220, y=120, anchor='center')
        self.pathDate.place(x=220, y=160, anchor='center')
        self.R1.place(x=60, y=210, anchor='center')
        self.R2.place(x=60, y=250, anchor='center')
        self.button_1.place(x=269, y=210, anchor='center')
        self.button_2.place(x=269, y=250, anchor='center')

    def close_frame(self):
        self.place_forget()
    def update_radio_button_data(self, *args):
        # Get the selected value from the variable
        self.ftpOrSftp = self.var.get()
    def passToServerChecker(self):
        self.hostname__ = str(self.serverDate.get('0.0', 'end').strip())
        self.username__ = str(self.userNameDate.get('0.0', 'end').strip())
        self.password__ = str(self.passwordDate.get('0.0', 'end').strip())
        self.ftpCatDir_ = str(self.pathDate.get('0.0', 'end').strip())
        self.tabb = [self.hostname__,self.username__, self.password__, self.ftpCatDir_, self.ftpOrSftp]
        # print(tabb)
        return self.tabb
    def fun(self):
        a = self.passToServerChecker()
        st = sC.ServerConnectionAction()
        st.connectionCheck(a[4],  a[0],  a[1],  a[2], a[3])
    def passToServerIfTrue(self):
        return self.passToServerChecker()
    def commander(self):

        # if self.hostname__ is not None and self.username__ is not None and self.password__ is not None and self.ftpCatDir_ is not None:
        sC.connectToServerSFTP(
            catDir="aa",
            hostname_=self.serverDate.get('0.0', 'end').strip(),
            username_=self.userNameDate.get('0.0', 'end').strip(),
            password_=self.passwordDate.get('0.0', 'end').strip(),
            ftpCatDir=self.pathDate.get('0.0', 'end').strip()
        )


