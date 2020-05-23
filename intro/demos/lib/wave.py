import numpy as np
from matplotlib.patches import Arc

class Wave(object):

    def __init__(self, origin=(0, 0), step=2, N=4, alpha=0, theta=60,
                 raylen=0, rayorigin=(0, 0), D=2):

        self.origin = origin
        self.step = step
        self.N = N
        self.D = D
        self.alpha = alpha
        self.theta = theta
        self.raylen = raylen
        self.rayorigin = rayorigin
    
    def draw(self, axes, color='blue', linestyle='-', zorder=1):


        alphar = np.radians(self.alpha)
        
        size = 0
        for n in range(self.N):
            
            size += self.step

            extent = 2 * abs(size) * np.tan(np.radians(self.theta) / 2)
            
            if extent <= self.D:
                x1 = self.origin[0] + size * np.cos(alphar) - 0.5 * self.D * np.sin(alphar)
                x2 = self.origin[0] + size * np.cos(alphar) + 0.5 * self.D * np.sin(alphar)
                y1 = self.origin[1] + size * np.sin(alphar) + 0.5 * self.D * np.cos(alphar)
                y2 = self.origin[1] + size * np.sin(alphar) - 0.5 * self.D * np.cos(alphar)                                
                axes.plot((x1, x2), (y1, y2), linestyle=linestyle,
                          color=color, zorder=zorder)
            else:
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
            
            x1 = x0 + raylen * np.cos(alphar)
            y1 = y0 + raylen * np.sin(alphar)        
        
            axes.plot((x0, x1), (y0, y1), linestyle=linestyle,
                      color=color, zorder=zorder)
