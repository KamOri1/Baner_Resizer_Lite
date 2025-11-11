import os

from .photoshopApi import apsResize as pSa
from .systemResize import systemResize as sR
from .systemResize import convert_mp4 as mp4


class Manager:
    def __init__(self, root, file_name, dimensions, is_b_bm_on, is_sd_on, photoshop_or_not, video_path, mp4_mode,
                 banner_frame):
        self.root = root
        self.file_name = file_name
        self.dimensions = dimensions
        self.is_b_bm_on = is_b_bm_on
        self.is_sd_on = is_sd_on
        self.photoshop_or_not = photoshop_or_not
        self.video_path = video_path
        self.mp4_mode = mp4_mode
        self.banner_frame = banner_frame
        self.banner_list: list = list(os.listdir(f"{self.root}"))

    def scaled_method(self):
        match self.photoshop_or_not:
            case "on":
                photoShopAPi = pSa.PhotoshopAPI(self.root, self.file_name, self.dimensions, self.is_b_bm_on,
                                                self.is_sd_on)
                photoShopAPi.psBannerResizer()
            case "off":
                match self.mp4_mode:
                    case 'on':
                        mp4.ConvertFromMP4(video_path=self.root, mp4_mode=self.mp4_mode, banner_frame=self.banner_frame)
                        sR.ResizeFile(catDir=self.root,
                                      data=self.file_name,
                                      width_height=self.dimensions,
                                      b_mb=self.is_b_bm_on,
                                      is_sd_on=self.is_sd_on)
                    case "off":
                        if any(item.endswith('.mp4') for item in self.banner_list):
                            self.banner_frame(root=self.root)

                        else:
                            sR.ResizeFile(catDir=self.root,
                                          data=self.file_name,
                                          width_height=self.dimensions,
                                          b_mb=self.is_b_bm_on,
                                          is_sd_on=self.is_sd_on)

