from webptools import grant_permission
from webptools import cwebp
import os


def convertToWebp(catdir):

    files = os.listdir(f'{catdir}\\Banner\\')
    grant_permission()
    for file in files:
        print(cwebp(input_image=f"{catdir}\\Banner\\{file}", output_image=f"{catdir}\\Banner\\{file.replace('.png', '.webp')}",
            option="-q 80", logging="-v"))
        print(f'file: {file}')
        print(f'file web: {file.replace('.png', '.webp')}')



