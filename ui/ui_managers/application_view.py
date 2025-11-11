import customtkinter as ctk
from . import connection_frame as cF
from . import main_frame as mF
from . import main_menu as menu
from . import mp4_slider_frame as sF


class Application(ctk.CTk):
    def __init__(self):
        # main setup
        super().__init__()
        self.title("Banner Resizer MarQ 5")
        self.geometry('600x300')
        self.resizable(False, False)
        self.configure(fg_color='#242424')

        # widgets

        self.create_left_frames()
        self.create_right_frames()

        self.mainloop()


    def create_left_frames(self) -> None:
        self.left_frame: ctk.CTkFrame = ctk.CTkFrame(self, fg_color='#333333', corner_radius=10, width=125)
        self.left_frame.pack(side='left', fill='both', expand=False, padx=10, pady=10)
        self.show_main_menu()

    def create_right_frames(self) -> None:
        self.right_frame: ctk.CTkFrame = ctk.CTkFrame(self, fg_color='#242424')
        self.right_frame.pack(side='right', fill='both', expand=True, padx=(0, 10), pady=10)
        self.show_main_frame()

    def show_connection_menu_frame(self) -> None:
        self.server_frame: ctk.CTkFrame = cF.ServerLogView(master=self.right_frame, corner_radius=10)
        self.server_frame.configure(width=445, height=280, fg_color='#333333', corner_radius=10)
        self.server_frame.place(x=220, y=140, anchor='center')

    def show_slider_frame(self, root=None) -> None:
        self.geometry('600x450')
        self.slider_frame: ctk.CTkFrame = sF.SliderFrame(master=self.right_frame, banner_frame=1,
                                                         mp4_list=2,
                                                         video_path=self.main_menu.banner_dir,
                                                         corner_radius=10,
                                                         mp4_mode=self.get_mp4_mode,
                                                         resize_param=self.get_format_data,
                                                         campaign_date=self.get_campaign_date,
                                                         root=root)


        self.slider_frame.configure(width=445, height=450, fg_color='#333333', corner_radius=10)
        self.slider_frame.pack(side='left', fill='both', expand=False, padx=1, pady=1)


    def show_main_frame(self) -> None:
        self.main_frame_look = mF.MainFrame(master=self.right_frame, corner_radius=10)
        self.main_frame: ctk.CTkFrame = self.main_frame_look
        self.main_frame.configure(width=445, height=280, fg_color='#333333', corner_radius=10)
        self.main_frame.place(x=220, y=140, anchor='center')

    def show_main_menu(self) -> None:
        self.main_menu = menu.MainMenu(master=self.left_frame, corner_radius=10,
                                       connection_menu=self.show_connection_menu_frame,
                                       file_path=self.update_file_path,
                                       campaign_date=self.get_campaign_date,
                                       resize_param=self.get_format_data,
                                       banner_frame=self.show_slider_frame,
                                       mp4_mode=self.get_mp4_mode)

        self.main: ctk.CTkFrame = self.main_menu
        self.main.configure(width=120, height=320, fg_color='#333333', corner_radius=10)
        self.main.place(x=60, y=115, anchor='center')

    def update_file_path(self) -> str:
        self.main_frame_look.stringvar.set(self.main_menu.banner_dir)
        path = self.main_frame_look.stringvar
        return path

    def get_mp4_mode(self):
        if hasattr(self.main_frame_look, 'switch_mp4_var'):
            mode = self.main_frame_look.switch_mp4_var.get()
            return mode

    def get_campaign_date(self) -> str:
        campaign_date = self.main_frame_look.get_campaign_date()
        return campaign_date

    def get_format_data(self) -> dict:
        format: str = self.main_frame_look.switch_b_mb_var.get()
        dimension: str = self.main_frame_look.radio_buttons_format_type_var.get()
        sunday_nsltr: str = self.main_frame_look.switch_sunday_var.get()
        photoshop: str = self.main_frame_look.switch_photoshop_var.get()
        web_p: str = self.main_frame_look.switch_webp_var.get()
        video_path = self.main_menu.banner_dir
        size = self.main_frame_look.radio_buttons_format_type_var.get()

        return {
            'format': format,
            'dimension': dimension,
            'sunday_nsltr': sunday_nsltr,
            'photoshop': photoshop,
            'web_p': web_p,
            'video_path': video_path,
            'size': size
        }