import os
import shutil

f_patch = 'C:\\Users\\User\\Desktop\\Praca\\2024\\testy'
class Copy_Missing_C:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_path_list = os.listdir(self.file_path)



    def file_copy_dach(self):
        # sprawdza czy jest DACH i kopiuje go na DE AT CHDE
        dach = ['CHDE.png','AT.png', 'DE.png']
        self.file_path_list = [country.lower() for country in self.file_path_list]
        print(self.file_path_list)
        if 'dach.png' in self.file_path_list and 'de.png' not in self.file_path_list and 'at.png' not in self.file_path_list:
            print(self.file_path_list, 'qq')
            for country in dach:
                shutil.copy(self.file_path + '\\DACH.png', self.file_path + '\\' + country)
            os.remove(self.file_path + '\\DACH.png')
        # Banery kiedy mamy inny text na DE AT CHDE -> DEAT lub DE AT oraz CH dla szwajcari
        elif 'ch.png' in self.file_path_list:
            for country in dach:
                if 'deat.png' in self.file_path_list:
                    if country in dach[1::]:
                        shutil.copy(self.file_path + '\\DEAT.png', self.file_path + '\\' + country)

                if country == dach[0]:
                    shutil.copy(self.file_path + '\\CH.png', self.file_path + '\\' + country)

            if os.path.exists(self.file_path + '\\DEAT.png'):
                os.remove(self.file_path + '\\DEAT.png')
            if os.path.exists(self.file_path + '\\CH.png'):
                os.remove(self.file_path + '\\CH.png')

    # CHFR i FR jak takie same to FR jak inne to FR i CHF
    def file_copy_chf(self):
        self.file_path_list = [country.lower() for country in self.file_path_list]
        if 'fr.png' in self.file_path_list and 'chf.png' not in self.file_path_list:
            shutil.copy(self.file_path + '\\FR.png', self.file_path + '\\CHFR.png')
            print('opcja jeden')
        elif 'chf.png' in self.file_path_list:
            shutil.copy(self.file_path + '\\CHF.png', self.file_path + '\\CHFR.png')
            print('opcja 2')

        if os.path.exists(self.file_path + '\\CHF.png'):
            os.remove(self.file_path + '\\CHF.png')







f_cop = Copy_Missing_C(f_patch)
f_cop.file_copy_dach()
f_cop.file_copy_chf()