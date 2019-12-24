#!/usr/bin/env python


class Action:

    def __init__(self, venv_name, pipe):
        self.venv_name = venv_name
        self.pipe = pipe

    def create(self):
        pass

    def remove(self):
        pass

    def update_packages(self):
        pass

    def change_environment(self):
        pass

    def exit_environment(self):
        pass

