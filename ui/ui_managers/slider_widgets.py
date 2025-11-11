import customtkinter as ctk

from menu.connection_menu import ConnectionMenu
from menu.menu_consts import MenuConsts

class Widget(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        self.command_dict: dict = kwargs
        super().__init__(master)

    def create_widgets(self) -> None:
        self.command_dict: dict = {
            'Accept': self.command_dict['accept'],
            'Close': self.command_dict['close'],
            'Left Arrow': self.command_dict['left_arrow'],
            'Right Arrow': self.command_dict['right_arrow'],
        }
        self.button_frame = ctk.CTkFrame(master=self, fg_color='#333333')
        self.slider_buttons = ConnectionMenu.show_button(options=MenuConsts.SLIDER_BUTTON, master=self.button_frame, command=self.command_dict)

        self.arrows_frame = ctk.CTkFrame(master=self, fg_color='#333333')
        self.slider_arrow = ConnectionMenu.show_button(options=MenuConsts.SLIDER_BUTTON_ARROW, master=self.arrows_frame, command=self.command_dict)

        self.separator_label = ctk.CTkLabel(master=self.arrows_frame, text="||", font=ctk.CTkFont(size=16, weight="bold"))
        self.separator_label = ConnectionMenu.show_label(options=MenuConsts.SLIDER_LABEL, master=self.arrows_frame)

    def widget_configuration(self) -> None:
        self.button_frame.pack(side=ctk.BOTTOM, pady=(0, 10))
        self.slider_buttons[0]['Item'].pack(side=ctk.LEFT, fill=ctk.X, pady=5, padx=5)
        self.slider_buttons[1]['Item'].pack(side=ctk.LEFT, fill=ctk.X, pady=5, padx=5)

        self.arrows_frame.pack(side=ctk.BOTTOM, pady=(0, 10))
        self.slider_arrow[0]['Item'].pack(side=ctk.LEFT, padx=0)
        self.slider_arrow[0]['Item'].configure(width=60, height=20,)

        self.separator_label[0]['Item'].pack(side=ctk.LEFT, padx=10)

        self.slider_arrow[1]['Item'].pack(side=ctk.LEFT, padx=0)
        self.slider_arrow[1]['Item'].configure(width=60, height=20)

    def show_widgets(self) -> None:
        self.create_widgets()
        self.widget_configuration()