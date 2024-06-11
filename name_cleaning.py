import os
f_patch = 'C:\\Users\\User\\Desktop\\Praca\\2024\\testy'
COUNTRY = ['UK', 'PL', 'FR', 'ES', 'HU', 'IT', 'SE', 'PT', 'DK', 'CZ', 'FI', 'NL', 'NO', 'SK', 'CHDE', 'CHFR', 'DEAT', 'CHF']
COUNTRY2 = {'UK':'UK', 'PL':'PL', 'FR':'FR', 'ES':'ES', 'HU':'HU', 'IT':'IT', 'SE':'SE', 'PT':'PT', 'DK':'DK', 'CZ':'CZ',
            'FI':'FI', 'NL':'NL', 'NO':'NO', 'SK':'SK', 'CHDE':'CHDE', 'CHFR':'CHFR', 'DEAT':'DEAT', 'CHF':'CHF'}
class Clean_File_Name:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_path_list = os.listdir(self.file_path)

    def clear_name(self):
        print(self.file_path_list)
        for country in self.file_path_list:
            if 'CHF' in country:
                print('si 1 ')
                os.rename(self.file_path + '\\' + country, self.file_path + '\\' + country[0:3] + '.png')
            elif 'DEAT' in country or 'DACH' in country:
                print('si 2 ')
                os.rename(self.file_path + '\\' + country, self.file_path + '\\' + country[0:4] + '.png')
            else:
                os.rename(self.file_path + '\\' + country, self.file_path + '\\' + country[0:2] + '.png')
                print('si 3 ')








spr=(Clean_File_Name(f_patch))
spr.clear_name()