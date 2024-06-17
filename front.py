import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog as fd
import APS_API as aps
import os
import connectionFrame as cF
import serverConnection as sC
import pngTowebp as ptw
import serverPass as sP
import name_cleaning
import file_copy

class App(ctk.CTk):
    def __init__(self):
        # main setup
        super().__init__()
        self.title("Banner Resizer")
        self.geometry('600x300')
        self.resizable(False, False)
        self.configure(fg_color='#242424')
        self.flag = False
        self.stringvar = tk.StringVar()

        # widgets
        self.create_widgets()
        self.create_layout()

        # run
        self.mainloop()
    def sprw(self):

        if self.flag == True:
            if self.my_serv.winfo_ismapped() == 0:
                self.serverFrame()
                self.flag = True

        elif self.flag == False:
                self.serverFrame()
                self.flag = True

    def serverFrame(self):
            self.my_serv = cF.ServerLogView(master=self)
            self.my_serv.configure(width=450, height=280, fg_color='#2b2b2b')
            self.my_serv.place(x=360, y=150, anchor='center')
            self.my_serv.connectionTest()

    def create_widgets(self):
        self.label1 = ctk.CTkLabel(master=self, text='Campaign date YYYYMMDD: ', font=('Open Sans', 14), text_color='#ffffff')
        self.dateforCatalog_ = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1,
                                          width=200, height=10,fg_color='#1d1e1e', text_color='#ffffff')
        self.dateforCatalog1_ = ctk.CTkLabel(master=self, textvariable=self.stringvar, width=300,  height=20, text_color='#ffffff',
                                             fg_color='#1d1e1e', wraplength=300, justify='left')
        self.switch_var_0 = tk.StringVar(value="on")
        self.switch_var_1 = tk.StringVar(value="on")
        # self.switch_var.trace_add("write", self.switch_event)
        self.switch_0 = ctk.CTkSwitch(master=self, text="b _mb", variable=self.switch_var_0, onvalue="on", offvalue="off",
                                      progress_color='green', fg_color='red', switch_height=13, font=('Open Sans', 14), text_color='#ffffff')
        self.switch_1= ctk.CTkSwitch(master=self, text=".webp", variable=self.switch_var_1,onvalue="on", offvalue="off",
                                     progress_color='green',fg_color='red', switch_height=13,font=('Open Sans', 14), text_color='#ffffff')
        self.var = tk.IntVar()
        self.var.trace_add("write", self.update_cam_data)
        self.R1 = ctk.CTkRadioButton(master=self, text="610x242", variable=self.var, value=610, hover_color='#d11507',
                                     radiobutton_width=15, radiobutton_height=15, font=('Open Sans', 14), border_width_checked=2,border_width_unchecked=2, fg_color='#d11507', text_color='#ffffff')
        self.R2 = ctk.CTkRadioButton(master=self, text="650x490", variable=self.var, value=650, hover_color='#d11507',
                                     radiobutton_width=15, radiobutton_height=15, font=('Open Sans', 14), border_width_checked=2,border_width_unchecked=2, fg_color='#d11507', text_color='#ffffff')
        self.button_1 = ctk.CTkButton(master=self, text='Select folder', width=80, height=26, fg_color="green",
                                      hover_color='#34661e',
                                      font=('Open Sans', 12), command=self.get_banner_dir, text_color='#ffffff')
        self.button_2 = ctk.CTkButton(master=self, text='Resize', width=80, height=26, fg_color="green", hover_color='#34661e',
                                      font=('Open Sans', 12), command=self.resize_banner, state="disabled", text_color='#ffffff')
        self.button_3 = ctk.CTkButton(master=self, text='Resend', width=80, height=26, fg_color="#0033FF", hover_color='#0000FF',
                                      font=('Open Sans', 12), command=self.sendFiletoServer , state="disabled", text_color='#ffffff')
        self.button_4 = ctk.CTkButton(self, text='Connection', width=80, height=26, fg_color="#0033FF", hover_color='#0000FF',
                                      font=('Open Sans', 12), command=self.sprw, text_color='#ffffff')

        self.button_5 = ctk.CTkButton(master=self, text='Exit', width=80, height=26, fg_color="#e33118", hover_color='#d11507',
                                      font=('Open Sans', 12), command=self.quite_app, text_color='#ffffff')

        self.ban_dir = None
        self.baner_size_data = None
        self.switch_data_0 = None
        self.switch_data_1 = None
        self.my_serv = None


    def create_layout(self):
        self.label1.place(x=255, y=40, anchor='center')
        self.dateforCatalog_.place(x=470, y=40, anchor='center')
        self.switch_0.place(x=220, y=80, anchor='center')
        self.switch_1.place(x=320, y=80, anchor='center')
        self.R1.place(x=422, y=80, anchor='center')
        self.R2.place(x=522, y=80, anchor='center')
        self.button_1.place(x=60, y=85, anchor='center')
        self.button_2.place(x=60, y=125, anchor='center')
        self.button_3.place(x=60, y=165, anchor='center')
        self.button_4.place(x=60, y=205, anchor='center')
        self.button_5.place(x=60, y=245, anchor='center')
        self.dateforCatalog1_.place(x=420, y=122, anchor='center')


    def update_cam_data(self, *args):
        self.baner_size_data = self.var.get()

    def switch_event_0(self):
        self.switch_data_0 = self.switch_var_0.get()
        return self.switch_data_0
    def switch_event_1(self):
        self.switch_data_1 = self.switch_var_1.get()
        return self.switch_data_1
    def ban_dir_update(self):
        self.stringvar.set(self.ban_dir)
    def get_banner_dir(self):
        # stringvar = tk.StringVar()

        self.ban_dir = fd.askdirectory()  # Get the directory from button_1
        self.ban_dir_update()
        if self.ban_dir is not None:

            self.button_2.configure(state="normal")
            self.button_3.configure(state="normal")
            self.resizeFlag = True

    def resize_banner(self):
        if self.ban_dir is not None and self.baner_size_data is not None:  # Check if a directory is selected
            dimensions = self.baner_size_data
            banner_check = list(os.listdir(f"{self.ban_dir}"))
            plik_jpg_istnieje = any(
                plik.endswith(rozszerzenie) for plik in banner_check for rozszerzenie in ['.jpg', '.png', '.mp4'])
            if plik_jpg_istnieje == True:
                if os.path.exists(f"{self.ban_dir}\\Banner") == False:
                    os.makedirs(f"{self.ban_dir}\\Banner")

                self.cleaning_napespace()

                is_b_bm_on = self.switch_event_0()
                photoShopAPi =aps.PhotoshopAPI(self.ban_dir, self.dateforCatalog_.get('0.0', 'end').strip(),
                                 int(dimensions), is_b_bm_on)
                photoShopAPi.psBannerResizer()
                self.copy_dach_fr(self.dateforCatalog_.get('0.0', 'end').strip(),self.m_or_mb_(dimensions, is_b_bm_on))
                banner_check = list(os.listdir(f"{self.ban_dir}\\Banner"))
                comm = f' {str(len(banner_check))} banners have been prepared '
                print(f'{comm:=^80}')
                self.webPisON()
                self.sendFiletoServer()
            else:
                print('There are no files to scale in this directory')

    def sendFiletoServer(self):

        if self.my_serv is not None:
            sendFile = self.my_serv.passToServerIfTrue()
            sC.ServerConnectionAction().connectioFtpOrSftp(sendFile['ftpORsftp'],
                                                           f"{self.ban_dir}\\Banner",
                                                           sendFile['hostname'],
                                                           sendFile['username'],
                                                           sendFile['password'],
                                                           sendFile['ftpCatDir'])

        else:
            if '' not in sP.passToFTP.values():
                try:
                    sC.ServerConnectionAction().connectToServerFTP(f"{self.ban_dir}\\Banner")
                except FileNotFoundError as e:
                    print(e)
            else:
                print('Complete the server data')



    def webPisON(self):
        webp = self.switch_event_1()
        if webp == 'on':
            ptw.convertToWebp2(self.ban_dir)

    def cleaning_napespace(self):
        spr = name_cleaning.Clean_File_Name(self.ban_dir)
        spr.clear_name()
        #print('poprawa nazw zakończona')


    def copy_dach_fr(self, data, ext):

        f_cop = file_copy.Copy_Missing_C(self.ban_dir)
        f_cop.file_copy_dach_2(data, ext)
        # print('duplikowanie dach zakończone')
        f_cop.file_copy_chf_2(data, ext)
        # print('duplikowanie CHFR zakończone')
    def m_or_mb_(self, dimension, on_of):
        if on_of == 'on':
            if int(dimension) == 650:

                return '_mb'
            else:
                return 'b'
        else:
            return ''
    def quite_app(self):
        self.quit()


