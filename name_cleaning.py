import os

class Clean_File_Name:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_path_list = os.listdir(self.file_path)

    def clear_name(self):

        file_endswith = ['.jpg', '.png', '.mp4']

        for country in self.file_path_list:
            plik_jpg_istnieje = any(
                plik.endswith(rozszerzenie) for plik in self.file_path_list for rozszerzenie in ['.jpg', '.png', '.mp4'])
            if plik_jpg_istnieje == True and country[-4::] in file_endswith:
                if 'CHF' in country:

                    os.rename(self.file_path + '\\' + country, self.file_path + '\\' + country[0:3] + country[-4::])
                elif 'DEAT' in country or 'DACH' in country:

                    os.rename(self.file_path + '\\' + country, self.file_path + '\\' + country[0:4] + country[-4::])
                else:
                    os.rename(self.file_path + '\\' + country, self.file_path + '\\' + country[0:2] + country[-4::])


            else:
                continue






