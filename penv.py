#!/usr/bin/env python3

import os
from pathlib import Path


class Main():
    """
    DOC
    """
    def __init__(self):
        self.dirpath = os.getcwd()
        self.folder_name = os.path.basename(self.dirpath)
        self.command_to_create_venv = 'virtualenv ' + self.folder_name
        self.home_dir = str(Path.home())
        self.venv_dir = self.home_dir + "/.local/share/venvs/"
        self.check_dir()

    def check_dir(self):
        if os.path.exists(self.venv_dir):
            # activate venv
        else:
            os.makedirs(self.venv_dir)

            print('verify if exists requirements.txt')


Main()
