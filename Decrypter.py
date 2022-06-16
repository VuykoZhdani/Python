from os import name

from Electronics.Analog import Analog
Analog
class Decrypter(Analog):
    def __init__(self,name,type, amount):
        super(Decrypter, self).__init__(type, amount)
        self.name=name
    def __str__(self):
        return super(Decrypter, self).__str__() \
               + f"Name  {self.name}\n"



