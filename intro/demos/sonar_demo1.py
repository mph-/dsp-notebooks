import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots, show
from matplotlib.patches import Arc, Rectangle, Polygon
import numpy as np


def draw_wave(axes, origin=(0, 0), step=2, N=4, alpha=0, theta=60,
              raylen=0, color='blue', linestyle='-', rayorigin=(0, 0)):

    origin = np.array(origin)
    
    size = 0
    for n in range(N):

        #origin[0] += step
        size += step

        e1 = Arc(origin, width=2 * size, height=2 * size,
                 angle=alpha, theta1=-theta / 2, theta2=theta / 2, linewidth=2,
                 zorder=1, color=color, linestyle=linestyle)    

        axes.add_patch(e1)

    if raylen:
        x0 = rayorigin[0]
        y0 = rayorigin[1]        
        x1 = x0 + raylen * np.cos(np.radians(alpha))
        y1 = y0 + raylen * np.sin(np.radians(alpha))        
        
        axes.plot((x0, x1), (y0, y1), linestyle=linestyle,
                  color=color, zorder=1)
    

def draw_reflected_wave(axes, origin=(0, 0), step=2, N=4, theta=60,
                        raylen=0, X=15, alpha=15, linestyle='--'):

    xp = origin[0] + X * 2 * np.cos(np.radians(-alpha))**2
    yp = origin[1] + X * 2 * np.cos(np.radians(-alpha)) * np.sin(np.radians(-alpha))

    draw_wave(axes, (xp, yp), step=-step, N=N, theta=theta, raylen=-raylen,
              color='blue', alpha=-2 * alpha, linestyle=linestyle,
              rayorigin=(X, 0))
    
        
def draw_target_rect(axes, origin, W=30, L=40, H=20, alpha=0):

    x1 = origin[0] + (L / 2) * np.sin(np.radians(alpha))
    y1 = origin[1] + (L / 2) * np.cos(np.radians(alpha))
    x2 = origin[0] - (L / 2) * np.sin(np.radians(alpha))
    y2 = origin[1] - (L / 2) * np.cos(np.radians(alpha))        
    axes.plot((x1, x2), (y1, y2))

    r1 = Rectangle((x2, y2), width=W, height=L, angle=-alpha, zorder=2,
                   fill=True, color='white')
    axes.add_patch(r1)


def draw_target(axes, origin, W=30, L=40, H=20, alpha=0,
                color='purple', block=True):

    X = origin[0]
    Y = origin[1]

    zorder = 2 if block else 1
    
    p1 = Polygon(((X - 0.5 * H * np.tan(np.radians(alpha)), Y - 0.5 * H),
                  (X + W, Y - 0.5 * H),
                  (X + W, Y + 0.5 * H),
                  (X + 0.5 * H * np.tan(np.radians(alpha)), Y + 0.5 * H)),
                 closed=True, color=color, zorder=zorder)

    axes.add_patch(p1)    


def draw_sonar(axes, origin, W=2, H=2, alpha=0, color='black'):

    x2 = origin[0] - (W / 2)
    y2 = origin[1] - (H / 2)

    r1 = Rectangle((x2, y2), width=W, height=H, angle=-alpha, zorder=2,
                   fill=True, color=color)
    axes.add_patch(r1)    


def sonar_demo1_plot(X=10, alpha=20, beamwidth=20, steps=10,
                     virtual_source=False):

    fig, axes = subplots(1)
    
    draw_wave(axes, (0, 0), step=2, N=steps, raylen=X, theta=beamwidth)        
    
    draw_target(axes, (X, 0), alpha=alpha, W=30, block=not virtual_source)
    
    draw_reflected_wave(axes, (0, 0), step=2, N=steps, raylen=X + 2, X=X,
                        alpha=alpha, theta=beamwidth)
    
    draw_sonar(axes, (0, 0))
    
    axes.axis('equal')
    axes.set_ylim(-10, 10)
    axes.set_xlim(0, 10)



def sonar_demo1():
    interact(sonar_demo1_plot, X = (4, 20, 2),  alpha=(-30, 30, 5),
             beamwidth=(5, 30, 5), continuous_update=False)
