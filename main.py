from Electronics.Analog import Analog
Analog
from Electronics.Decrypter import Decrypter
Decrypter
from Electronics.Impulse import Impulse
Impulse
from Electronics.Enhancer import Enhancer
Enhancer
from Electronics.VoltageSource import Source
Source
from Electronics.StreamSource import StreamSource
StreamSource
from Electronics.Digital import Digital
Digital
from Electronics.BinaryDecoder import BinaryDecoder
BinaryDecoder
from Electronics.DecimalDecoder import DecimalDecoder
DecimalDecoder
def main():
    decrypter=Decrypter("Analog","5","Decrypter")
    print(decrypter)
    enhancer=Enhancer("Impulse","5","Decrypter","220")
    print(enhancer)
    volatgesource=Source("Analog","10","Voltage Source","100")
    print(volatgesource)
    streamsource=StreamSource("Analog","10","Voltage Source","3000")
    print(streamsource)
    binarydecoder=BinaryDecoder("Analog","10","Voltage Source","10")
    print(binarydecoder)
    decimaldecoder = DecimalDecoder("Analog", "10", "Voltage Source", "10")
    print(decimaldecoder)
if __name__ == '__main__':
    main()