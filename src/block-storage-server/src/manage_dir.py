import os

class ManageDir:
    def __init__(self, dir_name = '__files__'):
        self.dir_name = '__files__'

    def createWorkDir(self):
        if os.path.isdir(self.dir_name):
            print('Work dir exists, skipping.')
            return
        try:
            os.mkdir(self.dir_name)
            print(f'Dir {self.dir_name} created.')
        except OSError as err:
            return err

    def save(self, file, name):
        file.save(os.path.join(self.dir_name, name))