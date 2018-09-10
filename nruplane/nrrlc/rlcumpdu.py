from nruplane.nrcommon.nrpdu import NrPdu
import math

class NrRlcUmPdu(NrPdu):

    SI_LENGTH = 2
    SI_BIT_OFFSET = 6
    SI_MASK = 0xC0

    SO_LENGTH = 16

    # bit masks to extract the most significant bits of SN
    SN_MSB_MASK_12BIT = 0x0F
    SN_MSB_MASK_6BIT = 0x3F

    def __init__(self, lengthSn, byteStream=None):
        if (self.evalSnLength(lengthSn)):
            print("WRN : Unsupported SN Length")
            return

        NrPdu.__init__(self)

        self.SN_LENGTH = lengthSn
        self.NUM_HEADER_BYTES = 0
        self.NUM_SN_BYTES = math.ceil(lengthSn / 8)
        self.HeaderByteArray = bytearray()
        self.DataByteArray = bytearray()
        self.Si = 0
        self.Sn = 0
        self.So = 0

        if (byteStream != None):
            NrPdu.__init__(self, byteStream)
            self.initFields()

    def evalSnLength(self, lengthSn):
        return (lengthSn != 6 and lengthSn != 12)

    def initFields(self):
        self.parseSi()
        self.NUM_HEADER_BYTES = self.getNumHeaderBytes(self.Si)
        self.HeaderByteArray = self.PduByteArray[0:self.NUM_HEADER_BYTES]
        self.DataByteArray = self.PduByteArray[self.NUM_HEADER_BYTES:]
        self.parseSo()
        self.parseSn()

    def getNumHeaderBytes(self, Si):
        if Si == 0b00:
            headerBits = self.SI_LENGTH
        elif Si == 0b01:
            headerBits = self.SI_LENGTH + self.SN_LENGTH
        else:
            headerBits = self.SI_LENGTH + self.SO_LENGTH + self.SN_LENGTH
        return math.ceil(headerBits / 8)

    def parseSi(self):
        self.Si = (self.PduByteArray[0] & self.SI_MASK) >> self.SI_BIT_OFFSET

    def parseSo(self):
        tmpSoByteArray = bytearray()
        if self.Si > 0b01:
            tmpSoByteArray = self.HeaderByteArray[self.NUM_HEADER_BYTES - 2 :]
            self.So = int(tmpSoByteArray.hex(), 16)

    def parseSn(self):
        tmpSnByteArray = bytearray()
        if self.Si > 0b00:
            if self.SN_LENGTH == 12:
                tmpSnByteArray = self.HeaderByteArray[0:self.NUM_SN_BYTES]
                tmpSnByteArray[0] = tmpSnByteArray[0] & self.SN_MSB_MASK_12BIT
            elif self.SN_LENGTH == 6:
                tmpSnByteArray.append(self.HeaderByteArray[0] & self.SN_MSB_MASK_6BIT)

            self.Sn = int(tmpSnByteArray.hex(), 16)

    def __str__(self):
        return  '{:d}-bit SN RLC UM PDU \n'.format(self.SN_LENGTH) \
                + 'Header\t: SI = ' + '0b{:02b} '.format(self.Si) \
                + 'SN = ' + '0x{:02x} '.format(self.Sn) \
                + 'SO = ' + '0x{:02x}'.format(self.So) \
                + '\nData\t: ' + '{:s}'.format(self.DataByteArray.hex())