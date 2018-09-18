from nruplane.nrcommon.nrpdu import NrPdu
import math

class RlcUmPdu(NrPdu):

    SI_BIT_LENGTH = 2
    SI_BIT_OFFSET = 6
    SI_BIT_MASK = 0xC0

    SO_LENGTH = 16
    SO_NUM_BYTES = 2

    # bit masks to extract the most significant bits of SN
    SN_MSB_MASK_12BIT = 0x0F
    SN_MSB_MASK_6BIT = 0x3F

    def __init__(self, lengthSn, byteStream=None):
        if (self.evalSnLength(lengthSn)):
            print("WRN : Unsupported SN Length")
            return

        NrPdu.__init__(self)

        self.HEADER_NUM_BYTES = 0
        self.SN_LENGTH = lengthSn
        self.SN_NUM_BYTES = math.ceil(self.SN_LENGTH / 8)

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
        self.HEADER_NUM_BYTES = self.getNumHeaderBytes(self.Si)
        self.HeaderByteArray = self.PduByteArray[0:self.HEADER_NUM_BYTES]
        self.DataByteArray = self.PduByteArray[self.HEADER_NUM_BYTES:]
        self.parseSo()
        self.parseSn()

    def getNumHeaderBytes(self, Si):
        if Si == 0b00:
            headerBits = self.SI_BIT_LENGTH
        elif Si == 0b01:
            headerBits = self.SI_BIT_LENGTH + self.SN_LENGTH
        else:
            headerBits = self.SI_BIT_LENGTH + self.SO_LENGTH + self.SN_LENGTH
        return math.ceil(headerBits / 8)

    def parseSi(self):
        self.Si = (self.PduByteArray[0] & self.SI_BIT_MASK) >> self.SI_BIT_OFFSET

    def parseSo(self):
        if self.Si > 0b01:
            self.So = int(self.HeaderByteArray[self.HEADER_NUM_BYTES - self.SO_NUM_BYTES :].hex(), 16)

    def parseSn(self):
        tmpSnByteArray = bytearray()
        if self.Si > 0b00:
            if self.SN_LENGTH == 12:
                tmpSnByteArray = self.HeaderByteArray[0:self.SN_NUM_BYTES]
                tmpSnByteArray[0] = tmpSnByteArray[0] & self.SN_MSB_MASK_12BIT
            elif self.SN_LENGTH == 6:
                tmpSnByteArray.append(self.HeaderByteArray[0] & self.SN_MSB_MASK_6BIT)

            self.Sn = int(tmpSnByteArray.hex(), 16)

    def __str__(self):
        return  '{:d}-bit SN RLC UM PDU \n'.format(self.SN_LENGTH) \
                + 'Header\t: SI = ' + '0b{:02b} '.format(self.Si) \
                + 'SN = ' + '0x{:02x} '.format(self.Sn) \
                + 'SO = ' + '0x{:02x}'.format(self.So) \
                + '\nData\t: ' + '0x{:s}'.format(self.DataByteArray.hex())