import photoshop.api as ps
import os


class PhotoshopAPI:
    def __init__(self, catDir=None, data=None, width_height=None, b_mb='on'):
        self.catDir = catDir
        self.data = data
        self.width_height = width_height
        self.b_mb = b_mb
    def psBannerResizer(self):
        app = ps.Application()
        banner_check = list(os.listdir(f"{self.catDir}"))
        if self.b_mb == 'on':
            if self.width_height == 650:
                args = [650, 490]
                banner_format = '_mb'
            else:
                args = [610, 242]
                banner_format = 'b'
        else:
            if self.width_height == 650:
                args = [650, 490]
                banner_format = ''
            else:
                args = [610, 242]
                banner_format = ''
        counter = 0
        for banner_name in banner_check:
            if banner_name.endswith('.jpg') or banner_name.endswith('.png') or banner_name.endswith('.mp4'):
                try:
                    new_banner_name = banner_name.replace(banner_name[banner_name.index('.')::], '')
                    # Load the image file into Photoshop and assign it to the 'a' variable
                    banner_file = app.load(f"{self.catDir}\\{banner_name}")
                    print(f'Banner uploaded: {banner_name}')
                    # Resize and save the image
                    banner_file.resizeImage(width=args[0], height=args[1], resolution=72, automatic=8)
                    png = f"{self.catDir}\\Banner\\{new_banner_name.lower()}{self.data}{banner_format}"
                    options = ps.PNGSaveOptions()
                    banner_file.saveAs(png, options, asCopy=True)
                    banner_file.close()
                    counter +=1
                    print(f" - Banner: {new_banner_name.lower()}{self.data}{banner_format} has been scaled")
                except:
                    print("Check if Adobe Photoshop does not perform an action")
            else:
                continue

        comm = f' {counter} banner has been scaled '
        print(f'{comm:=^80}')
