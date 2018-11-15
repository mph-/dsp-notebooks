# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots, setp

response_modes = ['Step response', 'Impulse response', 'Frequency response',
                  'AC response omega=1', 'AC response omega=10',
                  'DC response']
                  
ylims = {'Step response': (-0.5, 2.1), 'Impulse response' : (-5, 10),
         'Frequency response': (-40, 20), 'AC response omega=1':(-2.1, 2.1),
         'AC response omega=10':(-2.1, 2.1), 'DC response':(-2.1, 2.1)}

def polezero_plot_with_time(t, h, poles=None, zeros=None, ylim=None,
                            mode=response_modes[0], **kwargs):

    fig, axes = subplots(1, 2, figsize=(12, 6))
    
    axes[0].grid(True)
    axes[0].set_xlim(-30, 10)
    axes[0].set_ylim(-20, 20)
    axes[0].set_xlabel('Real')
    axes[0].set_ylabel('Imaginary')
    # Show axes
    axes[0].plot((-30, 10), (0, 0), 'k')
    axes[0].plot((0, 0), (-20, 20), 'k')    

    if poles is not None:
        poles = np.array(poles)
        axes[0].plot(poles.real, poles.imag, 'C0x', ms=20)
    if zeros is not None:
        zeros = np.array(zeros)
        axes[0].plot(zeros.real, zeros.imag, 'C0o', ms=20, fillstyle='none')

    if 'DC' in mode:
        axes[1].plot(t, t * 0 + 1, color='C1')        
    elif 'AC' in mode:
        if '10' in mode:
            axes[1].plot(t, np.cos(10 * t), color='C1')
        else:
            axes[1].plot(t, np.cos(1 * t), color='C1')
    elif mode == 'Step response':
        axes[1].plot(t, (t >= 0) * 1, color='C1')        
        
    if 'Frequency' in mode:
        mlines = axes[1].semilogx(t, 20 * np.log10(abs(h)), label='magnitude (dB)')
        axes[1].set_xlabel('Angular frequency (rad/s)')
        ax2 = axes[1].twinx()
        plines = ax2.semilogx(t, np.degrees(np.arctan2(h.imag, h.real)), '-.',
                              label='phase (deg)', color='C1')
        lines = mlines + plines
        labels = [l.get_label() for l in lines]
        axes[1].legend(lines, labels)        
        ax2.set_ylim(-180, 180)
        ax2.set_yticks((-180, -120, -60, 0, 60, 120, 180))
    else:
        axes[1].plot(t, h, color='C0')
        axes[1].set_xlabel('Time (s)')

    if ylim is None:
        ylim = ylims[mode]
    axes[1].set_ylim(ylim)
    axes[1].grid(True)


    #axes[1].set_ylabel('Amplitude')

    return axes
