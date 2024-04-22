import paramiko
import os
from ftplib import FTP
import serverPass as sP


class ServerConnectionAction:
    def connectionCheck(self, ftpOrSftp, hostnameData, usernameData, passwordData, ftpCatDir):
        self.ftpOrSftp = ftpOrSftp
        self.hostnameData = hostnameData
        self.usernameData = usernameData
        self.passwordData = passwordData
        self.ftpCatDir = ftpCatDir
        if self.ftpOrSftp is not None and self.hostnameData is not None and self.usernameData is not None \
            and self.passwordData is not None and self.ftpCatDir is not None:
            try:
                if self.ftpOrSftp == 'sftp':
                    self.cnopts = paramiko.client.SSHClient()
                    self.cnopts.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
                    self.cnopts.connect(hostname=self.hostnameData,
                                       username=self.usernameData,
                                       password=self.passwordData)
                    with self.cnopts.open_sftp() as sftp:
                        sftp.chdir(ftpCatDir)
                        print(f"Connected to the server {sP.passToSFTP['serverName']}: {sftp.getcwd()}")
                        self.cnopts.close()
                    return True

                elif self.ftpOrSftp == 'ftp':
                    with FTP(host=self.hostnameData,
                             user=self.usernameData,
                             passwd=self.passwordData) as ftp:
                        self.ftp = ftp
                        ftp.cwd(ftpCatDir) # Change to `other_dir/
                        print(f"Connected to the server {sP.passToFTP['serverName']}: {ftp.pwd()}")
                        self.ftp.quit()
                    return True
            except:
                print('Cannot connect to the server')
                return False

    def disconnection(self):
        if self.ftpOrSftp == 'sftp':
            self.cnopts.close()
        elif self.ftpOrSftp == 'ftp':
            self.ftp.quit()

    def connectioFtpOrSftp(self, ftpOrsftp, catDir, hostname_, username_, password_, ftpCatDir):
        if ftpOrsftp == 'ftp':
            self.connectToServerFTP(catDir, hostname_, username_, password_, ftpCatDir)
        elif ftpOrsftp == 'sftp':
            self.connectToServerSFTP(catDir, hostname_, username_, password_, ftpCatDir)

    def connectToServerSFTP(self, catDir, hostname_, username_, password_, ftpCatDir):
        cnopts = paramiko.client.SSHClient()
        cnopts.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        cnopts.connect(hostname=hostname_,
                       username=username_,
                       password=password_, )
        with cnopts.open_sftp() as sftp:
            sftp.chdir(ftpCatDir)
            print(f"Connected to the server {sP.passToSFTP['serverName']}: {sftp.getcwd()}")
            current_directory = sftp.getcwd()
            if current_directory == ftpCatDir:
                checkToSend = list(os.listdir(catDir))
                for ban in checkToSend:
                    sftp.put(f"{catDir}\\{ban}", f"{ftpCatDir}//{ban}")
                    print(f'The banner {ban} has been uploaded to the server')
                print(
                    "All banners were uploaded to the server #######################################################")
            else:
                print(f"{sftp.getcwd()}")
            cnopts.close()

    def connectToServerFTP(self, catDir, hostname_=sP.passToFTP['hostname'], username_=sP.passToFTP['username'],
                           password_=sP.passToFTP['password'], ftpCatDir=sP.passToFTP['ftpCatDir']):
        with FTP(host=hostname_,
                 user=username_,
                 passwd=password_) as ftp:
            ftp.cwd(ftpCatDir)  # Change to `other_dir/
            print(f"Connected to the server {sP.passToFTP['serverName']}: {ftp.pwd()}")
            current_directory = ftp.pwd()
            if current_directory == ftpCatDir:
                checkToSend = list(os.listdir(catDir))
                for ban in checkToSend:
                    with open(f"{catDir}\\{ban}", 'rb') as image_file:
                        ftp.storbinary(f'STOR {ban}', image_file)
                        print(f'The banner {ban} has been uploaded to the server')
                    print(
                        "All banners were uploaded to the server #######################################################")
            ftp.quit()
