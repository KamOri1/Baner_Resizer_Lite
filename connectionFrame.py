import tkinter as tk
import customtkinter as ctk
import serverConnection as sC
import serverPass as sP
import front
class ServerLogView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame...
        self.ftpOrSftp = None
        self.var = tk.StringVar()
        self.var.trace_add("write", self.update_radio_button_data)
        self.create_widgets()
        self.create_layout()
        self.defaulValues = None
        self.tabb = self.passToServerChecker()


    def create_widgets(self):
        self.label1 = ctk.CTkLabel(master=self, text='Server: ', font=('Open Sans', 14), text_color='#ffffff')
        self.label2 = ctk.CTkLabel(master=self, text='User Name: ', font=('Open Sans', 14), text_color='#ffffff')
        self.label3 = ctk.CTkLabel(master=self, text='Password: ', font=('Open Sans', 14), text_color='#ffffff')
        self.label4 = ctk.CTkLabel(master=self, text='Path: ', font=('Open Sans', 14), text_color='#ffffff')
        self.serverDate = ctk.CTkEntry(master=self, corner_radius=5, border_color='green', border_width=1, width=200,
                                       height=28, fg_color='#1d1e1e', text_color='#ffffff')
        self.userNameDate = ctk.CTkEntry(master=self, corner_radius=5, border_color='green', border_width=1, width=200,
                                         height=28, fg_color='#1d1e1e', text_color='#ffffff')
        self.showPass = ctk.CTkButton(master=self, text=chr(0x1F441), anchor='center', font=('Open Sans', 14),
                                      text_color='green', height=16, width=20, fg_color='#2b2b2b', hover_color=None,
                                      hover=False, command=self.showPassword)
        self.passwordDate = ctk.CTkEntry(master=self, corner_radius=5, border_color='green', border_width=1, width=200,
                                         height=28, fg_color='#1d1e1e', show="•", text_color='#ffffff')
        self.pathDate = ctk.CTkTextbox(master=self, corner_radius=5, border_color='green', border_width=1, width=200,
                                       height=10, fg_color='#1d1e1e', text_color='#ffffff')
        self.R1 = ctk.CTkRadioButton(master=self, text="FTP", variable=self.var, value="ftp", hover_color='#d11507',
                                     radiobutton_width=15, radiobutton_height=15, font=('Open Sans', 14),
                                     border_width_checked=2,border_width_unchecked=2, fg_color='#d11507',command=self.clearData, text_color='#ffffff')
        self.R2 = ctk.CTkRadioButton(master=self, text="SFTP", variable=self.var, value="sftp", hover_color='#d11507',
                                     radiobutton_width=15, radiobutton_height=15, font=('Open Sans', 14),
                                     border_width_checked=2,border_width_unchecked=2, fg_color='#d11507',command=self.clearData, text_color='#ffffff')
        self.switch_var_0 = tk.StringVar(value="off")
        self.switch_0 = ctk.CTkSwitch(master=self, text="Default data ", variable=self.switch_var_0, onvalue="on",
                                      offvalue="off",
                                      progress_color='green', fg_color='red', switch_height=13, font=('Open Sans', 14),
                                      command=self.addDefaulParam, state="disabled", text_color='#ffffff')
        self.button_1 = ctk.CTkButton(self, text='Connect', width=80, height=26, fg_color="#0033FF", hover_color='#0000FF',
                                      font=('Open Sans', 12), command=self.connectionTest, text_color='#ffffff')
        self.button_2 = ctk.CTkButton(self, text='Close', width=80, height=26, fg_color="#e33118", hover_color='#d11507',
                                      font=('Open Sans', 12), command=self.close_frame, text_color='#ffffff')

    def create_layout(self):
        self.label1.place(x=60, y=40, anchor='center')
        self.label2.place(x=60, y=80, anchor='center')
        self.label3.place(x=60, y=120, anchor='center')
        self.label4.place(x=60, y=160, anchor='center')
        self.serverDate.place(x=220, y=40, anchor='center')
        self.userNameDate.place(x=220, y=80, anchor='center')
        self.showPass.place(x=335, y=120, anchor='center')
        self.passwordDate.place(x=220, y=120, anchor='center')
        self.pathDate.place(x=220, y=160, anchor='center')
        self.R1.place(x=70, y=210, anchor='center')
        self.R2.place(x=130, y=210, anchor='center')
        self.switch_0.place(x=70, y=250, anchor='center')
        self.button_1.place(x=269, y=210, anchor='center')
        self.button_2.place(x=269, y=250, anchor='center')


    def showPassword(self):
        showPass = self.passwordDate.cget("show")
        if showPass == '•':
            self.passwordDate.configure(show='')
            self.showPass.configure(text_color='red')
        else:
            self.passwordDate.configure(show='•')
            self.showPass.configure(text_color='green')

    def update_radio_button_data(self, *args):
        self.ftpOrSftp = self.var.get()
        if self.ftpOrSftp is not None:
            self.switch_0.configure(state="normal")
        return self.ftpOrSftp

    def switch_event_0(self):
        self.switch_data_0 = self.switch_var_0.get()
        return self.switch_data_0

    def addDefaulParam(self):
        self.defaulValues = self.switch_event_0()
        ftpORsftp = self.update_radio_button_data()
        if self.button_1.cget('fg_color') == 'green' or self.button_1.cget('fg_color') == 'grey':
            self.button_1.configure(fg_color="#0033FF", hover_color='#0000FF')
        if self.defaulValues == 'on':

            if ftpORsftp == 'sftp':
                self.serverDate.insert('0', sP.passToSFTP['hostname'])
                self.userNameDate.insert('0', sP.passToSFTP['username'])
                self.passwordDate.insert('0', sP.passToSFTP['password'])
                self.pathDate.insert('0.0', sP.passToSFTP['ftpCatDir'])
            elif ftpORsftp == 'ftp':
                self.serverDate.insert('0', sP.passToFTP['hostname'])
                self.userNameDate.insert('0', sP.passToFTP['username'])
                self.passwordDate.insert('0', sP.passToFTP['password'])
                self.pathDate.insert('0.0', sP.passToFTP['ftpCatDir'])
        elif self.defaulValues == 'off':
            self.serverDate.delete("0", "end")
            self.userNameDate.delete("0", "end")
            self.passwordDate.delete("0", "end")
            self.pathDate.delete("0.0", "end")
    def clearData(self):
        self.serverDate.delete("0", "end")
        self.userNameDate.delete("0", "end")
        self.passwordDate.delete("0", "end")
        self.pathDate.delete("0.0", "end")
        self.switch_var_0.set("off")
        if self.button_1.cget('fg_color') == 'green' or self.button_1.cget('fg_color') == 'grey':
                self.button_1.configure(fg_color="#0033FF", hover_color='#0000FF')



    def close_frame(self):
        self.place_forget()

    def passToServerChecker(self):
        self.hostname__ = str(self.serverDate.get().strip())
        self.username__ = str(self.userNameDate.get().strip())
        self.password__ = str(self.passwordDate.get().strip())
        self.ftpCatDir_ = str(self.pathDate.get('0.0', 'end').strip())
        self.credentials = {
            "hostname": self.hostname__,
            "username": self.username__,
            "password": self.password__,
            "ftpCatDir": self.ftpCatDir_,
            "ftpORsftp": self.ftpOrSftp
        }
        return self.credentials
    def connectionTest(self):
        dataToConnect = self.passToServerChecker()
        ServerConnecOn = sC.ServerConnectionAction()
        ConnectResult = ServerConnecOn.connectionCheck(dataToConnect['ftpORsftp'],
                                       dataToConnect['hostname'],
                                       dataToConnect['username'],
                                       dataToConnect['password'],
                                       dataToConnect['ftpCatDir'])
        if ConnectResult == True:
            self.button_1.configure(fg_color='green', hover_color='#34661e')
        elif ConnectResult == False:
            self.button_1.configure(fg_color='grey', hover_color='#696969')


    def passToServerIfTrue(self):
        return self.passToServerChecker()


