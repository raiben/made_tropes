from commands.base_command import BaseCommand
from plot_builder.use_cases.build_random_plot_use_case import BuildRandomPlotUseCase


class BuildRandomPlotCommand(BaseCommand):
    def run(self):
        use_case = BuildRandomPlotUseCase()
        return use_case.run()

    @staticmethod
    def get_description():
        return "Builds a random plot"
