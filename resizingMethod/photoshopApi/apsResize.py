import os

import photoshop.api as ps

from ..paramCheck import ScalingParametersCheck
from ..messages import BANNER_UPLOADED, BANNER_SCALED_SUCCESS, SCALING_SUMMARY_SUCCESS, PHOTOSHOP_ACTION


class PhotoshopAPI:
    def __init__(self, catDir=None, data=None, width_height=None, b_mb='on', is_sd_on='off') -> None:
        self.catDir = catDir
        self.data = data
        self.width_height = width_height
        self.b_mb = b_mb
        self.is_sd_on = is_sd_on

    def check_width_height(self) -> dict:
        params: ScalingParametersCheck = ScalingParametersCheck(width_height=self.width_height, b_mb=self.b_mb)

        return params.image_params

    def psBannerResizer(self):
        app = ps.Application()
        banner_check = list(os.listdir(f"{self.catDir}"))
        image_config: dict = self.check_width_height()
        counter = 0
        banner_num: int = 0
        for banner_name in banner_check:
            if os.path.splitext(banner_name)[1].lower() in [".gif", ".png", ".jpg"]:
                try:
                    new_banner_name: str = os.path.splitext(banner_name)[0]
                    banner_file = app.load(os.path.join(self.catDir, banner_name))
                    print(BANNER_UPLOADED.format(banner_name))
                    banner_file.resizeImage(width=image_config['width'], height=image_config['height'], resolution=72, automatic=8)
                    png = os.path.join(self.catDir, 'Banner', f'{new_banner_name.lower()}{self.data}{image_config['b_mb']}')

                    options = ps.PNGSaveOptions()
                    banner_file.saveAs(png, options, asCopy=True)
                    banner_file.close()
                    counter += 1
                    print(BANNER_SCALED_SUCCESS.format(new_banner_name.lower(), f"{self.data}{image_config['b_mb']}"))

                except Exception as e:
                    print(PHOTOSHOP_ACTION.format(e))

        if counter == 0 and self.is_sd_on == 'on':
            pass
        else:
            comm = SCALING_SUMMARY_SUCCESS.format(counter, banner_num)
            print(f'{comm:=^80}')
