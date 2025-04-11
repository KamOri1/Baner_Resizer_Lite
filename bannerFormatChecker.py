import os


class CheckBannerFormat:
    def __init__(self, banner_dir):
        self.banner_dir: list = banner_dir
        self.banner_list: list = list(os.listdir(f"{self.banner_dir}"))

    def banner_format(self):
        """Function check if mp4 banner is in the catalog return True else return False"""

        if ".mp4" in self.banner_list:
            return True
        else:
            return False

