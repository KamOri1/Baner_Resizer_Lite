import tkinter as tk
import customtkinter as ctk

from serverData import serverConnection as sC
from serverData import serverDefaultData as sP
from menu.connection_menu import ConnectionMenu
from menu.menu_consts import MenuConsts
from serverData import server_custom_data as sCd

class ServerLogView(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.ftpOrSftp = None
        self.connection_type_var = tk.StringVar()
        self.connection_type_var.trace_add("write", self.update_radio_button_data)
        self.default_data_switch_var = tk.StringVar(value="off")
        self.create_widgets()
        self.defaulValues = None
        self.tabb = self.passToServerChecker()
        self.configure(corner_radius=10)

    def create_widgets(self):
        (commands_buttons, commands_radio_buttons, variable_radio_buttons,
         commands_switch, variable_switch) = self._initialize_widget_data()

        self.connect_menu_labels = ConnectionMenu.show_label(options=MenuConsts.CONNECTION_LABELS,
                                                             master=self)
        self.connect_menu_buttons = ConnectionMenu.show_button(options=MenuConsts.CONNECTION_BUTTON,
                                                               master=self,
                                                               command=commands_buttons)
        self.connect_menu_entries = ConnectionMenu.show_entry(options=MenuConsts.CONNECTION_ENTRY,
                                                              master=self)
        self.connect_menu_radio_buttons = ConnectionMenu.show_radio_button(options=MenuConsts.CONNECTION_RADIO_BUTTON,
                                                                           master=self,
                                                                           command=commands_radio_buttons,
                                                                           variable=variable_radio_buttons)
        self.connect_menu_text_box = ConnectionMenu.show_text_box(options=MenuConsts.CONNECTION_TEXT_BOX,
                                                                  master=self)
        self.connect_menu_switch = ConnectionMenu.show_switch(options=MenuConsts.CONNECTION_SWITCH,
                                                              master=self, variable=variable_switch,
                                                              command=commands_switch)
        self._configure_widget()

    def _initialize_widget_data(self) -> tuple:
        commands_buttons: dict = {
            'Connect': self.test_connection,
            'Close': self.close_frame,
            'ShowPassword': self.showPassword
        }
        commands_radio_buttons: dict = {'clearData': lambda: (self.clearData(), self.default_data_switch_var.set("off"),self.connectButtonColor())}
        variable_radio_buttons: dict = {'var': self.connection_type_var}
        commands_switch: dict = {'addDefaulParam': self.add_default_param}
        variable_switch: dict = {'switch_var_0': self.default_data_switch_var}

        return (commands_buttons, commands_radio_buttons, variable_radio_buttons,
                commands_switch, variable_switch)

    def _configure_widget(self) -> None:
        self.connect_menu_buttons[2]['Item'].configure(font=('Open Sans', 14),
                                                       text_color='green',
                                                       height=16,
                                                       width=20,
                                                       hover=False,)
        self.connect_menu_entries[2]['Item'].configure(show="•")

    def showPassword(self) -> None:
        menu_entries = self.connect_menu_entries[2]["Item"]
        menu_buttons = self.connect_menu_buttons[2]['Item']
        match menu_entries.cget("show"):
            case '•':
                menu_entries.configure(show='')
                menu_buttons.configure(text_color='red')
            case '':
                menu_entries.configure(show='•')
                menu_buttons.configure(text_color='green')

    def update_radio_button_data(self, *args) -> str:
        default_data_switch = self.connect_menu_switch[0]["Item"]
        self.ftpOrSftp = self.connection_type_var.get()
        if self.ftpOrSftp is not None:
            default_data_switch.configure(state="normal")
        return self.ftpOrSftp

    def default_param(self) -> None:
        self.connectButtonColor()
        protocol = self.update_radio_button_data()
        passToServer = sP.passToSFTP if protocol == 'sftp' else sP.passToFTP

        keys_in_order = ['hostname', 'username', 'password']
        for index, key in enumerate(keys_in_order):
            self.connect_menu_entries[index]['Item'].insert('0', passToServer[key])
        self.connect_menu_text_box[0]["Item"].insert('0.0', passToServer['ftpCatDir'])

    def connectButtonColor(self) -> None:
        connectButton = self.connect_menu_buttons[0]['Item']
        if connectButton.cget('fg_color') != "#0033FF":
            connectButton.configure(fg_color="#0033FF", hover_color='#0000FF')

    def clearData(self) -> None:
        for entry in self.connect_menu_entries:
            entry["Item"].delete("0", "end")
        self.connect_menu_text_box[0]["Item"].delete("0.0", "end")

    def add_default_param(self) -> None:
        use_default_values = self.default_data_switch_var.get() == 'on'
        if use_default_values:
            self.default_param()
        else:
            self.clearData()

    def passToServerChecker(self) -> dict:
        credentials: dict = {}
        keys_in_order = ['hostname', 'username', 'password']
        for index, key in enumerate(keys_in_order):
            credentials[key] = str(self.connect_menu_entries[index]["Item"].get().strip())
        credentials["ftpCatDir"] = str(self.connect_menu_text_box[0]["Item"].get('0.0', 'end').strip())
        credentials["ftpOrSftp"] = self.ftpOrSftp

        return credentials

    def test_connection(self) -> None:
        menu_buttons = self.connect_menu_buttons[0]['Item']
        dataToConnect: dict = self.passToServerChecker()
        ServerConnecOn = sC.ServerConnectionAction(server_details=dataToConnect,catDir=dataToConnect['ftpCatDir'])
        ConnectResult = ServerConnecOn.connection_check()
        if ConnectResult:
            menu_buttons.configure(fg_color='green', hover_color='#34661e')
            sCd.VERIFIED_SERVER_DETAILS = dataToConnect
        else:
            menu_buttons.configure(fg_color='grey', hover_color='#696969')
            sCd.VERIFIED_SERVER_DETAILS = None

    def close_frame(self) -> None:
        self.place_forget()

