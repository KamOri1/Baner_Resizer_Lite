import customtkinter as ctk

class Label:
    def __init__(self, text: str, master: object) -> None:
        self.text: str = text
        self.master: object = master
        self.font: tuple = ('Open Sans', 14)
        self.text_color: str = '#ffffff'


    def add_label(self) -> ctk.CTkLabel:
        label = ctk.CTkLabel(master=self.master,
                             text=self.text,
                             font=self.font,
                             text_color=self.text_color)

        return label
