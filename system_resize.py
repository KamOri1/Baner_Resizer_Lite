from PIL import Image
import os

class ResizeFile:
    def __init__(self, catDir: str | None = None, data: int | None = None, width_height: int | None = None, b_mb: str = 'on', is_sd_on: str = 'off'):
        self.catDir: str | None = catDir
        self.data: int | None = data
        self.width_height: int | None = width_height
        self.b_mb: str = b_mb
        self.is_sd_on: str = is_sd_on
        self.resize_all_file()

    def check_width_height(self) -> dict:

        if self.width_height == 650:
            args = [650, 490]
        else:
            args = [610, 242]

        if self.b_mb == 'on':
            if self.width_height == 650:
                banner_format = '_mb'
            else:
                banner_format = 'b'
        else:
            banner_format = ''

        image_params: dict = {
            'width': args[0],
            'height': args[1],
            'b_mb': banner_format
        }
        return image_params

    def resize_to_png(self, banner_name: str, new_banner_name: str) -> None:
        image_config: dict = self.check_width_height()
        save_file_path: str = f"{self.catDir}\\Banner\\{new_banner_name.lower()}{self.data}{image_config['b_mb']}.png"
        try:
            image: Image = Image.open(f"{self.catDir}\\{banner_name}")
            resize_image = image.resize((image_config['width'], image_config['height']))
            resize_image.save(save_file_path, "PNG")

        except FileNotFoundError:
            print(f"Błąd: Plik {banner_name} nie został znaleziony.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

    def resize_all_file(self) -> None:
        image_config: dict = self.check_width_height()
        banner_check: list = list(os.listdir(f"{self.catDir}"))
        counter: int = 0
        for banner_name in banner_check:
            if banner_name.endswith('.jpg') or banner_name.endswith('.png') or banner_name.endswith('.gif'):
                try:
                    new_banner_name: str = banner_name.replace(banner_name[banner_name.index('.')::], '')
                    print(f'Banner uploaded: {banner_name}')
                    self.resize_to_png(banner_name, new_banner_name)
                    counter += 1
                    print(f" - Banner: {new_banner_name.lower()}{self.data}{image_config['b_mb']} has been scaled")
                except:
                    print("Check if Adobe Photoshop does not perform an action")
            else:
                continue

        if counter == 0 and self.is_sd_on == 'on':
            pass
        else:
            comm = f' {counter} banner has been scaled '
            print(f'{comm:=^80}')






# # Przykładowe użycie
# catDir = 'C:\\Users\\User\\Desktop\\Baner_test\\Test'
# data = 20222201
# width_height = 610
# graf = ResizeFile(catDir=catDir, data=data, width_height=width_height)