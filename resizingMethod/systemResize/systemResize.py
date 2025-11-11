import os

from PIL import Image

from ..paramCheck import ScalingParametersCheck
from ..messages import FILE_NOT_FOUND_ERROR, GENERIC_ERROR, BANNER_UPLOADED, BANNER_SCALED_SUCCESS, FILE_PROBLEM, SCALING_SUMMARY_SUCCESS


class ResizeFile:
    def __init__(self, catDir: str | None = None, data: int | None = None, width_height: int | None = None, b_mb: str = 'on', is_sd_on: str = 'off'):
        self.catDir: str | None = catDir
        self.data: int | None = data
        self.width_height: int | None = width_height
        self.b_mb: str = b_mb
        self.is_sd_on: str = is_sd_on
        self.resize_all_file()

    def check_width_height(self) -> dict:
        params: ScalingParametersCheck = ScalingParametersCheck(width_height=self.width_height, b_mb=self.b_mb)

        return params.image_params

    def resize_to_png(self, banner_name: str, new_banner_name: str) -> None:
        image_config: dict = self.check_width_height()
        banner_dir = os.path.join(self.catDir, "Banner")
        save_file_path: str = os.path.join(banner_dir, f"{new_banner_name.lower()}{self.data}{image_config['b_mb']}.png")
        try:
            image: Image = Image.open(os.path.join(self.catDir, banner_name))
            resize_image = image.resize((image_config['width'], image_config['height']))
            resize_image.save(save_file_path, "PNG")

        except FileNotFoundError:
            print(FILE_NOT_FOUND_ERROR.format(banner_name))
        except Exception as e:
            print(GENERIC_ERROR.format(e))

    def resize_all_file(self) -> None:
        image_config: dict = self.check_width_height()
        banner_check: list = list(os.listdir(self.catDir))
        counter: int = 0
        banner_num: int = 0
        for banner_name in banner_check:
            if os.path.splitext(banner_name)[1].lower() in [".gif", ".png", ".jpg"]:
                try:
                    new_banner_name: str = os.path.splitext(banner_name)[0]
                    print(BANNER_UPLOADED.format(banner_name))
                    self.resize_to_png(banner_name, new_banner_name)
                    counter += 1
                    print(BANNER_SCALED_SUCCESS.format(new_banner_name.lower(), f"{self.data}{image_config['b_mb']}"))
                except Exception as e:
                    print(FILE_PROBLEM.format(banner_name, e))

        if counter == 0 and self.is_sd_on == 'on':
            pass
        else:
            comm = SCALING_SUMMARY_SUCCESS.format(counter, banner_num)
            print(f'{comm:=^80}')
