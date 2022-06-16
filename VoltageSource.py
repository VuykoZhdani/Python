from Electronics.Analog import Analog
Analog
class Source(Analog):
    def __init__(self,name,type, amount,capacity):
        super(Source, self).__init__(type, amount)
        self.name=name
        self.capacity = capacity
    def __str__(self):
        return super(Source, self).__str__() \
               + f"Name  {self.name}\n Capacity  {self.capacity}\n"