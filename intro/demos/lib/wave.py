import numpy as np
from matplotlib.patches import Arc

class Wave(object):

    def __init__(self, origin=(0, 0), step=2, N=4, alpha=0, theta=60,
                 raylen=0, rayorigin=(0, 0)):

        self.origin = origin
        self.step = step
        self.N = N
        self.alpha = alpha
        self.theta = theta
        self.raylen = raylen
        self.rayorigin = rayorigin
    
    def draw(self, axes, color='blue', linestyle='-', zorder=1):

        size = 0
        for n in range(self.N):
            
            size += self.step
            
            e1 = Arc(self.origin, width=2 * size, height=2 * size,
                     angle=self.alpha, theta1=-self.theta / 2,
                     theta2=self.theta / 2,
                     linewidth=2, zorder=zorder, color=color,
                     linestyle=linestyle)    
            
            axes.add_patch(e1)

        if self.raylen:
            x0 = self.rayorigin[0]
            y0 = self.rayorigin[1]

            raylen = self.raylen
            if self.step < 0:
                raylen = -raylen
            
            x1 = x0 + raylen * np.cos(np.radians(self.alpha))
            y1 = y0 + raylen * np.sin(np.radians(self.alpha))        
        
            axes.plot((x0, x1), (y0, y1), linestyle=linestyle,
                      color=color, zorder=zorder)
