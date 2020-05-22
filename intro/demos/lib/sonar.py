from matplotlib.patches import Rectangle

class Sonar(object):

    def __init__(self, origin, W=2, H=2, alpha=0):

        self.origin = origin
        self.W = W
        self.H = H
        self.alpha = alpha

    def draw(self, axes, color='black'):

        x2 = self.origin[0] - (self.W / 2)
        y2 = self.origin[1] - (self.H / 2)
        
        r1 = Rectangle((x2, y2), width=self.W, height=self.H,
                       angle=-self.alpha, zorder=2,
                       fill=True, color=color)
        axes.add_patch(r1)
        
