class EventEntity(object):
    def __init__(self, subjects=None, subjects_initial_states=None, subjects_final_states=None,
                 actions=None, objects=None, objects_initial_states=None, objects_final_states=None,
                 places=None, places_initial_states=None, places_final_states=None,
                 interpretations=None):
        self.subjects = subjects
        self.subjects_initial_states = subjects_initial_states
        self.subjects_final_states = subjects_final_states
        self.actions = actions
        self.objects = objects
        self.objects_initial_states = objects_initial_states
        self.objects_final_states = objects_final_states
        self.places = places
        self.places_initial_states = places_initial_states
        self.places_final_states = places_final_states
        self.interpretations = interpretations
