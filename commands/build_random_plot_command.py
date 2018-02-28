from commands.base_command import BaseCommand
from plot_builder.interfaces.plot_presenter_interface import PlotPresenterFactory
from plot_builder.interfaces.random_generator_interface import RandomGeneratorFactory
from plot_builder.presenters.plot_presenter_without_substitutions import PlotPresenterWithoutSubstitution
from plot_builder.use_cases.build_random_plot_use_case import BuildRandomPlotUseCase


class BuildRandomPlotCommand(BaseCommand):
    just_chromosome = None

    def run(self):
        if "seed" in self.arguments:
            random_generator = RandomGeneratorFactory.get_instance()
            random_generator.set_seed(int(self.arguments["seed"]))

        just_chromosome = "just_chromosome" in self.arguments and self.arguments["just_chromosome"] == 'y'
        if just_chromosome:
            PlotPresenterFactory.set_mocking_class(PlotPresenterWithoutSubstitution)

        use_case = BuildRandomPlotUseCase()
        return use_case.run()

    @staticmethod
    def get_description():
        return "Builds a random plot"

    @staticmethod
    def get_parameters():
        return "- seed: Random generator seed. >=0 for a specific seed. If not present, use random.\n" \
               "- just_chromosome: Whether or not print just the encoded chromosome. y/n. Default 'n'.\n"

    @staticmethod
    def get_sample_usage():
        return "seed=0 substitute=n"
