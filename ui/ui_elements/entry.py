import customtkinter as ctk


class Entry:
    def __init__(self, master: object) -> None:
        self.master = master
        self.corner_radius: int = 5
        self.border_color: str = 'green'
        self.border_width: int = 1
        self.width: int = 200
        self.height: int = 28
        self.fg_color: str = '#1d1e1e'
        self.text_color: str = '#ffffff'

    def add_entry(self) -> ctk.CTkEntry:
        entry = ctk.CTkEntry(master=self.master,
                             corner_radius=self.corner_radius,
                             border_color=self.border_color,
                             border_width=self.border_width,
                             width=self.width,
                             height=self.height,
                             fg_color=self.fg_color,
                             text_color=self.text_color)

        return entry
