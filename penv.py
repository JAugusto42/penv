#!/usr/bin/env python

import subprocess
import os
import sys
from pathlib import Path


class Main():
    """
    Main Class
    """

    def __init__(self):
        self.dirpath = os.getcwd()
        self.folder_name = os.path.basename(self.dirpath)
        self.create_venv = 'virtualenv ' + self.folder_name
        # TODO refatoring
        self.home_dir = str(Path.home())
        self.venv_dir = self.home_dir + "/.local/share/virtualenvs/"

        try:
            subprocess.call(['virtualenv'])
            # continue the code below
        except FileNotFoundError:
            resp = input(str('virtualenv not installed, install? [y/n]'))
            if resp == 'y' or resp == 'Y':
                # maybe this is not the best way to do that,
                # but we need the virtualenv on main interpreter,
                # send me a pull request if you now a best way thx.
                os.system('sudo pip install virtualenv')
            else:
                exit()

    def check_dir(self):
        self.venv_name = self.venv_dir + self.folder_name + '_venv'

        if os.path.exists(self.venv_dir):
            if os.path.exists(self.venv_name):
                self.activate_venv = "source " + self.venv_name + "/bin/activate"
                os.system(self.activate_venv)
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
            return self.check_dir()


Main()
