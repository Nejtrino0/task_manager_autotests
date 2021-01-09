import os
import pathlib
import shutil

absolute_dir = str(pathlib.Path(__file__).parent.absolute())


class ReportManager:
    def __init__(self, path):
        self.path = path

    def delete(self):
        for file in os.listdir(absolute_dir + self.path):
            path_to_remove = ''.join([absolute_dir, self.path, file])

            if file.endswith('.html') or file.endswith('.png'):
                os.remove(path_to_remove)

            else:
                shutil.rmtree(path_to_remove, ignore_errors=True)


