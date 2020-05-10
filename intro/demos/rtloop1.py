from ipywidgets import interactive, ToggleButtons, FloatSlider
from IPython.display import display
from .lib.rtaudio import RTAudio
import numpy as np

        
class Demo(RTAudio):

    def __init__(self, *args, **kwargs):
        super (Demo, self).__init__(*args, **kwargs)
        self.gain = 1.0
    
    def __call__(self, in_data):

        if False:
            N = len(in_data)
            t = np.arange(N) / self.fs
            
            signal = 0.5 * np.cos(2 * np.pi * 440 * t)
            return signal
        else:
            return in_data * self.gain

    def runstop(self, command):
        
        if command == 'Run':
            self.run()
            print('Running')
        else:
            self.stop()
            print('Stopped')    

    def gainset(self, gain):
        self.gain = gain
        print(gain)


def rtloop1():
    
    demo = Demo(input_device_index=0, output_device_index=0)        

    # Note, need named args
    runstop_widget = interactive(demo.runstop, command=ToggleButtons(options=['Run', 'Stop'],
                                                             description=' ', value= 'Stop'))

    gain_widget = interactive(demo.gainset, gain=FloatSlider(description='Gain',
                                                             continuous_update=True, value=0.2,
                                                             min=0.0, max=2.0, step=0.01))
    
    display(gain_widget)
    display(runstop_widget)
    
