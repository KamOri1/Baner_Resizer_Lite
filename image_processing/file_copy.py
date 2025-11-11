import os
import shutil


class CopyMissingBanner:
    def __init__(self, file_path, data, ext):
        self.data = data
        self.ext = ext
        self.file_path: str = os.path.join(file_path, 'Banner')
        self.file_path_list = os.listdir(self.file_path)

    def copy_file(self, data, ext, file_prefix_1: str, file_prefix_2: str, new_file_prefix: str) -> None:
        """
        Creates a new file based on the specified prefixes and extension.

        Args:
            data (str): Name of the file to be created, e.g., “20230901”.
            ext (str): File extension, e.g., “b” or “_mb”.
            file_prefix_1 (str): File prefix checked to see if it is in the file list.
            file_prefix_2 (str): File prefix checked to see if it is not in the file list.
            new_file_prefix (str): File prefix to be created, e.g., “befr”.
        """
        self.file_path_list = [country.lower() for country in self.file_path_list]
        if f'{file_prefix_1}{data}{ext}.png' in self.file_path_list and f'{file_prefix_2}{data}{ext}.png' not in self.file_path_list:
            shutil.copy(self.create_path(f'{file_prefix_1}{data}{ext}'), self.create_path(f'{new_file_prefix}{data}{ext}'))
            print(f' - added missing {new_file_prefix}{data}{ext}.png file')

        elif f'{file_prefix_2}{data}{ext}.png' in self.file_path_list:
            shutil.copy(self.create_path(f'{file_prefix_2}{data}{ext}'), self.create_path(f'{new_file_prefix}{data}{ext}'))

        if os.path.exists(self.create_path(f'{file_prefix_2}{data}{ext}')):
            os.remove(self.create_path(f'{file_prefix_2}{data}{ext}'))

    def file_copy_dach(self,data, ext):
        """
        Checks
        if: there is a DACH and copies it to DE AT CHDE

        elif: Banners when we have different text on DE AT CHDE -> DEAT or DE AT and CH for Switzerland

        """
        dach = [f'chde{data}{ext}.png',f'at{data}{ext}.png', f'de{data}{ext}.png',]
        self.file_path_list = [country.lower() for country in self.file_path_list]

        if f'dach{data}{ext}.png' in self.file_path_list and f'de{data}{ext}.png' not in self.file_path_list and f'at{data}{ext}.png' not in self.file_path_list:
            for country in dach:
                shutil.copy(self.create_path(f'dach{data}{ext}'), os.path.join(self.file_path ,country))
                print(f' - added missing {country} file')

            os.remove(self.create_path(f'dach{data}{ext}'))

        elif f'ch{data}{ext}.png' in self.file_path_list:
            for country in dach:
                if f'deat{data}{ext}.png' in self.file_path_list:
                    if country in dach[1::]:
                        shutil.copy(self.create_path(f'deat{data}{ext}'), os.path.join(self.file_path ,country))
                        print(f' - added missing {country} file')
                if country == dach[0]:
                    shutil.copy(self.create_path(f'ch{data}{ext}'), os.path.join(self.file_path ,country))
                    print(f' - added missing {country} file')

            if os.path.exists(self.create_path(f'deat{data}{ext}')):
                os.remove(self.create_path(f'deat{data}{ext}'))
            if os.path.exists(self.create_path(f'ch{data}{ext}')):
                os.remove(self.create_path(f'ch{data}{ext}'))

    def create_path(self, name: str):
        return os.path.join(self.file_path, f'{name}.png')

    def start_copy_processing(self):
        """
            method initiating file copying
        """
        self.file_copy_dach(self.data, self.ext)

        file_to_copy: list[dict] =[
            {'file_prefix_1':'fr', 'file_prefix_2':'bef', 'new_file_prefix':'befr'},
            {'file_prefix_1':'nl', 'file_prefix_2':'ben', 'new_file_prefix':'benl'},
            {'file_prefix_1':'fr', 'file_prefix_2':'chf', 'new_file_prefix':'chfr'}
        ]
        for file_params in file_to_copy:
            self.copy_file(data=self.data,
                           ext=self.ext,
                           **file_params)


