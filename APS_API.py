import photoshop.api as ps
import os


def ends_with_del(banner_name):
    if banner_name.endswith('.jpg'):
        new_banner_name = banner_name.replace('.jpg', '')
    elif banner_name.endswith('.png'):
        new_banner_name = banner_name.replace('.png', '')
    elif banner_name.endswith('.mp4'):
        new_banner_name = banner_name.replace('.mp4', '')
    return new_banner_name
def psBannerResizer(catDir,data, width_):
    app = ps.Application()
    banner_check = list(os.listdir(f"{catDir}"))
    if width_ == 650:
        args = [650, 490]
    else:
        args = [610, 242]
    for banner_name in banner_check:
        print(banner_name)

        # Load the image file into Photoshop and assign it to the 'a' variable
        banner_file = app.load(f"{catDir}\\{banner_name}")
        print('załadowano kraj')
        # Resize and save the image
        banner_file.resizeImage(width=args[0], height=args[1], resolution=72, automatic=8)
        png = f"{catDir}\\{ends_with_del(banner_name).lower()}{data}b"
        options = ps.PNGSaveOptions()
        banner_file.saveAs(png, options, asCopy=True)
        banner_file.close()




def closePhotoshop(closePS):
    if closePS.lower() == "close_ps":
        # zamyka program photoshop
        ps.Application().quit()
        print('zakończono')


