#!/usr/bin/env python
#----------------------------------------------------------------
#	Note:
#		ds18b20's data pin must be connected to pin7.
#		replace the 28-XXXXXXXXX as yours.
#----------------------------------------------------------------
import os


class Temperature:

    def __init__(self, is_celsius, ds18b20='28-0316563a9dff'):
        self.ds18b20 = ds18b20
        self.is_celsius = is_celsius
        self.setup()

    def setup(self):
        for i in os.listdir('/sys/bus/w1/devices'):
            if i != 'w1_bus_master1':
                self.ds18b20 = i


    def read(self):
        location = '/sys/bus/w1/devices/' + self.ds18b20 + '/w1_slave'
        tfile = open(location)
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = (temperature / 1000)
        if not self.is_celsius:
            temperature = temperature * 9 / 5 + 32
        self.temperature = temperature
        return temperature
    
    def destroy(self):
        pass

    def get_temperature(self):
        if self.is_celsius:
            print "Current temperature : %0.3f C" % self.read()
        else:
            print "Current temperature : %0.3f F" % self.read()
        return self.temperature
