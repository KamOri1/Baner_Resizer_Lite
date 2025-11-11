from tkinter import StringVar
from typing import Callable
import customtkinter as ctk

class RadioButton:
    def __init__(self, text: str, variable: StringVar, value: str, command: Callable[[], None], master: object) -> None:
        self.text: str = text
        self.variable: StringVar = variable
        self.master: object = master
        self.value: str = value
        self.command: Callable[[], None] = command
        self.hover_color: str = '#d11507'
        self.radiobutton_width: int = 15
        self.radiobutton_height: int = 15
        self.font: tuple =('Open Sans', 14)
        self.border_width_checked: int = 2
        self.border_width_unchecked: int = 2
        self.fg_color: str = '#d11507'
        self.text_color: str = '#ffffff'

    def add_radio_button(self) -> ctk.CTkRadioButton:
        radioButton = ctk.CTkRadioButton(master=self.master,
                                         text=self.text,
                                         variable=self.variable,
                                         value=self.value,
                                         hover_color=self.hover_color,
                                         radiobutton_width=self.radiobutton_width,
                                         radiobutton_height=self.radiobutton_height,
                                         font=self.font,
                                         border_width_checked=self.border_width_checked,
                                         border_width_unchecked=self.border_width_unchecked,
                                         fg_color=self.fg_color,
                                         command=self.command,
                                         text_color=self.text_color)

        return radioButton
