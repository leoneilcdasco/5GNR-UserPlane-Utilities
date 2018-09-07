from nruplane.nrcommon.nrpdu import NrPdu
import math

class NrRlcUmPdu(NrPdu):
    SI_BIT_OFFSET = 6
    SI_LENGTH = 2
    SO_LENGTH = 16

    def __init__(self, lengthSn, byteStream=None):
        if (self.evalSnLength(lengthSn)):
            print("WRN : Unsupported SN Length")
            return

        NrPdu.__init__(self)

        self.SN_LENGTH = lengthSn
        self.NUM_HEADER_BYTES = 0
        self.HeaderByteArray = bytearray()
        self.DataByteArray = bytearray()
        self.Si = 0
        self.Sn = 0
        self.So = 0

        if (byteStream != None):
            NrPdu.__init__(self, byteStream)
            self.initFields()

    def evalSnLength(self, lengthSn):
        print(lengthSn)
        return (lengthSn != 6 and lengthSn != 12)

    def getNumHeaderBytes(self, Si):
        if Si == 0b00:
            headerBits = self.SI_LENGTH
        elif Si == 0b01:
            headerBits = self.SI_LENGTH + self.SN_LENGTH
        else:
            headerBits = self.SI_LENGTH + self.SO_LENGTH + self.SN_LENGTH

        return math.ceil(headerBits / 8)

    def initFields(self):
        self.Si = (self.PduByteArray[0] & 0xC0) >> self.SI_BIT_OFFSET
        self.NUM_HEADER_BYTES = self.getNumHeaderBytes(self.Si)
        print (self.NUM_HEADER_BYTES)
        self.HeaderByteArray = self.PduByteArray[0:self.NUM_HEADER_BYTES]
        print(self.HeaderByteArray)
        self.DataByteArray = self.PduByteArray[self.NUM_HEADER_BYTES:]
        print(self.DataByteArray)
        self.parseSo()
        print(self.So)
        self.parseSn()
        print(self.Sn)

    def parseSo(self):
        if self.Si > 0b01:
            self.So = self.HeaderByteArray[self.NUM_HEADER_BYTES - 2 :]

    def parseSn(self):
        tmpSnByteArray = bytearray()
        if self.Si > 0b00:
            if self.SN_LENGTH == 12:
                tmpSnByteArray = self.HeaderByteArray[0:1]
                tmpSnByteArray[0] = tmpSnByteArray[0] & 0x0F
            elif self.SN_LENGTH == 6:
                tmpSnByteArray.append(self.HeaderByteArray[0] & 0x3F)
            print((tmpSnByteArray.hex()))
            # self.Sn = int(hex(tmpSnByteArray), 16)

