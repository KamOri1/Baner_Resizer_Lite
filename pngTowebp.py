import os
from PIL import Image



def convertToWebp2(catdir):
    files = os.listdir(f'{catdir}\\Banner\\')
    for file in files:
        Image.open(f"{catdir}\\Banner\\{file}").save(f"{catdir}\\Banner\\{file.replace('.png', '.webp')}",
            'webp', lossless=True)
        print(f'Plik {file} został skonwertowany do .webp')
