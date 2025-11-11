import os
import cv2


class ConvertFromMP4:
    def __init__(self, video_path: str, **kwargs):
        self.mp4_default = False
        self.video_path: str = video_path
        self.mp4_mode = kwargs.get('mp4_mode')
        self.banner_frame = kwargs.get('banner_frame')
        self.selected_frame = kwargs.get('selected_frame') or 0
        self.first_frame_only = True
        self.keyframes_data = []

        self.method_selection()

    def save_first_frame_as_png(self, new_banner_name, original_name, selected_frame=0) -> None:
        video = cv2.VideoCapture(os.path.join(self.video_path, original_name))

        if not video.isOpened():
            print(f"Cannot open ...{original_name}")

        elif self.mp4_mode == 'off':
            video.set(cv2.CAP_PROP_POS_FRAMES, selected_frame)

        ret, frame = video.read()
        if ret:
            cv2.imwrite(os.path.join(self.video_path, f'{new_banner_name}.png'), frame)

        else:
            print("It was not possible to read the first frame.")

        video.release()

    def save_all_first_frame_as_png(self, selected_frame=0) -> None:
        banner_check: list = list(os.listdir(f"{self.video_path}"))
        counter: int = 0
        banner_num: int = 0
        for banner_name in banner_check:
            if banner_name.endswith('.mp4'):
                try:
                    new_banner_name: str = banner_name.replace(banner_name[banner_name.index('.')::], '')
                    self.save_first_frame_as_png(new_banner_name, banner_name,  selected_frame)
                    banner_num += 1
                    counter += 1
                    print(f" - Banner: {new_banner_name.lower()} has been extracted from MP4")
                except:
                    print(f"There was a problem with the file {banner_name}")
            else:
                continue

        if banner_num > 0:
            comm = f' {counter}/{banner_num} banners converted to png '
            print(f'{comm:=^80}')

    def extract_one_frame_per_second(self) -> list:
        banner_check: list = list(os.listdir(self.video_path))
        banner_filter = [banner for banner in banner_check if banner.endswith('.mp4')]
        video_file = os.path.join(self.video_path, banner_filter[0])
        filename = video_file
        vidcap = cv2.VideoCapture(filename)
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        success, image = vidcap.read()
        frame_count = 0

        while success:
            if frame_count % fps == 0:
                rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                self.keyframes_data.append((frame_count, rgb_image))

            success, image = vidcap.read()
            frame_count += 1

        vidcap.release()
        print(f"Loading complete.  {len(self.keyframes_data)} frames found.")

        return self.keyframes_data

    def method_selection(self) -> None:
        match self.mp4_mode:
            case 'on':
                self.save_all_first_frame_as_png()
            case 'off':
                pass

