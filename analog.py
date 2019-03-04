# Arduino Simulator
# CSE1010 Homework 8, Fall 2018
# Kathleen Quinn
# 7 December 2018
# TA: Nila Mandal
# Lab section: 016L
# Instructor: Dr. Ahmad Jbara

import random

class Analog:
    '''
    Represents an analog pin for the Arduino.
    '''
    def __init__(self):
        self._value = 0
        self._mode = 'read'
        for n in range(16):
            self._value += random.randint(0, 63)

    def read(self):
        '''
        Returns the value of this analog pin.
        '''
        return self._value
    
    def write(self, _value):
        '''
        Changes the argument value to 0 or 255.
        '''
        if self._value < 0:
            self._value = 0
        elif self._value > 255:
            self._value = 255
        self._value = _value / .25

    def set_value(self, _value):
        '''
        Accepts a value from 0 to 1023 and sets the analog pin's value to that number.
        '''
        self._value = _value
        if self._value < 0:
            self._value = 0
        elif self._value > 1023:
            self._value = 1023
