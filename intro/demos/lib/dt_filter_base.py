from matplotlib.pyplot import subplots
from scipy.signal import freqz, lfilter
from numpy import exp, sin, cos, sqrt, pi, angle, unwrap
import numpy as np
from .signal_plot import lollipop_plot

response_modes = ['Step response', 'Impulse response',
                  'Frequency response', 'Frequency response (Bode)',
                  'AC response f0=1', 'AC response f0=10',
                  'DC response']

ylims = {'Step response': (-0.5, 2.1), 'Impulse response': (-0.5, 2.1),
         'Frequency response (Bode)': (-40, 20),
         'Frequency response': (0, 2),
         'AC response f0=1': (-2.1, 2.1), 'AC response f0=10': (-2.1, 2.1),
         'DC response': (-2.1, 2.1)}


class DTFilterBase(object):

    @property
    def fs(self):
        return 1 / self.dt

    @property
    def poles(self):
        return self.tf.poles

    @property
    def zeros(self):
        return self.tf.zeros

    def dc_response(self, n):

        H = self.frequency_response(0)
        return 0 * n + H.real

    def ac_response(self, n, f0):

        H = self.frequency_response(f0)

        phase = angle(H)
        mag = abs(H)

        return mag * cos(2 * np.pi * f0 * n * self.dt + phase)

    def frequency_response(self, f):

        w, H = freqz(self.b, self.a, f, fs=self.fs)
        return H

    def impulse_response(self, n):

        x = n * 0
        x[n == 0] = 1
        h = lfilter(self.b, self.a, x)
        return h

    def step_response(self, n):

        x = n >= 0
        h = lfilter(self.b, self.a, x)
        return h

    def time_input(self, mode, n):

        if mode == 'Step response':
            return n >= 0
        elif mode == 'Impulse response':
            x = np.zeros_like(n)
            x[n == 0] = 1
            return x
        elif mode == 'DC response':
            return np.ones_like(n)
        elif mode == 'AC response f0=1':
            return cos(2 * np.pi * 1 * n * self.dt)
        elif mode == 'AC response f0=10':
            return cos(2 * np.pi * 10 * n * self.dt)
        raise ValueError('Unknown mode=%s', mode)

    def time_response(self, mode, n):

        if mode == 'Step response':
            return self.step_response(n)
        elif mode == 'Impulse response':
            return self.impulse_response(n)
        elif mode == 'DC response':
            return self.dc_response(n)
        elif mode == 'AC response f0=1':
            return self.ac_response(n, 1)
        elif mode == 'AC response f0=10':
            return self.ac_response(n, 10)
        raise ValueError('Unknown mode=%s', mode)

    def response(self, mode, n):

        if mode in ('Frequency response', 'Frequency response (Bode)'):
            N = len(n)
            f = 0.5 * np.arange(N) / (N * self.dt)
            return f, self.frequency_response(f)
        else:
            return n, self.time_response(mode, n)

    def polezero_plot(self, axes=None, **kwargs):

        from matplotlib.pyplot import Circle

        def annotate(axes, roots, offset=None):
            if offset is None:
                xmin, xmax = axes.get_xlim()
                offset = (xmax - xmin) / 27

            plist = list(roots)
            for root in set(roots):
                num = plist.count(root)
                if num > 1:
                    axes.text(root.real + offset,
                              root.imag + offset, '%d' % num)

        if axes is None:
            fig, axes = subplots(1)

        axes.grid(True)
        axes.set_xlabel('Real')
        axes.set_ylabel('Imaginary')

        poles = self.poles
        axes.plot(poles.real, poles.imag, 'C0x', ms=20)
        annotate(axes, poles)

        zeros = self.zeros
        axes.plot(zeros.real, zeros.imag, 'C0o', ms=20, fillstyle='none')
        annotate(axes, zeros)

        axes.add_artist(Circle((0, 0), 1, color='blue',
                        linestyle='--', fill=False))
        a = np.hstack((poles, zeros))

        bbox = axes.get_window_extent()
        aspect = bbox.width / bbox.height
        axes.set_xlim(-1.2, 1.2)
        axes.set_ylim(-1.2, 1.2)

        # axes.axis('equal')

    def response_plot(self, n=100, mode=response_modes[0],
                      axes=None, ylim=None, **kwargs):

        if axes is None:
            fig, axes = subplots(1)

        nn, y = self.response(mode, n)

        if mode == 'Frequency response (Bode)':
            f = nn

            mlines = axes.semilogx(
                f, 20 * np.log10(abs(y)), label='magnitude (dB)')
            axes.set_xlabel('Frequency (Hz)')
            ax2 = axes.twinx()
            phase = np.arctan2(y.imag, y.real)
            phase_unwrapped = unwrap(phase)

            plines = ax2.semilogx(f, np.degrees(phase_unwrapped),
                                  '-.', label='phase (deg)', color='C1')
            lines = mlines + plines
            labels = [l.get_label() for l in lines]
            axes.legend(lines, labels)
            # ax2.set_ylim(-180, 180)
            # ax2.set_yticks((-180, -120, -60, 0, 60, 120, 180))

        elif mode == 'Frequency response':
            f = nn

            mlines = axes.plot(f, abs(y), label='magnitude')
            axes.set_xlabel('Frequency (Hz)')
            ax2 = axes.twinx()
            phase = np.arctan2(y.imag, y.real)
            phase_unwrapped = unwrap(phase)

            plines = ax2.plot(f, np.degrees(phase_unwrapped),
                              '-.', label='phase (deg)', color='C1')
            lines = mlines + plines
            labels = [l.get_label() for l in lines]
            axes.legend(lines, labels)
            # ax2.set_ylim(-180, 180)
            # ax2.set_yticks((-180, -120, -60, 0, 60, 120, 180))

        else:
            # TODO lollipop
            x = self.time_input(mode, n)

            lollipop_plot(nn, x, color='C1', label='input', axes=axes)
            lollipop_plot(nn, y, color='C0', label='output', axes=axes)
            axes.set_xlabel('Sample')
            axes.legend()

        if ylim is None:
            ylim = ylims[mode]
        axes.set_ylim(ylim)
        axes.grid(True)

    def polezero_plot_with_response(self, n=20,
                                    mode=response_modes[0], axes=None,
                                    ylim=None, **kwargs):

        if axes is None:
            fig, axes = subplots(1, 2, figsize=(12, 6))

        if isinstance(n, int):
            n = np.arange(-5, -5 + n)

        self.polezero_plot(axes[0], **kwargs)

        self.response_plot(n, mode=mode, axes=axes[1], ylim=ylim, **kwargs)

        return axes
