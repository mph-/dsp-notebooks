import numpy as np
from matplotlib.patches import Arc

class Lens(object):

    def __init__(self, origin=(0, 0), H=30, f1=40, f2=40):

        self.origin = origin
        self.H = H
        self.f1 = f1
        self.f2 = f2

    def draw(self, axes, color='blue', linestyle='-', zorder=1):

        origin = self.origin

        HH = self.H / 2
        
        theta1 = np.degrees(np.arctan(HH / self.f1))
        theta2 = np.degrees(np.arctan(HH / self.f2))

        r1 = np.sqrt(HH**2 + self.f1**2)
        r2 = np.sqrt(HH**2 + self.f2**2)        
        x1 = -self.f1
        x2 = self.f2
        
        origin1 = (origin[0] + x1, origin[1])
        origin2 = (origin[0] + x2, origin[1])        
                            
        e1 = Arc(origin1, width=2 * r1, height=2 * r1,
                 angle=0, theta1=-theta1, theta2=theta1, linewidth=2,
                 zorder=zorder, color=color, linestyle=linestyle)
        axes.add_patch(e1)

        e2 = Arc(origin2, width=2 * r2, height=2 * r2,
                 angle=0, theta1=180 - theta2, theta2=180 + theta2,
                 linewidth=2, zorder=zorder, color=color,
                 linestyle=linestyle)
        axes.add_patch(e2)        
        
