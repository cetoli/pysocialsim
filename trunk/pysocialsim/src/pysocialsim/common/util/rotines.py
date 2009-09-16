"""
Defines the module with util common rotines.

@author: Fabricio
@organization: Federal University of Rio de Janeiro
@contact: fbarros@gmail.com 
@since: 24/08/2009
"""
from pysocialsim.common.error.invalid_value_error import InvalidValueError

def requires(variable, *tupleOfTypes):
    if variable <> None:
        if (not isinstance(variable, *tupleOfTypes)) and (not implements(variable, *tupleOfTypes)):
            raise TypeError()
    return True

def returns(variable, *tupleOfTypes):
    requires(variable, *tupleOfTypes)
    return variable

def implements(variable, *tupleOfTypes):
    for t in tupleOfTypes:
        operations = [attr for attr in t.__dict__.keys() if callable(t.__dict__[attr]) and (attr <> "__init__")]
        if not operations:
            raise TypeError()
        for opName in operations:
            try:
                getattr(variable, opName)
            except AttributeError:
                raise TypeError()
        
    return True

def pre_condition(variable, validation):
    if not validation(variable):
        raise InvalidValueError()
    return variable
    
def post_condition(variable, validation):
    if not validation(variable):
        raise InvalidValueError()
    return variable

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
