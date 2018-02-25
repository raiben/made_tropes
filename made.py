import sys

from commands.base_command import BaseCommand
from commands import *


class MainClass(object):
    def __init__(self):
        self.commands_subclasses = BaseCommand.__subclasses__()
        self.command_name = None
        self.command = None

    def run(self):
        self.check_command_is_provided()
        self.retrieve_command_and_check_existence()
        self.run_command_with_rest_of_arguments()

    def check_command_is_provided(self):
        if len(sys.argv) == 1:
            self.print_error_no_command_introduced()
            self.print_valid_commands()
            exit(0)

    def retrieve_command_and_check_existence(self):
        self.command_name = sys.argv[1]
        commands = [command for command in self.commands_subclasses if self.command_name == command.__name__]
        if len(commands) == 0:
            self.print_error_command_not_found()
            self.print_valid_commands()
            exit(0)
        self.command = commands[0]

    def run_command_with_rest_of_arguments(self):
        instance = self.command(sys.argv[1:])
        self.print_running_command()
        instance.run()

    def print_valid_commands(self):
        print("Please, select one of the commands below:")
        command_help_template = " - {command}: {description}"
        for subClass in self.commands_subclasses:
            print(command_help_template.format(command=subClass.__name__, description=subClass.get_info()))

    @staticmethod
    def print_error_no_command_introduced():
        print("No command introduced.")

    def print_error_command_not_found(self):
        print("Command not found: {}".format(self.command_name))

    def print_running_command(self):
        print("Running command {}".format(self.command_name))


MainClass().run()
