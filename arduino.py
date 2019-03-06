#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess 
import RPi.GPIO as GPIO
import time
#import espeak
#import commands
from nanpy import ArduinoApi
from nanpy import SerialManager
#def espeak(string):
 #   output = 'espeak "%s" ' % string
#a = commands.getoutput(output)
connection=SerialManager(device='/dev/ttyACM0')
a = ArduinoApi(connection=connection)
bulb = 10
a.pinMode(bulb,a.OUTPUT)

def bulb50():
    connection=SerialManager(device='/dev/ttyACM0')
    a = ArduinoApi(connection=connection)
    bulb = 10
    a.pinMode(bulb,a.OUTPUT)
for i in range(0,200):
      a.analogWrite(bulb,100)
