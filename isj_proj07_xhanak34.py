#!/usr/bin/env python3

class TooManyCallsError(Exception):
    """Call count error class"""
    pass

def limit_calls(max_calls = 2, error_message_tails = "called too often"):
    """Custom function decorator"""

    def func_decorator(function):
        """Decorating function"""
        
        def func_wrapper(*args,**kwargs):
            """Wrapper for function"""
            func_wrapper.numcalls += 1
            if func_wrapper.numcalls > max_calls:
                raise TooManyCallsError('function "'+str(function.__name__)+'" - '+error_message_tails)
            return function(*args,**kwargs)

        func_wrapper.numcalls = 0
        return func_wrapper
                                             
    return func_decorator  

def ordered_merge(*args,**kwargs):
    """Method that generates a list of values
    from arguments based on selector sequence."""
    if 'selector' in kwargs:
        sequence = kwargs['selector']
    else:
        return []

    gendict = {}  # storing number of elements used from generators
    generators = []  # list of generators
    generated = []  # list of generated values

    for item in sequence:
        gendict.update({item: 0})  # fill up dict with selectors
    
    for arg in args:
        generators.append(arg)  # fill up list of generators

    for s in sequence:
        generated.append(generators[s][gendict[s] % len(generators[s])])
        gendict[s] += 1  # value from generator used, increment

    return generated
        
class Log():
    """class for logging"""
    def __init__(self, filename):
        """Constructor"""
        self.filename = filename
        self.logfile = open(filename, "w") 

    def __enter__(self):
        """Method specifying actions to take when a log object is created."""
        self.logfile.write("Begin\n")
        return self

    def __exit__(self, etype, evalue, etraceback):
        """Method specifying actions to take when a log object is destroyed."""
        self.logfile.write("End\n")
        self.logfile.close()

    def logging(self, string):
        """Function that logs actions performed."""
        self.logfile.write(string + "\n")
