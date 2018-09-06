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

        self.LENGTH_SN = lengthSn
        self.NUM_HEADER_BYTES = 0

        if (byteStream != None):
            NrPdu.__init__(self, byteStream)
            self.initFields()
        else:
            NrPdu.__init__(self)
            self.initFieldsEmpty()

    def evalSnLength(self, lengthSn):
        return lengthSn != 6 and lengthSn != 12

    def initFieldsEmpty(self):
        self.HeaderByteArray = bytearray()
        self.DataByteArray = bytearray()
        self.Si = 0
        self.Sn = 0
        self.So = 0

    def getNumHeaderBytes(self, Si):
        headerBits = self.SI_LENGTH + self.SO_LENGTH + self.LENGTH_SN if (Si != 0) else self.SI_LENGTH + self.LENGTH_SN
        return math.ceil(headerBits / 8)

    def initFields(self):
        self.Si = (self.PduByteArray[0] & 0xC0) >> self.SI_BIT_OFFSET
        self.NUM_HEADER_BYTES = self.getNumHeaderBytes(self.Si)
