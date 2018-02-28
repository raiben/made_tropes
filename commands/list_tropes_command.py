from commands.base_command import BaseCommand
from plot_builder.use_cases.list_tropes_use_case import ListTropesUseCase


class ListTropesCommand(BaseCommand):
    just_chromosome = None

    def run(self):
        use_case = ListTropesUseCase()
        return use_case.run()

    @staticmethod
    def get_description():
        return "List all the tropes as a json"

    @staticmethod
    def get_parameters():
        return ""

    @staticmethod
    def get_sample_usage():
        return ""
