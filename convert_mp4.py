import os
import cv2


class ConvertFromMP4:
    def __init__(self, video_path: str):
        self.video_path: str = video_path
        self.save_all_first_frame_as_png()
    def save_first_frame_as_png(self, new_banner_name, orginal_name) -> None:
        video = cv2.VideoCapture(f"{self.video_path}\\{orginal_name}")

        if not video.isOpened():
            print(f"Cannot open ...{orginal_name}")
            return

        ret, frame = video.read()
        if ret:
            cv2.imwrite(f"{self.video_path}\\{new_banner_name}.png", frame)
        else:
            print("It was not possible to read the first frame.")

        video.release()

    def save_all_first_frame_as_png(self):

        banner_check: list = list(os.listdir(f"{self.video_path}"))
        counter: int = 0
        for banner_name in banner_check:
            if banner_name.endswith('.mp4'):
                try:
                    new_banner_name: str = banner_name.replace(banner_name[banner_name.index('.')::], '')
                    self.save_first_frame_as_png(new_banner_name, banner_name)
                    counter += 1
                    print(f" - Banner: {new_banner_name.lower()} has been extracted")
                except:
                    print("Check if Adobe Photoshop does not perform an action")
            else:
                continue

        comm = f' {counter} banner has been scaled '
        print(f'{comm:=^80}')


# Przykład użycia
# video_path = "C:\\Users\\User\\Desktop\\Baner_test\\test1"  # Zmienna ścieżki do pliku wideo
# ConvertFromMP4(video_path)
