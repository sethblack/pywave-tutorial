"""
copyright 2014 Seth Black
www.sethserver.com
"""

import wave
import struct
import random
import math

# the notes we want to play
scale = [ 261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370, 392, 415.3, 440, 466.2, 493.9, 523.3, ]

if __name__ == '__main__':

    # the raw sample data will live here
    samples = []

    # sample rate of 44.1k is perfect for my ears
    sample_rate = 44100

    # how many seconds do we want to record
    # for now, just play each note for one second
    duration = len(scale) * sample_rate

    # float between 0 and 100 if you go bigger than 100 it'll break >:[
    # this will be normalized later
    volume = 90

    # stepper
    for i in range(0, duration):

            # grab the nth note in our scale
            note = scale[int(i / sample_rate)]

            # calculate the sample (or frame)
            amplitude = 32768 * float(volume) / 100
            frequency = math.sin(2 * math.pi * float(note) * (float(i) / sample_rate))
            sample = amplitude * frequency

            # if you want more tones...like to create a triad
            # just generate the next sample, clip it and the current sample
            # and finally add the two samples together

            #amplitude = 32768 * float(volume) / 100
            #frequency = math.sin(2 * math.pi * float(261.6) * (float(i) / sample_rate))
            #sample1 = amplitude * frequency
            #sample = (sample * .5) + (sample1 * .5)

            # just for visualization purposes, it's always fun
            # to plot waves
            print "%f %f %f %f" % (note, amplitude, frequency, sample)

            # grow our little array of samples
            samples.append(struct.pack('h', sample))

    # the file we want to spit out
    output = wave.open('tone.wav', 'w')

    # mono, 16-bit, 44.1k, empty file with no frills :)
    # don't worry about the 0-length file, writeframes will fix that for us
    output.setparams((1, 2, sample_rate, 0, 'NONE', 'not compressed'))

    # write our samples to the file
    output.writeframes(''.join(samples))

    # done, so clean up
    output.close()
