# Arduino Simulator
# CSE1010 Homework 8, Fall 2018
# Kathleen Quinn
# 7 December 2018
# TA: Nila Mandal
# Lab section: 016L
# Instructor: Dr. Ahmad Jbara

from analog import Analog
from digital import Digital
import time

class ArduinoSim:
    '''
    Contains the variables and methods that represent an instance of an Arduino.
    '''

    _numAnalogs = 6
    _numDigitals = 14
    
    def __init__(self):
        self._digitalPins = []
        self._analogPins = []
        for i in range(0, ArduinoSim._numDigitals):
            digPin = Digital()
            self._digitalPins.append(digPin)
        for i in range(0, ArduinoSim._numAnalogs):
            anPin = Analog()
            self._analogPins.append(anPin)

    def ar(self, _pinNum):
        '''
        Returns the read value of the corresponding Analog instance, but only if the pin number is within the allowable range.
        '''
        try:
            readVal = self._analogPins[_pinNum].read()
        except IndexError:
            pass
        if 0 <= _pinNum and _pinNum < ArduinoSim._numAnalogs:
            return readVal
        
    def dr(self, _pinNum):
        '''
        Returns the read value of the corresponding Digital instance, but only if the pin number is within the allowable range.
        '''
        try:
            readVal = self._digitalPins[_pinNum].read()
        except IndexError:
            pass
        if 0 <= _pinNum and _pinNum < ArduinoSim._numDigitals:
            return readVal
        else:  # pin out of range
            return None

    def aw(self, _pinNum, _val):
        '''
        Writes the value to the corresponding analog pin instance only if the pin number is in the correct range.
        '''
        if 0 <= _pinNum <= (ArduinoSim._numAnalogs - 1):
            self._analogPins[_pinNum].write(_val)

    def dw(self, _pinNum, _val):
        '''
        Writes the value to the corresponding digital pin instance only if the pin number is in the correct range.
        If _val is not 0 or 1 no write occurs.
        '''
        if (0 <= _pinNum <= (ArduinoSim._numDigitals - 1)
              and _val in [0,1]):
            self._digitalPins[_pinNum].write(_val)
            if _pinNum == 13:
                if self.dr(13) == 1:
                    print("LED is on")
                else:
                    print("LED is off")

    def dm(self, _pinNum, _modeVal):
        '''
        Sets the mode of the pin to the parameter variable.
        '''
        if 0 <= _pinNum and _pinNum < ArduinoSim._numDigitals:
            pin = self._digitalPins[_pinNum]
            pin.set_mode(_modeVal)

def blink(arduino):
    '''
    Acts just like the Arduino blink program.
    '''
    arduino.dm(13, 1)
    for i in range(5):
        arduino.dw(13, 1)
        time.sleep(1)
        arduino.dw(13, 0)
        time.sleep(1)

import threading
def start_potentiometer(arduino):
    def run():
        delay = 0.002
        while True:
            # count up from 0 to 1023
            for n in range(1024):
                # you may need to use a variable name other than
                # _analogs, depending on what you called it
                arduino._analogPins[0].set_value(n)
                time.sleep(delay)
            # count down from 1023 to 0
            for n in range(1023, -1, -1):
                arduino._analogPins[0].set_value(n)
                time.sleep(delay)
    thread = threading.Thread(target=run)
    thread.start()

def main():
    ard = ArduinoSim()
    start_potentiometer(ard)
    for n in range(10):
        print(n, ':', ard.ar(0))
        time.sleep(1)
