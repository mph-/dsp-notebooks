# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots, setp

response_modes = ['Step response', 'Impulse response', 'Frequency response']

def polezero_plot_with_time(t, h, poles=None, zeros=None, ylim=None,
                            mode=response_modes[0], **kwargs):

    fig, axes = subplots(1, 2, figsize=(12, 6))
    
    axes[0].grid(True)
    axes[0].set_xlim(-20, 20)
    axes[0].set_ylim(-20, 20)
    axes[0].set_xlabel('Real')
    axes[0].set_ylabel('Imaginary')    

    if poles is not None:
        axes[0].plot(poles.real, poles.imag, 'bx', ms=20)
    if zeros is not None:        
        axes[0].plot(zeros.real, zeros.imag, 'bo', ms=20, fillstyle='none')

    if 'Frequency' in mode:
        mlines = axes[1].semilogx(t, 20 * np.log10(abs(h)), label='magnitude (dB)')
        axes[1].set_xlabel('Frequency (Hz)')
        ax2 = axes[1].twinx()
        plines = ax2.semilogx(t, np.degrees(np.arctan2(h.imag, h.real)), '-.',
                              label='phase (deg)', color='orange')
        lines = mlines + plines
        labels = [l.get_label() for l in lines]
        axes[1].legend(lines, labels)        
        ax2.set_ylim(-180, 180)
    else:
        axes[1].plot(t, h)        
        axes[1].set_xlabel('Time (s)')
    
    if ylim is not None:
        axes[1].set_ylim(ylim)
    axes[1].grid(True)


    #axes[1].set_ylabel('Amplitude')

    return axes
