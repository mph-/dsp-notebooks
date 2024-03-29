# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots, setp

response_modes = ['Step response', 'Impulse response', 'Frequency response',
                  'AC response omega=1', 'AC response omega=10',
                  'DC response']

ylims = {'Step response': (-0.5, 2.1), 'Impulse response': (-5, 10),
         'Frequency response': (-40, 20), 'AC response omega=1': (-2.1, 2.1),
         'AC response omega=10': (-2.1, 2.1), 'DC response': (-2.1, 2.1)}


def polezero_plot(axes, poles, zeros):

    axes.grid(True)
    axes.set_xlim(-30, 10)
    axes.set_ylim(-20, 20)
    axes.set_xlabel('Real')
    axes.set_ylabel('Imaginary')
    # Show axes
    axes.plot((-30, 10), (0, 0), 'k')
    axes.plot((0, 0), (-20, 20), 'k')

    def annotate(axes, poles, offset=None):
        if offset is None:
            xmin, xmax = axes.get_xlim()
            offset = (xmax - xmin) / 27

        plist = list(poles)
        for pole in set(poles):
            num = plist.count(pole)
            if num > 1:
                axes.text(pole.real + offset, pole.imag + offset, '%d' % num)

    if poles is not None:
        poles = np.array(poles)
        axes.plot(poles.real, poles.imag, 'C0x', ms=20)
        annotate(axes, poles)

    if zeros is not None:
        zeros = np.array(zeros)
        axes.plot(zeros.real, zeros.imag, 'C0o', ms=20, fillstyle='none')
        annotate(axes, zeros)


def polezero_plot_with_time(t, h, poles=None, zeros=None, ylim=None,
                            mode=response_modes[0], **kwargs):

    fig, axes = subplots(1, 2, figsize=(12, 6))

    polezero_plot(axes[0], poles, zeros)

    if 'DC' in mode:
        axes[1].plot(t, t * 0 + 1, color='C1', label='input')
    elif 'AC' in mode:
        if '10' in mode:
            axes[1].plot(t, np.cos(10 * t), color='C1', label='input')
        else:
            axes[1].plot(t, np.cos(1 * t), color='C1', label='input')
    elif mode == 'Step response':
        axes[1].plot(t, (t >= 0) * 1, color='C1', label='input')

    if 'Frequency' in mode:
        mlines = axes[1].semilogx(
            t, 20 * np.log10(abs(h)), label='magnitude (dB)')
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
        axes[1].plot(t, h, color='C0', label='output')
        axes[1].set_xlabel('Time (s)')
        axes[1].legend()

    if ylim is None:
        ylim = ylims[mode]
    axes[1].set_ylim(ylim)
    axes[1].grid(True)

    # axes[1].set_ylabel('Amplitude')

    return axes


def polezero_frequency_impulse_plot(obj, t, w, title):

    w1, H = obj.response('Frequency response', t, w)

    t, h = obj.response('Impulse response', t, w)
    if h is None:
        return False

    fig, axes = subplots(1, 3, figsize=(12, 6))

    polezero_plot(axes[0], obj.poles, obj.zeros)

    axes[0].set_title('Pole-zero (%s)' % title)

    f = w / (2 * np.pi)
    mlines = axes[1].semilogx(f, 20 * np.log10(abs(H)), label='magnitude (dB)')
    axes[1].set_xlabel('Frequency (Hz)')
    ax2 = axes[1].twinx()
    plines = ax2.semilogx(t, np.degrees(np.arctan2(H.imag, H.real)), '-.',
                          label='phase (deg)', color='C1')
    lines = mlines + plines
    labels = [l.get_label() for l in lines]
    axes[1].legend(lines, labels)
    ax2.set_ylim(-180, 180)
    ax2.set_yticks((-180, -120, -60, 0, 60, 120, 180))

    axes[1].set_title('Frequency response')
    axes[1].grid(True)

    axes[2].plot(t, h, color='C0', label='output')
    axes[2].set_xlabel('Time (s)')
    axes[2].set_title('Impulse response')
    axes[2].grid(True)

    fig.tight_layout()
    return True
