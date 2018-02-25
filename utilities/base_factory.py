class BaseFactory(object):
    _mocking_class = None

    @classmethod
    def get_default_class(cls):
        raise Exception("No default class")

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._mocking_class is not None:
            return cls._mocking_class(*args, **kwargs)

        return cls.get_default_class()(*args, **kwargs)

    def set_mocking_class(self, new_mocking_class):
        self._mocking_class = new_mocking_class

    def clear_moking_class(self):
        self._mocking_class = None
