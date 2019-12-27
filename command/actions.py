#!/usr/bin/env python
import shlex
import subprocess


class Action:

    def __init__(self, venv_path, python_path):
        self.venv_path = venv_path
        self.python_path = python_path

    def create(self):
        try:
            subprocess.check_call(['virtualenv', f'--python={self.python_path}', self.venv_path])
        except subprocess.CalledProcessError as e:
            print(f"Error in calling the command: {e}")

    def remove(self):
        try:
            subprocess.check_call(['rm', '-rf', self.venv_path])
        except subprocess.CalledProcessError as e:
            print(f"Error in calling the command: {e}")

    def update_packages(self):
        command = shlex.split(
            f""" source {self.venv_path}/bin/activate && 
            pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U"""
        )

        try:
            subprocess.check_call([
                command
            ])
        except subprocess.CalledProcessError as e:
            print(f"Error in calling the command: {e}")

    def change_environment(self):
        pass

    def exit_environment(self):
        pass

    def no_action_required(self):
        """
        Fallback function for unavailable
        """
        print('No action required in the moment.')
