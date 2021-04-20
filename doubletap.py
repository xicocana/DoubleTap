#import time
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM) # GPIO numbers instead of board numbers
#RELAYS_1_GPIO = 17
#GPIO.setup(RELAYS_1_GPIO, GPIO.OUT) # GPIO Assign mode

#while(True):
    #time.sleep(1)
    #print("OFF")
    #GPIO.output(RELAYS_1_GPIO, GPIO.LOW) # OFF
    #time.sleep(1)
    #print("ON")
    #GPIO.output(RELAYS_1_GPIO, GPIO.HIGH) # ON
    
import pyaudio
import math
import struct
import wave
import time
import os

Threshold = 10

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2

class Recorder:

    @staticmethod
    def rms(frame):
        count = len(frame) / swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  output=True,
                                  frames_per_buffer=chunk)

    def listen(self):
        print('Listening beginning')
        while True:
            input = self.stream.read(chunk)
            rms_val = self.rms(input)
            if rms_val > Threshold:
                print("hello world")

a = Recorder()

a.listen()
