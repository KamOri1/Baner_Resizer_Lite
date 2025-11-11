import customtkinter as ctk
from tkinter import filedialog as fd

from menu.connection_menu import ConnectionMenu
from menu.menu_consts import MenuConsts
from image_processing.processing_manager import ProcessingImgManager



class MainMenu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        self.connection_menu = kwargs.pop('connection_menu')
        self.update_folder_localization = kwargs.pop('file_path')
        self.campaign_date = kwargs.pop('campaign_date')
        self.resize_param = kwargs.pop('resize_param')
        self.banner_frame = kwargs.pop('banner_frame')
        self.mp4_mode = kwargs.pop('mp4_mode')
        self.banner_dir = None

        super().__init__(master, **kwargs)
        self.command_dict: dict = {
            'SelectFolder': lambda: (self.get_banner_dir(), self.update_folder_localization()),
            'Resize': self.run_resize_process,
            'Resend': self.banner_frame,
            'Connection': self.connection_menu,
            'Exit': self.quite_app,

        }

        self.create_widgets()
        self._configure_widget()

    def create_widgets(self) -> None:
        self.main_menu_buttons = ConnectionMenu.show_button(options=MenuConsts.MAIN_MANU_BUTTON,
                                                                            master=self,
                                                                            command=self.command_dict)

    def _configure_widget(self) -> None:
        if self.banner_dir is None:
           self.main_menu_buttons[1]['Item'].configure(state="disabled")
        self.main_menu_buttons[2]['Item'].configure(state="disabled")

    def get_banner_dir(self) -> str:
        select_folder: str = fd.askdirectory()
        self.banner_dir = select_folder
        self.main_menu_buttons[1]['Item'].configure(state="normal")
        return self.banner_dir

    def run_resize_process(self) -> None:
        if self.banner_dir is not None:
            resize_param: dict = self.resize_param()
            prepare_img: ProcessingImgManager = ProcessingImgManager(
                file_path=self.banner_dir,
                file_name=self.campaign_date(),
                dimensions=int(resize_param['dimension']),
                is_b_bm_on=resize_param['format'],
                is_sd_on=resize_param['sunday_nsltr'],
                photoshop_or_not=resize_param['photoshop'],
                web_p=resize_param['web_p'],
                video_path=resize_param['video_path'],
                mp4_mode=self.mp4_mode(),
                banner_frame=self.banner_frame

            )

            prepare_img.prepare_image()
        else:
            print("Lokalizacja jest pusta")

    def quite_app(self) -> None:
        self.quit()

