from os import name
from Electronics.Impulse import Impulse

Impulse


class Enhancer(Impulse):
    def __init__(self, name, volts, type, amount):
        super(Enhancer, self).__init__(type, amount)
        self.volts = volts
        self.name = name
    def __str__(self):
        return super(Enhancer, self).__str__() \
               + f"Voltage  {self.volts}\n " \
               + f"Name  {self.name}\n"
