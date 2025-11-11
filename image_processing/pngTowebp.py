import os
from PIL import Image

class PngToWebp:
    def __init__(self, file_path):
        self.file_path = file_path

    def convert_to_web_p(self):
        files = os.listdir(os.path.join(self.file_path, 'Banner'))
        for file in files:
            Image.open(os.path.join(self.file_path, 'Banner', file)).save(os.path.join(self.file_path, 'Banner', file.replace('.png', '.webp')),
                'webp', lossless=True)
            print(f'File {file} has been converted to .webp')



