#!/usr/bin/env python

import os
from pathlib import Path


class Main():
    """
    Main Class
    """
    def __init__(self):
        self.dirpath = os.getcwd()
        self.folder_name = os.path.basename(self.dirpath)
        self.command_to_create_venv = 'virtualenv ' + self.folder_name
        # TODO refatoring
        self.home_dir = str(Path.home())
        self.venv_dir = self.home_dir + "/.local/share/virtualenvs/"
        self.check_dir()

    def check_dir(self):
        self.venv_name = self.venv_dir + self.folder_name + '_venv'

        if os.path.exists(self.venv_dir):
            if os.path.exists(self.venv_name):
                self.command_to_activate_venv = "source " + self.venv_name + "/bin/activate"
                os.system(self.command_to_activate_venv)
                # TODO verify if requirements is update

            else:
                response = input('This project dont have an virtualenvironment create? [Y/n]')
                print(response)
                print('creating a virtualenv')
                os.system('virtualenv ' + self.venv_name)
                print('verify if exists requirements.txt')
        else:
            print('Dir virtualenv on {} not exists, creating...'.format(self.venv_dir))
            os.makedirs(self.venv_dir)
            return check_dir()



Main()
