import os

from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.sftp_client import SFTPClient
from ftplib import FTP

from .messages import CONNECTION_SUCCESS, CONNECTION_ERROR,UPLOAD_SUCCESS, ALL_BANNERS_UPLOADED


class ServerConnectionAction:
    def __init__(self, server_details: dict, catDir: str | None = None ) -> None:
        self.ftpOrSftp: str = server_details['ftpOrSftp']
        self.hostnameData: str = server_details['hostname']
        self.usernameData: str = server_details['username']
        self.passwordData: str = server_details['password']
        self.ftpCatDir: str = server_details['ftpCatDir']
        self.catDir: str = catDir


    def sftp_connection(self, checkStatus: bool = False) -> bool:
        self.cnopts: SSHClient = SSHClient()

        with self.cnopts:
            self.cnopts.set_missing_host_key_policy(AutoAddPolicy())
            self.cnopts.connect(hostname=self.hostnameData,
                                username=self.usernameData,
                                password=self.passwordData)

            with self.cnopts.open_sftp() as sftp:
                sftp.chdir(self.ftpCatDir)
                print(CONNECTION_SUCCESS.format(sftp.getcwd()))

                if checkStatus:
                    self.send_png_to_the_server(current_directory=sftp.getcwd(), serverCatDir=self.ftpCatDir,
                                                catDir=self.catDir, ftpOrSftp=sftp)

            return True

    def ftp_connection(self, checkStatus: bool = False) -> bool:
        with FTP(host=self.hostnameData,
                 user=self.usernameData,
                 passwd=self.passwordData) as ftp:

            ftp.cwd(self.ftpCatDir)
            print(CONNECTION_SUCCESS.format(ftp.pwd()))
            if checkStatus:
                self.send_png_to_the_server(current_directory=ftp.pwd(), serverCatDir=self.ftpCatDir, catDir=self.catDir, ftpOrSftp=ftp)

        return True

    def send_png_to_the_server(self, current_directory: str, serverCatDir: str, catDir: str, ftpOrSftp: FTP | SFTPClient):
        if current_directory == serverCatDir:

            checkToSend = list(os.listdir(catDir))

            for banner in checkToSend:

                with open(os.path.join(catDir, banner), 'rb') as image_file:
                    if isinstance(ftpOrSftp, FTP):
                        ftpOrSftp.storbinary(f'STOR {banner}', image_file),
                    else:
                        ftpOrSftp.put(os.path.join(catDir, banner), os.path.join(serverCatDir, banner))
                print(UPLOAD_SUCCESS.format(banner))
            comm = ALL_BANNERS_UPLOADED
            print(f'{comm:=^80}')

    def connection_check(self) -> bool | None:
        if all([self.ftpOrSftp, self.hostnameData, self.usernameData, self.passwordData, self.ftpCatDir]):
            try:
                match self.ftpOrSftp:
                    case 'sftp':
                        connection_test = self.sftp_connection()
                        return connection_test

                    case 'ftp':
                        connection_test = self.ftp_connection()
                        return connection_test

            except Exception as exception:
                print(f'{CONNECTION_ERROR:=^80} \n {exception}')
                return False

    def connection_ftp_or_sftp(self) -> None:
        match self.ftpOrSftp:
            case 'ftp':
                self.ftp_connection(checkStatus=True),
            case 'sftp':
                self.sftp_connection(checkStatus=True)


