from Electronics.Impulse import Impulse

Impulse
class StreamSource(Impulse):
    def __init__(self,name,type, amount,stream):
        super(StreamSource, self).__init__(type, amount)
        self.name=name
        self.stream = stream
    def __str__(self):
        return super(StreamSource, self).__str__() \
               + f"Name  {self.name}\n Stream  {self.stream}\n"