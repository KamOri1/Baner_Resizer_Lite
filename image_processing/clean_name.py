import os


class NameCleaner:
    FILE_EXTENSIONS = ('.jpg', '.png', '.mp4', '.gif')

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_path_list = os.listdir(file_path)

    def _rename_file(self, folder, filename):
        """Changing file names according to rules."""
        name, ext = os.path.splitext(filename)
        if ext.lower() not in self.FILE_EXTENSIONS:
            return

        if 'CHF' in name:
            new_name = name[:3] + ext
        elif any(x in name for x in ('DEAT', 'DACH')):
            new_name = name[:4] + ext
        elif any(x in name for x in ('BEN', 'BEF')):
            new_name = name[:3] + ext
        else:
            new_name = name[:2] + ext

        old_path = os.path.join(self.file_path, folder, filename)
        new_path = os.path.join(self.file_path, folder, new_name)

        if old_path != new_path and os.path.exists(old_path):
            os.rename(old_path, new_path)

    def clear_name2(self, files):
        for country in self.file_path_list:
            for file in files:
                if any(file.endswith(ext) for ext in self.FILE_EXTENSIONS):
                    self._rename_file(country, file)

    def clear_name(self):
        for filename in self.file_path_list:
            if any(filename.endswith(ext) for ext in self.FILE_EXTENSIONS):
                self._rename_file('', filename)

    def clean_name_space(self, root, files, sunday):

        banner_dir = os.path.join(root, "Banner")
        os.makedirs(banner_dir, exist_ok=True)

        if sunday == 'on':
            cleaner = lambda: self.clear_name2(files)
        else:
            cleaner = self.clear_name

        if any(file.endswith(ext) for file in files for ext in self.FILE_EXTENSIONS):
            cleaner()
        else:
            print("⚠️ No supported files to rename.")