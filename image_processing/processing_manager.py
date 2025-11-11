import os

from . import clean_name as cN
from . import pngTowebp as pWp
from . import file_copy as fC
from resizingMethod import resizing_manager as rM
from resizingMethod import paramCheck as pC
from serverData import serverConnection as sC
from serverData import serverDefaultData as serverPass
from serverData import server_custom_data as sCd

class ProcessingImgManager:
    def __init__(self, file_path, **kwargs):
        self.file_path = file_path
        self.kwargs = kwargs
        self.name_space_cleaned: bool = False
        self.file_scaled: bool = False
        self.missed_file_added: bool = False
        self.comment_finalized: bool = False
        self.converted_to_webp: bool = False
        self.file_sent_to_server: bool = False

    def prepare_image(self, scale_file=True):
        for root, dir, files in os.walk(self.file_path):
            if self.kwargs['is_sd_on'] == 'on':
                if os.path.basename(root) != 'Banner':
                    file_name = os.path.basename(root)
            else:
                file_name = self.kwargs.get('file_name')

            if files:
                self.clean_name_space(root, files, self.kwargs['is_sd_on'])

                if scale_file:

                    self.scale_file(root, file_name)

                self.add_missed_file(root, file_name)
                self.convert_to_web(root)
                self.send_file_to_server(catDir=fr'{root}/Banner')
            else:
               pass

    def _execute_operation(self, operation_func, success_flag_attr, error_message):
        try:
            operation_func()
            setattr(self, success_flag_attr, True)
        except Exception as error:
            print(f'{error_message} failed')
            print(error)

    def clean_name_space(self, root, files, sunday):
        def _clean_name_action():
            new_name = cN.NameCleaner(self.file_path)
            new_name.clean_name_space(root, files, sunday)

        self._execute_operation(
            operation_func=_clean_name_action,
            success_flag_attr='name_space_cleaned',
            error_message='Name cleaning'
        )

    def scale_file(self, root, banner_name):
        def _scale_file_action():
            file_name = banner_name
            dimensions = self.kwargs.get('dimensions')
            is_b_bm_on = self.kwargs.get('is_b_bm_on')
            is_sd_on = self.kwargs.get('is_sd_on')
            video_path = self.kwargs.get('video_path')
            mp4_mode = self.kwargs.get('mp4_mode')
            banner_frame = self.kwargs.get('banner_frame')
            photoshop_or_not = self.kwargs.get('photoshop_or_not')
            scaled = rM.Manager(root, file_name, dimensions, is_b_bm_on, is_sd_on, photoshop_or_not, video_path, mp4_mode, banner_frame)
            scaled.scaled_method()

        self._execute_operation(
            operation_func=_scale_file_action,
            success_flag_attr='file_scaled',
            error_message='Scaled'
        )

    def add_missed_file(self, file_path, data):
        dimension = self.kwargs.get('dimensions')
        file_extension = self.kwargs.get('is_b_bm_on')
        check_banner_ext = pC.ScalingParametersCheck(width_height=dimension, b_mb=file_extension)
        banner_ext = check_banner_ext.image_params

        def _add_missed_file_action():
            add_missing_banner = fC.CopyMissingBanner(file_path, data,  banner_ext['b_mb'])
            add_missing_banner.start_copy_processing()

        self._execute_operation(
            operation_func=_add_missed_file_action,
            success_flag_attr='missed_file_added',
            error_message='Adding missed file'
        )

    def finalize_comment(self):
        def _finalize_comment_action():
            cN.NameCleaner.clear_name(self.file_path)

        self._execute_operation(
            operation_func=_finalize_comment_action,
            success_flag_attr='comment_finalized',
            error_message='Finalizing comment'
        )

    def convert_to_web(self, file_path):
        web_p_state: str = self.kwargs.get('web_p')

        def _convert_to_web_action():
            convert = pWp.PngToWebp(file_path)
            convert.convert_to_web_p()

        if web_p_state == 'on':
            self._execute_operation(
                operation_func=_convert_to_web_action,
                success_flag_attr='converted_to_webp',
                error_message='WebP conversion'
            )

    def send_file_to_server(self, catDir):
        if sCd.VERIFIED_SERVER_DETAILS:
            serverData = sCd.VERIFIED_SERVER_DETAILS
        else:
            serverData = serverPass.passToFTP
            serverData['ftpOrSftp'] = 'ftp'

        def _send_file_action():
           connection = sC.ServerConnectionAction(server_details=serverData, catDir=catDir)
           connection.connection_ftp_or_sftp()

        self._execute_operation(
            operation_func=_send_file_action,
            success_flag_attr='file_sent_to_server',
            error_message='Server sending file'
        )