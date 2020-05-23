import numpy as np
from .sonar import Sonar

class SonarArray(object):

    def __init__(self, origin=(0, 0), M=1, S=4, W=2, H=2, alpha=0):

        self.origin = origin
        self.M = M
        self.S = S
        self.W = W
        self.H = H
        self.alpha = alpha

        self.extent = S * (M - 1) + H
        
        self.sonars = []

        # 0, (-0.5 * S, 0.5 * S), (-S, 0, S)

        for m in range(M):
            off = m * S - 0.5 * (M - 1) * S
            
            
            x0 = origin[0] + off * np.sin(np.radians(alpha))
            y0 = origin[1] + off * np.cos(np.radians(alpha))
                                                       
            self.sonars.append(Sonar((x0, y0), W=W, H=H, alpha=alpha))

    def draw(self, axes, color='black'):

        for sonar in self.sonars:
            sonar.draw(axes, color=color)
            
