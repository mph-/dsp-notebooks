# M. P. Hayes UCECE
from ipywidgets import interact as ipyinteract
from matplotlib.pyplot import show

def interact(func, *args, **kwargs):

    def func_show(*args, **kwargs):

        func(*args, **kwargs)
        show()

    kwargs.pop('continuous_update', None)

    # This does not work since it looks at the default args of the
    # called function but will look at func_show instead of func.
    ipyinteract(func_show, *args, **kwargs)
    
