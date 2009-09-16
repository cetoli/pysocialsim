"""
Defines the module with implementations of Object class.

@author: Fabricio Barros
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
"""
from copy import copy

class Object(object):
    """
    Define a superclass that implements protected visibility.
    @author: Fabricio Barros
    @organization: Federal University of Rio de Janeiro
    @contact: fbarros@gmail.com
    """
    
    def __new__(cls, *args, **kwargs):
        """
        Overrides static method for creating objects.
        @param cls: class object
        @type cls: class
        @param args: function's list of arguments
        @type args: tuple
        @param kwargs: parameter names
        @type kwargs: dict
        @return: Returns an object created by function.
        @rtype: object
        """
        obj = object.__new__(cls)        
        cls.__init__(obj, *args, **kwargs)
                                
        def __getattr__(self, name):            
            attr = getattr(obj, name)
            if hasattr(attr, "__public__"):
                return attr
            elif hasattr(cls, "__public__"):
                if name in cls.__public__:
                    return attr
        
            raise AttributeError, "Attribute %s is not public."%name
        
        def __setattr__(self, name, value):
            cls.__setattr__(self, name, value)    

        def is_own_magic(cls, name, without=[]):
            return name not in without and\
                   name.startswith("__") and name.endswith("__")
                   
        Proxy = type(cls.__name__,(),{})   

        for name in dir(cls):
            if is_own_magic(cls,name, without=dir(Proxy)):
                try:
                    setattr(Proxy, name, getattr(obj,name))
                except TypeError:
                    pass
        
        Proxy.__getattr__ = __getattr__
        Proxy.__setattr__ = __setattr__
        return Proxy()
    
    def __init__(self, *args, **kwargs):
        self.initialize(*args, **kwargs)
    
    def initialize(self, *args, **kwargs):
        """
        Initializes an object.
        @param args: function's list of arguments
        @type args: tuple
        @param kwargs: parameter names
        @type kwargs: dict
        @return: Returns an object created by function.
        @rtype: None
        """
        raise NotImplementedError()
    
    def clone(self):
        """
        Creates a new object from prototype instance.
        @return: a Object
        @rtype: Object
        """
        clone = copy(self)
        return clone