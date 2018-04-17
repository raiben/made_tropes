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

    @classmethod
    def set_mocking_class(cls,new_mocking_class):
        cls._mocking_class = new_mocking_class

    @classmethod
    def clear_mocking_class(cls):
        cls._mocking_class = None
