"""
Defines the module with implementations of function decorators.

@author: Fabricio Barros
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
"""


def public(f):
    """
    Decorator used to assign the attribute __public__ to methods.
    @param f: decorated function
    @type f: function
    """
    f.__public__ = True
    return f