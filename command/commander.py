#!/usr/bin/env python
import subprocess
from pathlib import Path

from .actions import Action


class Commander(object):

    def __init__(self, action, venv_name, python_path):
        self.action = action
        self.python_path = python_path
        self.venv_name = venv_name
        self.venv_path = f'{str(Path.home())}/.local/share/virtualenvs/{venv_name}_penv'

    def check_dir(self):
        return False if subprocess.run(['ls', f'{self.venv_path}'], stdout=subprocess.DEVNULL).returncode else True

    def check_virtualenv_binary(self):
        try:
            subprocess.check_call(['virtualenv', '-h'], stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            self.install_virtualenv()
            if subprocess.run(['virtualenv', '-h']).returncode:
                raise OSError('A pretty serious problem occurred and virtualenv wasn\'t installed.')

    def install_virtualenv(self):
        try:
            if self.check_pip():
                subprocess.check_call(['pip3', 'install', 'virtualenv'])
        except subprocess.CalledProcessError:
            pass
        return True

    @staticmethod
    def check_pip():
        try:
            subprocess.check_call(['pip3', '-V'], stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            raise OSError('No pip was found in operating system. Check if Python 3 or pip is installed.')

        return True

    def invoke_action(self):
        action = Action(self.venv_path, self.python_path)
        getattr(action, self.action)()

    def shutdown(self):
        exit(1)
