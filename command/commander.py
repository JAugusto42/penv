#!/usr/bin/env python
import os
import subprocess
from pathlib import Path

from .actions import Action


class Commander(object):

    def __init__(self, action, venv_name, python_path):
        self.action = action
        self.python_path = python_path
        self.shell = subprocess.Popen(
            "/bin/bash",
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.venv_name = venv_name
        self.venv_path = f'{str(Path.home())}/.local/share/virtualenvs/{venv_name}_venv'

    def check_dir(self):
        return False if subprocess.run(['ls', f'{self.venv_path}']).returncode else True

    def check_virtualenv_binary(self):
        try:
            subprocess.run(['virtualenv', '-h'], check=True)
        except subprocess.CalledProcessError:
            self.install_virtualenv()
            if subprocess.run(['virtualenv', '-h']).returncode:
                raise Exception('A pretty serious problem occurred and virtualenv wasn\'t installed.')

    def install_virtualenv(self):
        try:
            if self.check_pip():
                subprocess.run(['pip3', 'install', 'virtualenv'], check=True)
        except subprocess.CalledProcessError:
            pass
        return True

    @staticmethod
    def check_pip():
        try:
            subprocess.run(['pip3', '-V'], check=True)
        except subprocess.CalledProcessError:
            raise OSError('No pip was found in operating system. Check if Python 3 or pip is installed.')

        return True

    def invoke_action(self):
        action = Action(self.venv_name, self.shell)
        getattr(action, self.action)()
