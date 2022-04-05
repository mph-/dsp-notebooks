# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact
from .lib.signal_plot import signal_plot, create_axes
from .lib.flickernoise import FlickerNoise
from IPython.display import Audio


colours = ['red', 'pink', 'white', 'blue', 'violet']
betas = {'red': 2, 'pink': 1, 'white': 0, 'blue': -1, 'violet': -2}


def noise_colour_audio_plot(colour='white'):

    lollipop = False
    ASD = True
    seed = 42
    np.random.seed(seed)

    B = 10e3
    fs = 2 * B

    T = 5
    N = int(fs * T)
    t = np.arange(N) / fs

    beta = betas[colour]
    noise = FlickerNoise(N, fs, beta=beta, alpha=1, N0=1e-40)

    t = np.arange(N) / fs
    x = noise.realisation()

    if ASD:
        f = np.logspace(1, 4, 201)
        Sx = 1 / f**beta

        axes, tmp = create_axes(2)

        axes[0].loglog(f, Sx)
        axes[0].set_ylabel('Voltage ASD (V/rtHz)')
        axes[0].set_xlabel('Frequency (Hz)')

        ax = axes[1]
        signal_plot(t, x * 1e6, lollipop=lollipop, axes=ax)

    else:
        m = range(0, 51)
        fig = signal_plot(t[m], x[m] * 1e6, lollipop=lollipop)
        ax = fig.axes[0]

    # ax.set_ylim(-1, 1)
    # ax.set_ylabel('Voltage (uV)')

    xn = x / max(abs(x))
    audio = Audio(xn, rate=fs, embed=True)
    return audio


def noise_colour_audio_demo1():
    interact(noise_colour_audio_plot,
             colour=colours,
             continuous_update=False)
