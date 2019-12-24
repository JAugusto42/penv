#!/usr/bin/env python
from utils.argumenter import parse_args
from command.commander import Commander
from command.actions import Action


class Penv(object):
    """
    Main Class
    """
    def __init__(self, args):
        self.args = args
        self.commander = Commander(args.action, args.name, args.python_path)

    def start(self):
        import pdb; pdb.set_trace()
        answer = None
        if not hasattr(Action(self.commander.venv_name, self.commander.shell), self.args.action):
            print(f'Action {self.args.action} is invalid! Check help command.')
            self.commander.shell.kill()
            exit(1)

        self.commander.check_pip()
        self.commander.check_virtualenv_binary()

        if not self.commander.check_dir():
            while answer != 'y' and answer != 'n':
                answer = input(
                    f"No virtual environment named {self.commander.venv_name} was found in your venv directories.\
                     Wanna create one? [y/n]"
                )

            if answer == 'y':
                self.commander.action = 'create'
                self.commander.invoke_action()
                self.commander.action = self.args.action
                self.commander.invoke_action()
            else:
                print("Refused to create a virtual environment. Exiting...")
                exit(1)

        self.commander.invoke_action()


if __name__ == '__main__':
    penv = Penv(parse_args())
    penv.start()
