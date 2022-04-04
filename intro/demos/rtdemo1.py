import sk_dsp_comm.sigsys as ss
import sk_dsp_comm.pyaudio_helper as pah
import sk_dsp_comm.fir_design_helper as fir_d
import scipy.signal as signal
import ipywidgets as widgets
from IPython.display import Audio, display
import numpy as np

# define a pass through, y = x, callback


def callback(in_data, frame_count, time_info, status):
    global DSP_IO
    global Gain
    DSP_IO.DSP_callback_tic()
    # convert byte data to ndarray
    in_data_nda = np.frombuffer(in_data, dtype=np.int16)

    x = in_data_nda.astype(np.float32)
    y = Gain.value * x

    y = y.astype(np.int16)
    DSP_IO.DSP_callback_toc()
    # Convert ndarray back to bytes
    # return (in_data_nda.tobytes(), pyaudio.paContinue)
    return y.tobytes(), pah.pyaudio.paContinue


DSP_IO = pah.DSP_io_stream(callback, in_idx=0, out_idx=0, fs=48000, Tcapture=0)


def rtdemo1():
    Gain = widgets.FloatSlider(description='Gain',
                               continuous_update=True,
                               value=0.2,
                               min=0.0,
                               max=2.0,
                               step=0.01,
                               orientation='vertical')

    DSP_IO.interactive_stream(Tsec=0, numChan=1)
