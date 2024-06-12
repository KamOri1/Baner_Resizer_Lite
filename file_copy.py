import os
import shutil
f_path = 'C:\\Users\\User\\Desktop\\Praca\\2024\\testy\\2024.05.16 - Viennese Braid'
#f_patch = 'C:\\Users\\User\\Desktop\\Praca\\2024\\testy'

class Copy_Missing_C:
    def __init__(self, file_path):
        self.file_path = file_path + '\\Banner'
        self.file_path_list = os.listdir(self.file_path)



    def file_copy_dach(self):
        # sprawdza czy jest DACH i kopiuje go na DE AT CHDE
        dach = ['CHDE.png','AT.png', 'DE.png',]
        self.file_path_list = [country.lower() for country in self.file_path_list]

        if 'dach.png' in self.file_path_list and 'de.png' not in self.file_path_list and 'at.png' not in self.file_path_list:

            for country in dach:
                shutil.copy(self.file_path + '\\DACH.png', self.file_path + '\\' + country)
            os.remove(self.file_path + '\\DACH.png')
        # Banery kiedy mamy inny text na DE AT CHDE -> DEAT lub DE AT oraz CH dla szwajcari
        elif 'ch.png' in self.file_path_list:
            for country in dach:
                if 'deat.png' in self.file_path_list:
                    if country in dach[1::]:
                        shutil.copy(self.file_path + f'\\DEAT.png', self.file_path + '\\' + country)


                if country == dach[0]:
                    shutil.copy(self.file_path + f'\\CH.png', self.file_path + '\\' + country)

            if os.path.exists(self.file_path + f'\\DEAT.png'):
                os.remove(self.file_path + f'\\DEAT.png')
            if os.path.exists(self.file_path + '\\CH.png'):
                os.remove(self.file_path + '\\CH.png')

    # CHFR i FR jak takie same to FR jak inne to FR i CHF
    def file_copy_chf(self):
        self.file_path_list = [country.lower() for country in self.file_path_list]



        if 'fr.png' in self.file_path_list and 'chf.png' not in self.file_path_list:
            shutil.copy(self.file_path + f'\\FR.png', self.file_path + '\\CHFR.png')

        elif 'chf.png' in self.file_path_list:
            shutil.copy(self.file_path + '\\CHF.png', self.file_path + '\\CHFR.png')


        if os.path.exists(self.file_path + '\\CHF.png'):
            os.remove(self.file_path + '\\CHF.png')


    def file_copy_chf_2(self, data, ext):
        self.file_path_list = [country.lower() for country in self.file_path_list]

        if f'fr{data}{ext}.png' in self.file_path_list and f'chf{data}{ext}.png' not in self.file_path_list:
            shutil.copy(self.file_path + f'\\fr{data}{ext}.png', self.file_path + f'\\chfr{data}{ext}.png')
            print(f' - added missing chfr{data}{ext}.png file')

        elif f'chf{data}{ext}.png' in self.file_path_list:
            shutil.copy(self.file_path + f'\\chf{data}{ext}.png', self.file_path + f'\\chfr{data}{ext}.png')


        if os.path.exists(self.file_path + f'\\chf{data}{ext}.png'):
            os.remove(self.file_path + f'\\chf{data}{ext}.png')

    def file_copy_dach_2(self,data, ext):


        # sprawdza czy jest DACH i kopiuje go na DE AT CHDE
        dach = [f'chde{data}{ext}.png',f'at{data}{ext}.png', f'de{data}{ext}.png',]
        self.file_path_list = [country.lower() for country in self.file_path_list]

        if f'dach{data}{ext}.png' in self.file_path_list and f'de{data}{ext}.png' not in self.file_path_list and f'at{data}{ext}.png' not in self.file_path_list:

            for country in dach:
                shutil.copy(self.file_path + f'\\dach{data}{ext}.png', self.file_path + '\\' + country)
                print(f' - added missing {country} file')
            os.remove(self.file_path + f'\\dach{data}{ext}.png')
        # Banery kiedy mamy inny text na DE AT CHDE -> DEAT lub DE AT oraz CH dla szwajcari
        elif f'ch{data}{ext}.png' in self.file_path_list:
            for country in dach:
                if f'deat{data}{ext}.png' in self.file_path_list:
                    if country in dach[1::]:
                        shutil.copy(self.file_path + f'\\deat{data}{ext}.png', self.file_path + '\\' + country)
                        print(f' - added missing {country} file')


                if country == dach[0]:
                    shutil.copy(self.file_path + f'\\ch{data}{ext}.png', self.file_path + '\\' + country)
                    print(f' - added missing {country} file')
            if os.path.exists(self.file_path + f'\\deat{data}{ext}.png'):
                os.remove(self.file_path + f'\\deat{data}{ext}.png')
            if os.path.exists(self.file_path + f'\\ch{data}{ext}.png'):
                os.remove(self.file_path + f'\\ch{data}{ext}.png')

# pp = 'C:\\Users\\User\\Desktop\\Praca\\2024\\testy\\2024.05.16 - Viennese Braid'
# ss = Copy_Missing_C(pp).file_copy_dach_2('0101', '_mb')