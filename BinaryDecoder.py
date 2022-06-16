from Electronics.Digital import Digital

Digital


class BinaryDecoder(Digital):
    def __init__(self, name, type, timing, amount):
        super(BinaryDecoder, self).__init__(type, amount)
        self.name = name
        self.timing = timing

    def __str__(self):
        return super(BinaryDecoder, self).__str__() \
               + f"Name  {self.name}\n Name  {self.timing}"
