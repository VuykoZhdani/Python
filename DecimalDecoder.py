from Electronics.Digital import Digital

Digital


class DecimalDecoder(Digital):
    def __init__(self, name, type, energy, amount):
        super(DecimalDecoder, self).__init__(type, amount)
        self.name = name
        self.energy = energy

    def __str__(self):
        return super(DecimalDecoder, self).__str__() \
               + f"Name  {self.name}\n Name  {self.energy}"
