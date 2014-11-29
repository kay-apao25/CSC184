class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class Child(Singleton):
    pass

class Borg(object):
    _shared_state = {}
    
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class Child1(Borg):
    pass

class AnotherChild(Borg):
    _shared_state = {}
