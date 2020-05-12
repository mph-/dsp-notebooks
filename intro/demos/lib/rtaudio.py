import time
import numpy as np
from pyaudio import PyAudio, paContinue, paInt16
from threading import Thread


class RTAudio(object):

    def __init__(self, input_device_index, output_device_index, fs=48000, frame_length=1024,
                 channels=1, callback=None):
        self.input_device_index = input_device_index
        self.output_device_index = output_device_index
        self.fs = fs
        self.stream_callback = callback
        self.p = PyAudio()
        self.frame_length = frame_length
        self.channels = channels
        self.dostop = False
        self.sleeptime = 0.1
        self.frames = 0
        
    def run(self):

        self.stream_start()

        if False:
            self.stream_run()
        else:
            t = Thread(target=self.stream_run)
            t.start()

    def stop(self):
        self.do_stop = True        

    def _callback(self, in_data, frame_count, time_info, status):        

        self.frames += 1

        in_data = np.frombuffer(in_data, dtype=np.int16)
        in_data = in_data.astype(np.float32) / 32767
        
        out_data = self(in_data) * 32767
        
        out_data = out_data.astype(np.int16)
        return out_data.tobytes(), paContinue

    def stream_start(self):

        self.stream = self.p.open(format=paInt16, channels=self.channels,
                                  rate=self.fs, input=True, output=True,
                                  input_device_index=self.input_device_index,
                                  output_device_index=self.output_device_index,
                                  frames_per_buffer=self.frame_length,
                                  stream_callback=self._callback)

        self.stream.start_stream()

    def stream_run(self):
        
        self.do_stop = False
        while self.stream.is_active() and not self.do_stop:
            time.sleep(self.sleeptime)

        self.stream_stop()


    def stream_stop(self):
            
        self.stream.stop_stream()
        self.stream.close()

        #self.p.terminate()
        
    def devices(self):

        devices = []
        for m in range(self.p.get_device_count()):
            dev = self.p.get_device_info_by_index(m)
            
            devices.append({'name': dev['name'], 'inputs': dev['maxInputChannels'], 'outputs': dev['maxOutputChannels']})
        return devices
    
