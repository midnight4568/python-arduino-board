# Arduino Simulator
# CSE1010 Homework 8, Fall 2018
# Kathleen Quinn
# 7 December 2018
# TA: Nila Mandal
# Lab section: 016L
# Instructor: Dr. Ahmad Jbara


class Widget:

    def __init__(self, n):
        self.n = n
        print('Set n to', n)

    def f(self):
        print('My value is', self.n)
        
    def who(self):
        print('The receiver is', self)
