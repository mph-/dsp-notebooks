import numpy as np
from ipywidgets import interact, interactive, fixed
from IPython.display import display, Math
from matplotlib.pyplot import subplots, show
from .lib.lens import Lens
import numpy as np

def ir_range_sensor_demo1_plot(r=50, d=20, f=10, rays=False):

    X = 50
    Hl = 15
    Ht = 20    

    x0 = X
    y0 = 0
    
    origin = (x0, y0)

    xt = X - r
    yt = 0

    xled1 = x0 + f
    yled1 = y0
    
    xl1 = x0 + f
    yl1 = y0
    
    xl2 = x0
    yl2 = y0 - d
    
    xp = x0 + f
    yp = y0 - d - f * d / r
    
    fig, axes = subplots(1, figsize=(8, 4))

    # Target
    axes.plot((xt, xt), (-Ht / 2, Ht / 2), color='black')
    
    lens1 = Lens(origin, H=Hl)
    lens2 = Lens((origin[0], origin[1] - d), H=Hl)

    lens1.draw(axes)
    lens2.draw(axes)

    # Tx ray
    axes.plot((xled1, xt), (yled1, yt), color='C0')
    # Rx ray
    axes.plot((xt, xp), (yt, yp), color='C0')

    if rays:
        axes.plot((xt, xl2), (yt, yl2 + Hl / 2), color='C0', linestyle='--')
        axes.plot((xl2, xp), (yl2 + Hl / 2, yp), color='C0', linestyle='--')

        axes.plot((xt, xl2), (yt, yl2 - Hl / 2), color='C0', linestyle='--')
        axes.plot((xl2, xp), (yl2 - Hl / 2, yp), color='C0', linestyle='--')

    axes.plot((xl2, xp), (yl2, yl2), linestyle=':', color='black')    

    axes.axis('equal')
    axes.set_ylim(-30, 10)
    axes.set_xlim(0, 40)

    
    display(Math('x = %.1f' % (f * d / r)))

def ir_range_sensor_demo1():
    interact(ir_range_sensor_demo1_plot, r=(10, 70, 5),
             f=(5, 15, 1), d=(15, 25, 5),
             continuous_update=False)
