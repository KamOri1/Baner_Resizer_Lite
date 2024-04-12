import paramiko
import os
from ftplib import FTP

# self.dateforCatalog_.get('0.0', 'end')
def connectToServerSFTP(catDir, hostname_, username_, password_, ftpCatDir):
    cnopts = paramiko.client.SSHClient()
    cnopts.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    cnopts.connect(hostname=hostname_,
                   username=username_,
                   password=password_,
                   )
    with cnopts.open_sftp() as sftp:
        print(f"connected to server: {sftp.getcwd()}")

        sftp.chdir(ftpCatDir)
        print(f"connected to server 2: {sftp.getcwd()}")
        # current_directory = sftp.getcwd()
        # if current_directory == ftpCatDir:
        #     print(f"You are in the {ftpCatDir} directory.")
        #     checkToSend = list(os.listdir(catDir))
        #     for ban in checkToSend:
        #         sftp.put(f"{catDir}\\{ban}", f"{ftpCatDir}//{ban}")
        #         print(f'Baner {ban} został przesłany na server')
        #     print(
        #         "Wszystkie banery zostały przesłane na server #######################################################")
        # else:
        #     print(f"{sftp.getcwd()}") # dodać connection error zamiast tego
        cnopts.close()


def connectToServerFTP(catDir,hostname_, username_, password_, ftpCatDir):
    with FTP(host=hostname_,
             user=username_,
             passwd=password_) as ftp:
        print("connected to ...")
        print(ftp.cwd(ftpCatDir))  # Change to `other_dir/
        current_directory = ftp.pwd()
        if current_directory == '': # lokalizacja katalogu do img
            print(f"You are in the {current_directory} directory.")
            checkToSend = list(os.listdir(catDir))
            for ban in checkToSend:
                with open(f"{catDir}\\{ban}", 'rb') as image_file:
                    ftp.storbinary(f'STOR {ban}', image_file)
                    print(f'Baner {ban} został przesłany na server')
                print(
                    "Wszystkie banery zostały przesłane na server #######################################################")
            ftp.quit()