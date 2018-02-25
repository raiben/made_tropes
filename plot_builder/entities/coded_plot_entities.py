class CodedPlotEntity(object):
    def __init__(self):
        self.list_of_events = []


class CodedPlotEventEntity(object):
    def __init__(self):
        self.trope_id = None
        self.list_of_character_ids = []
        self.list_of_place_ids = []
        self.list_of_object_ids = []
