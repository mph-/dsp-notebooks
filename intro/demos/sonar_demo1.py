import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots, show
from matplotlib.patches import Arc, Rectangle, Polygon
from .lib.sonar import Sonar
from .lib.wave import Wave
import numpy as np


def draw_target(axes, origin, W=30, L=40, H=20, alpha=0,
                color='purple'):

    X = origin[0]
    Y = origin[1]

    zorder = 2
    
    p1 = Polygon(((X - 0.5 * H * np.tan(np.radians(alpha)), Y - 0.5 * H),
                  (X + W, Y - 0.5 * H),
                  (X + W, Y + 0.5 * H),
                  (X + 0.5 * H * np.tan(np.radians(alpha)), Y + 0.5 * H)),
                 closed=True, color=color, zorder=zorder)

    axes.add_patch(p1)    


def sonar_demo1_plot(X=16, alpha=20, beamwidth=20, steps=10,
                     virtual_source=False):

    origin = (0, 0)
    
    fig, axes = subplots(1, figsize=(8, 4))
    
    sonar = Sonar(origin=origin)
    sonar.draw(axes)
    
    wave = Wave(origin=origin, step=2, N=steps, raylen=X, theta=beamwidth)
    wave.draw(axes)

    xv = origin[0] + X * 2 * np.cos(np.radians(-alpha))**2
    yv = origin[1] + X * 2 * np.cos(np.radians(-alpha)) * np.sin(np.radians(-alpha))
    vorigin = (xv, yv)

    draw_target(axes, (X, 0), alpha=alpha, W=30)

    zorder = 3 if virtual_source else 1
    
    rwave = Wave(origin=vorigin, step=-2, N=steps, raylen=X,
                 theta=beamwidth, alpha=-2 * alpha, rayorigin=(X, 0))
    rwave.draw(axes, linestyle='--', zorder=zorder)

    axes.axis('equal')
    axes.set_ylim(-10, 10)
    axes.set_xlim(0, 10)
    #axes.set_xlim(-5, 15)    

def sonar_demo1():
    interact(sonar_demo1_plot, X=(4, 20, 2), alpha=(-30, 30, 5),
             beamwidth=(5, 30, 5), continuous_update=False)
