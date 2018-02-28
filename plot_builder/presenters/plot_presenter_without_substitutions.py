import json

from plot_builder.interfaces.plot_presenter_interface import PlotPresenterInterface


class PlotPresenterWithoutSubstitution(PlotPresenterInterface):
    def __init__(self, coded_plot, trope_definitions, space):
        self.coded_plot = coded_plot
        self.trope_definitions = trope_definitions
        self.space = space

    def present(self):
        print("<#>: [<trope_id>, [<characters>], [<places>], [<objects>]]")
        for index,event in enumerate(self.coded_plot.list_of_events):
            event_as_string = [event.trope_id, event.list_of_character_ids, event.list_of_place_ids,
                   event.list_of_object_ids]
            print("{}: {}".format(index, event_as_string))
