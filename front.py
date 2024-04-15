import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import filedialog as fd
import APS_API as aps
import os


import serverConnection as sC
# import pngTowebp as ptw


class MenuFrame(ctk.CTkFrame):
    def __init__(self, comm, master, **kwargs):
        self.comm = comm
        super().__init__(master, **kwargs)
        # add widgets onto the frame...
        self.button_1 = ctk.CTkButton(self, text='Connection', width=100, fg_color="blue", hover_color='#34661e',
                                      font=('Open Sans', 14), command=self.comm)
        self.button_1.grid(row=0, column=0, )


class ServerLogView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame...
        self.label1 = ctk.CTkLabel(master=self, text='Server: ', font=('Open Sans', 16))
        self.label2 = ctk.CTkLabel(master=self, text='User Name: ', font=('Open Sans', 16))
        self.label3 = ctk.CTkLabel(master=self, text='Password: ', font=('Open Sans', 16))
        self.label4 = ctk.CTkLabel(master=self, text='Path: ', font=('Open Sans', 16))
        self.serverDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1,
                                         width=200, height=10)
        self.userNameDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1,
                                           width=200, height=10)
        self.passwordDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1,
                                           width=200, height=10)
        self.pathDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1,
                                           width=200, height=10)

        self.label1.place(x=60, y=40, anchor='center')
        self.label2.place(x=60, y=80, anchor='center')
        self.label3.place(x=60, y=120, anchor='center')
        self.label4.place(x=60, y=160, anchor='center')
        self.serverDate.place(x=220, y=40, anchor='center')
        self.userNameDate.place(x=220, y=80, anchor='center')
        self.passwordDate.place(x=220, y=120, anchor='center')
        self.pathDate.place(x=220, y=160, anchor='center')

        # self.dateforCatalog_.get('0.0', 'end')



        self.button_1 = ctk.CTkButton(self, text='Connect', width=100, fg_color="#0033FF", hover_color='#0000FF',
                                      font=('Open Sans', 14), command=self.fun)
        self.button_1.place(x=269, y=210, anchor='center')
        self.button_2 = ctk.CTkButton(self, text='Close', width=100, fg_color="red", hover_color='#d11507',
                                      font=('Open Sans', 14), command=self.zamknij_frame)
        self.button_2.place(x=269, y=250, anchor='center')
        self.tabb = self.passToServerChecker()
    def zamknij_frame(self):
        self.place_forget()

    def passToServerChecker(self):
        self.hostname__ = str(self.serverDate.get('0.0', 'end').strip())
        self.username__ = str(self.userNameDate.get('0.0', 'end').strip())
        self.password__ = str(self.passwordDate.get('0.0', 'end').strip())
        self.ftpCatDir_ = str(self.pathDate.get('0.0', 'end').strip())
        self.tabb = [self.hostname__,self.username__, self.password__, self.ftpCatDir_]
        # print(tabb)
        return self.tabb
    def fun(self):
        a = self.passToServerChecker()
        st = sC.ServerConnectionAction()
        st.connectionCheck("ftp",  a[0],  a[1],  a[2], a[3])

        print("ftp",  a[0],  a[1],  a[2], a[3])
    def commander(self):

        # if self.hostname__ is not None and self.username__ is not None and self.password__ is not None and self.ftpCatDir_ is not None:
        sC.connectToServerSFTP(
            catDir="aa",
            hostname_=self.serverDate.get('0.0', 'end').strip(),
            username_=self.userNameDate.get('0.0', 'end').strip(),
            password_=self.passwordDate.get('0.0', 'end').strip(),
            ftpCatDir=self.pathDate.get('0.0', 'end').strip()
        )



class App(ctk.CTk):
    def __init__(self):
        # main setup
        super().__init__()
        self.title("Banner Resizer")
        self.geometry('600x300')
        self.resizable(False, False)

        # widgets
        # self.my_frame = MenuFrame(self.serverFrame, master=self)
        # self.my_frame.configure(width=100)
        # self.my_frame.place(x=60, y=240, anchor='center')

        self.create_widgets()
        self.create_layout()
        # run
        self.mainloop()

    def serverFrame(self):
        self.my_serv = ServerLogView(master=self)
        self.my_serv.configure(width=450, height=280)
        self.my_serv.place(x=360, y=150, anchor='center')

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
        self.button_1 = ctk.CTkButton(master=self, text='Select folder', width=100, fg_color="green",
                                      hover_color='#34661e',
                                      font=('Open Sans', 14), command=self.get_banner_dir)
        self.button_2 = ctk.CTkButton(master=self, text='Resize', width=100, fg_color="green", hover_color='#34661e',
                                      font=('Open Sans', 14), command=self.resize_banner)
        self.button_3 = ctk.CTkButton(self, text='Connection', width=100, fg_color="#0033FF", hover_color='#0000FF',
                                      font=('Open Sans', 14), command=self.serverFrame)

        self.button_4 = ctk.CTkButton(master=self, text='Exit', width=100, fg_color="red", hover_color='#d11507',
                                      font=('Open Sans', 14), command=self.quite_app)

        self.ban_dir = None
        self.baner_size_data = None

    def create_layout(self):
        self.label1.place(x=255, y=40, anchor='center')
        self.dateforCatalog_.place(x=470, y=40, anchor='center')
        self.R1.place(x=197, y=80, anchor='center')
        self.R2.place(x=297, y=80, anchor='center')
        self.button_1.place(x=60, y=120, anchor='center')
        self.button_2.place(x=60, y=160, anchor='center')
        self.button_3.place(x=60, y=200, anchor='center')
        self.button_4.place(x=60, y=240, anchor='center')

    def update_cam_data(self, *args):
        # Get the selected value from the variable
        self.baner_size_data = self.var.get()

    def get_banner_dir(self):
        self.ban_dir = fd.askdirectory()  # Get the directory from button_1
        # self.button_2.config(state='normal')   Enable button_2 after directory selection
        if self.ban_dir is not None:
            self.dateforCatalog1_ = ctk.CTkTextbox(master=self, corner_radius=5, border_color='red', width=300,
                                                   height=10)
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
            aps.PhotoshopAPI(self.ban_dir, self.dateforCatalog_.get('0.0', 'end').strip(),
                             int(dimensions)).psBannerResizer()
            # ptw.convertToWebp(self.ban_dir)
            # ptw.convertToWebp2(self.ban_dir)
            print(ServerLogView(master=self).passToServerChecker()[2])
            arr = ServerLogView(master=self).commander()


            # sC.connectToServer(f"{self.ban_dir}\\Banner")

    def quite_app(self):
        self.quit()


# App()


