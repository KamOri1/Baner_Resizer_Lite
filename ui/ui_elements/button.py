from typing import Callable

import customtkinter as ctk


class Button:
    def __init__(self, text: str, fg_color: str, hover_color: str, command: Callable[[], None], master: object) -> None:
        self.text: str = text
        self.fg_color: str = fg_color
        self.hover_color: str = hover_color
        self.command: Callable[[], None] = command
        self.master: object = master
        self.width: int = 80
        self.height: int = 26
        self.font: tuple = ('Open Sans', 12)
        self.text_color = '#ffffff'

    def add_button(self) -> ctk.CTkButton:
        button = ctk.CTkButton(master=self.master,
                               text=self.text,
                               width=self.width,
                               height=self.height,
                               fg_color=self.fg_color,
                               hover_color=self.hover_color,
                               font=self.font,
                               command=self.command,
                               text_color=self.text_color)
        return button
