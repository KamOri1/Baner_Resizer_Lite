import customtkinter as ctk
from typing import Callable


class Switch:
    def __init__(self, master: object, text: str,variable,  command: Callable[[], None], state: str) -> None:
        self.master = master
        self.text: str = text
        self.variable = variable
        self.onvalue: str = "on"
        self.offvalue: str = "off"
        self.progress_color: str = 'green'
        self.fg_color: str = 'red'
        self.switch_height: int = 13
        self.font: tuple = ('Open Sans', 14)
        self.command: Callable[[], None] = command
        self.state = state
        self.text_color: str = '#ffffff'

    def add_switch(self) -> ctk.CTkSwitch:
        switch: ctk.CTkSwitch = ctk.CTkSwitch(master=self.master,
                                            text=self.text,
                                            variable=self.variable,
                                            onvalue=self.onvalue,
                                            offvalue=self.offvalue,
                                            progress_color=self.progress_color,
                                            fg_color=self.fg_color,
                                            switch_height=self.switch_height,
                                            font=self.font,
                                            command=self.command,
                                            state=self.state,
                                            text_color=self.text_color,
                                            )

        return switch
