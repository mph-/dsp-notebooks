from ipywidgets import interactive, ToggleButtons, FloatSlider, IntSlider, Checkbox
from IPython.display import display
from .lib.rtaudio import RTAudio
import scipy.signal as signal
import numpy as np

Msize = 1024
Mmax = 48 * 1024
depthmax = 1000
ratemax = 10
fs = 48000

class Demo(RTAudio):

    def __init__(self, *args, **kwargs):
        super (Demo, self).__init__(*args, **kwargs)

        self.alpha = 0.5
        self.depth = 200
        self.M = 5000
        self.rate = 10
        self.delta_M = 0
        self.delaybuffer = np.zeros(Mmax)
        
        self.enable = True
        self.m = self.M

    def __call__(self, x):

        self.delaybuffer[0:Mmax - Msize] = self.delaybuffer[Msize:]
        self.delaybuffer[-Msize:] = x
        
        if not self.enable:
            return x

        if True:
            # Perhaps use sinusoidal modulation rather than triangular?
            self.m += self.delta_M
            if (self.m > self.M + self.depth) or (self.m <self.M - self.depth):
                self.delta_M = -self.delta_M
                self.m += self.delta_M            
            
        return (1 - self.alpha) * x + self.alpha * self.delaybuffer[-self.m - Msize:-self.m]

    def runstop(self, command):
        
        if command == 'Run':
            self.run()
            print('Running')
        else:
            self.stop()
            print('Stopped')    

    def alpha_set(self, alpha):

        self.alpha = alpha

    def M_set(self, M):

        self.M = M

    def depth_set(self, depth):

        self.depth = depth

    def rate_set(self, rate):

        self.rate = rate
        self.m = self.M
        self.delta_M = int(2 * self.M * Msize * self.rate / fs)

    def enable_set(self, enable):

        self.enable = enable
        

def rt_adt_demo1():
    
    demo = Demo(input_device_index=0, output_device_index=0, fs=fs, frame_length=Msize)

    # Note, need named args
    runstop_widget = interactive(demo.runstop, command=ToggleButtons(options=['Run', 'Stop'],
                                                             description=' ', value='Stop'))

    alpha_widget = interactive(demo.alpha_set, alpha=FloatSlider(description='alpha',
                                                              continuous_update=True, value=0.2,
                                                              min=0.0, max=2.0, step=0.01))

    M_widget = interactive(demo.M_set, M=IntSlider(description='M',
                                                   continuous_update=True, value=1440,
                                                   min=0, max=Mmax, step=100))

    depth_widget = interactive(demo.depth_set, depth=IntSlider(description='depth',
                                                               continuous_update=True, value=1440,
                                                               min=0, max=depthmax, step=100))

    rate_widget = interactive(demo.rate_set, rate=FloatSlider(description='rate',
                                                              continuous_update=True, value=4,
                                                              min=0, max=ratemax, step=0.1))            

    enable_widget = interactive(demo.enable_set,
                                enable=Checkbox(description='enable', value=True))
    
    display(M_widget)    
    display(alpha_widget)
    display(depth_widget)
    display(rate_widget)    
    display(enable_widget)    
    display(runstop_widget)
    
    # print(demo.devices())
    
