import tkinter as tk
import customtkinter as ctk

from menu.connection_menu import ConnectionMenu
from menu.menu_consts import MenuConsts


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        self.switch_mp4_var = tk.StringVar(value="on")

        super().__init__(master, **kwargs)
        self.stringvar = tk.StringVar()
        self.configure(corner_radius=10)
        self.radio_buttons_format_type_var = tk.StringVar(value="610")
        self.switch_b_mb_var = tk.StringVar(value="on")
        self.switch_sunday_var = tk.StringVar(value="off")
        self.switch_webp_var = tk.StringVar(value="off")
        self.switch_photoshop_var = tk.StringVar(value="off")


        self.create_widgets()

        # run

    def create_widgets(self):
        (commands_radio_buttons, variable_radio_buttons,
         commands_switch, variable_switch) = self._initialize_widget_data()

        self.main_menu_labels = ConnectionMenu.show_label(options=MenuConsts.MAIN_MENU_LABELS,
                                                          master=self)

        self.main_menu_text_box = ConnectionMenu.show_text_box(options=MenuConsts.MAIN_MENU_TEXT_BOX,
                                                               master=self)

        self.main_menu_radio_buttons = ConnectionMenu.show_radio_button(options=MenuConsts.MAIN_MENU_RADIO_BUTTON,
                                                                        master=self,
                                                                        command=commands_radio_buttons,
                                                                        variable=variable_radio_buttons)
        self.main_menu_switch = ConnectionMenu.show_switch(options=MenuConsts.MAIN_MENU_SWITCH,
                                                           master=self, variable=variable_switch,
                                                           command=commands_switch)
        self._configure_widget()

    def _initialize_widget_data(self) -> tuple:
        commands_switch: dict = {'resend_block': None}
        variable_switch: dict = {'switch_b_mb_var': self.switch_b_mb_var,
                                 'switch_webp_var': self.switch_webp_var,
                                 'switch_photoshop_var': self.switch_photoshop_var,
                                 'switch_sunday_var': self.switch_sunday_var,
                                 'switch_mp4_var': self.switch_mp4_var,
                                 }
        commands_radio_buttons: dict = {'resend_block': self.get_campaign_date}
        variable_radio_buttons: dict = {'format_type_var': self.radio_buttons_format_type_var}
        return (commands_radio_buttons, variable_radio_buttons,
                commands_switch, variable_switch)

    def _configure_widget(self) -> None:
        self.main_menu_labels[1]['Item'].configure(width=280,
                                                   height=25,
                                                   text_color='#ffffff',
                                                   fg_color='#1d1e1e',
                                                   wraplength=280,
                                                   justify='left',
                                                   corner_radius=5,
                                                   padx=5,
                                                   pady=5,
                                                   font=('Open Sans', 10),
                                                   textvariable=self.stringvar
                                                   )

    def get_campaign_date(self) -> str | None:
        textbox_item = self.main_menu_text_box[0]['Item']
        textbox_value = textbox_item.get("1.0", "end-1c")
        if textbox_item is not None:
            return textbox_value
        return None

    def get_mp4_switch_value(self) -> str:

        return self.switch_mp4_var.get()
    def close_frame(self) -> None:
        self.place_forget()
