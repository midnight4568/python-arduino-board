# Arduino Simulator
# CSE1010 Homework 8, Fall 2018
# Kathleen Quinn
# 7 December 2018
# TA: Nila Mandal
# Lab section: 016L
# Instructor: Dr. Ahmad Jbara

class Digital:
    '''
    Defines default behaviors for 14 digital pins.
    '''
    def __init__(self):
        self._digVal = 0
        self._mode = 0

    def set_mode(self, _mode):
        '''
        Sets the mode of this instance to either 0 or 1.
        '''
        self._mode = _mode


    def read(self):
        '''
        Returns the value of the pin.
        '''
        return self._digVal

    def write(self, _val):
        '''
        Changes or keeps the value of the pin depending on pin mode.
        '''
        if self._mode == 1:
            self._digVal = _val
        else:
            pass
        
