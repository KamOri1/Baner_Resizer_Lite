import os

import customtkinter as ctk

from resizingMethod.systemResize import convert_mp4
from banner_slider import slider
from resizingMethod.systemResize import systemResize as sR
from resizingMethod import paramCheck as pC
from image_processing import file_copy as fC
from serverData import serverConnection as sC
from serverData import serverDefaultData as serverPass

class SliderFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        self.banner_frame = kwargs.pop('banner_frame')
        self.mp4_list = kwargs.pop('mp4_list')
        self.video_path = kwargs.pop('video_path')
        self.mp4_mode = kwargs.pop('mp4_mode')
        self.resize_param = kwargs.pop('resize_param')
        self.campaign_date = kwargs.pop('campaign_date')
        self.root = kwargs.pop('root')
        self.catalog_name = self.campaign_date()

        super().__init__(master, **kwargs)
        self.command_dict: dict = {
            'Accept': self.close_frame,
        }
        self.frame: int = 0
        resize_param: dict = self.resize_param()
        if resize_param['sunday_nsltr'] == 'on':
            banner_list: list = list(os.listdir(f"{self.root}"))
            self.catalog_name = self.root.split("\\")[-1]
            if any(item.endswith('.mp4') for item in banner_list):
                self.video_path = self.root

        self.convert_mp4 = convert_mp4.ConvertFromMP4(video_path=self.video_path, mp4_mode='off', selected_frame=self.frame)
        self.viewer = None
        self.create_widgets()

    def create_widgets(self) -> None:
        video_data_extractor = self.convert_mp4
        keyframes = video_data_extractor.extract_one_frame_per_second()

        self.viewer = slider.FrameViewer(master=self, keyframes=keyframes, close_callback=self.close_frame, banner_catalog_name=self.catalog_name, close=self.close)
        self.viewer.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

    def close_frame(self) -> None:
        self.close()

        chosen_frame = self.viewer.chosen_frame()
        self.frame = chosen_frame * 30
        frame = chosen_frame * 30

        resize_param: dict = self.resize_param()
        if resize_param['sunday_nsltr'] == 'off':
            self.master.master.geometry('600x300')




        self.convert_mp4.save_all_first_frame_as_png(selected_frame=frame)
        self.resize_converted_frame()

        return frame


    def close(self) -> None:
        self.pack_forget()
        self.master.master.update_idletasks()
        #self.master.master.geometry('600x300')

    def send_file_to_server(self, catDir):
        serverData = serverPass.passToFTP
        serverData['ftpOrSftp'] = 'ftp'

        connection = sC.ServerConnectionAction(server_details=serverData, catDir=catDir)
        connection.connection_ftp_or_sftp()

    def resize_converted_frame(self):
        resize_param: dict = self.resize_param()

        for root, dir, files in os.walk(self.video_path):
            if os.path.basename(root).lower() == 'banner':
                continue

            if resize_param['sunday_nsltr'] == 'on':
                if os.path.basename(root) != 'Banner':
                    file_name = os.path.basename(root)
            else:
                file_name = self.campaign_date()

            sR.ResizeFile(catDir=self.video_path,
                          data=file_name,
                          width_height=int(resize_param['size']),
                          b_mb=resize_param['format'],
                          is_sd_on=resize_param['sunday_nsltr'])

        dimension = int(resize_param['size'])
        check_banner_ext = pC.ScalingParametersCheck(width_height=dimension, b_mb=resize_param['format'])
        banner_ext = check_banner_ext.image_params
        add_missing_banner = fC.CopyMissingBanner(file_path=self.video_path, data=file_name, ext=banner_ext['b_mb'])
        add_missing_banner.start_copy_processing()
        self.send_file_to_server(catDir=fr'{self.video_path}/Banner')
