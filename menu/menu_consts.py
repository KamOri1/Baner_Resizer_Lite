from dataclasses import dataclass


@dataclass
class MenuConsts:
    CONNECTION_LABELS = [{"Name": "Server:", "x": 60, "y": 90},
                         {"Name": "User Name:", "x": 60, "y": 130},
                         {"Name": "Password:", "x": 60, "y": 170},
                         {"Name": "Path:", "x": 60, "y": 210}]

    CONNECTION_BUTTON = [{'Name': "Connect", 'Text': "Connect", "fg_color": '#0033FF', 'hover_color': '#0000FF',
                          'command': 'self.connectionTest', 'x': 160, 'y': 250},
                         {'Name': "Close", 'Text': "Close", "fg_color": '#e33118', 'hover_color': '#d11507',
                          'command': "ServerLogView.close_frame", 'x': 280, 'y': 250},
                         {'Name': "ShowPassword", 'Text': chr(0x1F441), "fg_color": '#333333', 'hover_color': '#d11507',
                          'command': "self.showPassword", 'x': 335, 'y': 170}]

    CONNECTION_ENTRY = [{'Name': "serverDate:", 'x': 220, 'y': 90},
                        {'Name': "userNameDate:", 'x': 220, 'y': 130},
                        {'Name': "passwordDate:", 'x': 220, 'y': 170}]

    CONNECTION_RADIO_BUTTON = [{'Name': "FTP", "Text": "FTP", "Value": "ftp", "Variable": "var", "Command": "clearData", 'x': 70, 'y': 40},
                               {'Name': "SFTP", "Text": "SFTP", "Value": "sftp", "Variable": "var","Command": "clearData", 'x': 130, 'y': 40}]

    CONNECTION_TEXT_BOX = [{'Name': "pathDate:", 'x': 220, 'y': 210}]

    CONNECTION_SWITCH = [
        {"Name": "defaultDate:", "Text": "Default data", "State": "disabled", "Command": "addDefaulParam",
         "Variable": "switch_var_0", "x": 210, "y": 40}]

    MAIN_MANU_BUTTON = [{'Name': "SelectFolder", 'Text': "Select folder", "fg_color": 'green', 'hover_color': '#34661e',
                         'command': 'get_banner_dir', 'x': 60, 'y': 85},
                        {'Name': "Resize", 'Text': "Resize", "fg_color": 'green', 'hover_color': '#34661e',
                         'command': 'get_banner_dir', 'x': 60, 'y': 125},
                        {'Name': "Resend", 'Text': "Resend", "fg_color": '#0033FF', 'hover_color': '#0000FF',
                         'command': 'get_banner_dir', 'x': 60, 'y': 165},
                        {'Name': "Connection", 'Text': "Connection", "fg_color": '#0033FF', 'hover_color': '#0000FF',
                         'command': 'get_banner_dir', 'x': 60, 'y': 205},
                        {'Name': "Exit", 'Text': "Exit", "fg_color": '#e33118', 'hover_color': '#d11507',
                         'command': 'get_banner_dir', 'x': 60, 'y': 295}]
    MAIN_MENU_SWITCH = [
        {"Name": "BannerType", "Text": "b_mb", "State": "normal", "Variable": "switch_b_mb_var", "Command": "resend_block", "x": 70, "y": 120},
        {"Name": "Mp4:", "Text": "Mp4", "State": "normal", "Variable": "switch_mp4_var", "Command": "resend_block","x": 70, "y": 150},
        {"Name": "Sunday", "Text": "Sun", "State": "normal", "Variable": "switch_sunday_var", "Command": "resend_block","x": 70, "y": 180},
        {"Name": "WebP", "Text": ".webp", "State": "normal", "Variable": "switch_webp_var", "Command": "resend_block", "x": 70, "y": 210},
        {"Name": "PhotoShop:", "Text": "PS", "State": "normal", "Variable": "switch_photoshop_var", "Command": "resend_block", "x": 70, "y": 240},
    ]

    MAIN_MENU_RADIO_BUTTON = [
        {'Name': "610x242", "Text": "610x242", "Value": "610", "Variable": "format_type_var", "Command": "resend_block", 'x': 70, 'y': 80},
        {'Name': "650x490", "Text": "650x490", "Value": "650", "Variable": "format_type_var", "Command": "resend_block", 'x': 160, 'y': 80}]

    MAIN_MENU_LABELS = [{"Name": "Campagin date YYYYMMDD:", "Text": "Campagin date YYYYMMDD", "x": 115, "y": 40},
                        {"Name": "", "Text": "Campagin date YYYYMMDD", "x": 275, "y": 120}]

    MAIN_MENU_TEXT_BOX = [{'Name': "FolderDir:", 'x': 320, 'y': 40}]

    SLIDER_BUTTON = [{'Name': "Accept", 'Text': "Accept", "fg_color": 'green', 'hover_color': '#34661e',
                          'command': 'self.connectionTest', 'x': 200, 'y': 100},
                     {'Name': "Close", 'Text': "Close", "fg_color": '#e33118', 'hover_color': '#d11507',
                      'command': 'self.connectionTest', 'x': 200, 'y': 100}]

    SLIDER_BUTTON_ARROW = [{'Name': "Left Arrow", 'Text': "◀", "fg_color": '#0033FF', 'hover_color': '#0000FF',
                      'command': 'self.connectionTest', 'x': 200, 'y': 100},
                     {'Name': "Right Arrow", 'Text': "▶", "fg_color": '#0033FF', 'hover_color': '#0000FF',
                      'command': 'self.connectionTest', 'x': 200, 'y': 100}]

    SLIDER_LABEL = [{'Name': "||", 'Text': "||", "fg_color": '#0033FF', 'x': 200, 'y': 100}]



