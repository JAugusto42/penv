#!/usr/bin/env python
from command.commander import Commander
from command.actions import Action
from utils.argumenter import parse_args


class Penv(object):
    """
    Main Class
    """
    def __init__(self, args):
        self.args = args
        self.commander = Commander(args.action, args.name, args.python_path)

    def start(self):
        answer = None

        if not hasattr(Action, self.args.action):
            print(f'Action {self.args.action} is invalid! Check help command.')
            self.shutdown()

        self.commander.check_pip()
        self.commander.check_virtualenv_binary()

        if self.commander.check_dir():
            self.commander.action = self.args.action if self.commander.action != 'create' else 'no_action_required'
            self.commander.invoke_action()
        else:
            while answer != 'y' and answer != 'n':
                answer = input(
                    f"No virtual environment named \"{self.commander.venv_name}\" was found in your venv directories.\
                    \nWanna create one? [y/n] "
                )
            if answer == 'y':
                self.commander.action = 'create'
                self.commander.invoke_action()
                self.commander.action = self.args.action if self.commander.action != 'create' else 'no_action_required'
                self.commander.invoke_action()
            else:
                print("Refused to create a virtual environment. Exiting...")
                self.shutdown()

        self.shutdown()

    def shutdown(self):
        self.commander.shutdown()


if __name__ == '__main__':
    try:
        penv = Penv(parse_args())
        penv.start()
    except KeyboardInterrupt:
        penv.shutdown()
