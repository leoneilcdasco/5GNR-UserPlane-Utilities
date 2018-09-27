from nruplane.nrcommon.nrpdu import NrPdu
import math

class RlcAmNack(NrPdu):

    SN_BIT_LENGTH: int
    E_BIT_LENGTH = 1

    EBITS_BYTE_INDEX_18BIT_SN: int = 2
    EBITS_BYTE_INDEX_12BIT_SN: int = 1

    SOSTART_BYTE_INDEX_18BIT_SN: int = 3
    SOEND_BYTE_INDEX_18BIT_SN: int = 5
    NACKRANGE_BYTE_INDEX_18BIT_SN: int = 7

    SOSTART_BYTE_INDEX_12BIT_SN: int = 2
    SOEND_BYTE_INDEX_12BIT_SN: int = 4
    NACKRANGE_BYTE_INDEX_12BIT_SN: int = 6

    E1_18BIT_SN_BIT_OFFSET = 5
    E1_18BIT_SN_MASK = 0x20
    E2_18BIT_SN_BIT_OFFSET = 4
    E2_18BIT_SN_MASK = 0x10
    E3_18BIT_SN_BIT_OFFSET = 3
    E3_18BIT_SN_MASK = 0x08

    E1_12BIT_SN_BIT_OFFSET = 3
    E1_12BIT_SN_MASK = 0x08
    E2_12BIT_SN_BIT_OFFSET = 2
    E2_12BIT_SN_MASK = 0x04
    E3_12BIT_SN_BIT_OFFSET = 1
    E3_12BIT_SN_MASK = 0x02

    # bit mask and offset for 18-bit SN LSB
    NACK_18BIT_SN_LSB_BIT_MASK = 0xC0
    NACK_18BIT_SN_LSB_BIT_OFFSET = 0x6

    NACK_12BIT_SN_LSB_BIT_MASK = 0xF0
    NACK_12BIT_SN_LSB_BIT_OFFSET = 0x4

    def __init__(self, lengthSn, byteStream=None):
        if (self.evalSnLength(lengthSn)):
            print("WRN : Unsupported SN Length")
            return

        NrPdu.__init__(self)

        self.SN_BIT_LENGTH = lengthSn
        self.SN_NUM_BYTES = math.ceil(self.SN_BIT_LENGTH / 8)

        self.Sn = 0
        self.E1 = 0
        self.E2 = 0
        self.E3 = 0
        self.SoStart = 0
        self.SoEnd = 0
        self.NackRange = 0

        if (byteStream != None):
            NrPdu.__init__(self, byteStream)
            self.initFields()


    def evalSnLength(self, lengthSn):
        return (lengthSn != 12 and lengthSn != 18)

    def initFields(self):
        self.parseE1()
        self.parseE2()
        self.parseE3()
        self.parseSn()

    def parseE1(self):
        if self.SN_BIT_LENGTH == 18:
            self.E1 = self.getBitField(self.PduByteArray[self.EBITS_BYTE_INDEX_18BIT_SN],
                                       self.E1_18BIT_SN_MASK,
                                       self.E1_18BIT_SN_BIT_OFFSET)
        elif self.SN_BIT_LENGTH == 12:
            self.E1 = self.getBitField(self.PduByteArray[self.EBITS_BYTE_INDEX_12BIT_SN],
                                       self.E1_12BIT_SN_MASK,
                                       self.E1_12BIT_SN_BIT_OFFSET)

    def parseE2(self):
        if self.SN_BIT_LENGTH == 18:
            self.E2 = self.getBitField(self.PduByteArray[self.EBITS_BYTE_INDEX_18BIT_SN],
                                       self.E2_18BIT_SN_MASK,
                                       self.E2_18BIT_SN_BIT_OFFSET)
        elif self.SN_BIT_LENGTH == 12:
            self.E2 = self.getBitField(self.PduByteArray[self.EBITS_BYTE_INDEX_12BIT_SN],
                                       self.E2_12BIT_SN_MASK,
                                       self.E2_12BIT_SN_BIT_OFFSET)

    def parseE3(self):
        if self.SN_BIT_LENGTH == 18:
            self.E3 = self.getBitField(self.PduByteArray[self.EBITS_BYTE_INDEX_18BIT_SN],
                                       self.E3_18BIT_SN_MASK,
                                       self.E3_18BIT_SN_BIT_OFFSET)
        elif self.SN_BIT_LENGTH == 12:
            self.E3 = self.getBitField(self.PduByteArray[self.EBITS_BYTE_INDEX_12BIT_SN],
                                       self.E3_12BIT_SN_MASK,
                                       self.E3_12BIT_SN_BIT_OFFSET)

    def parseSn(self):
        tmpSnByteArray = self.PduByteArray[0:self.SN_NUM_BYTES]

        if self.SN_BIT_LENGTH == 18:
            tmpSnByteArray[self.SN_NUM_BYTES - 1] = tmpSnByteArray[self.SN_NUM_BYTES - 1] & self.NACK_18BIT_SN_LSB_BIT_MASK
            self.Sn = (int(tmpSnByteArray.hex(), 16)) >> self.NACK_18BIT_SN_LSB_BIT_OFFSET
        elif self.SN_BIT_LENGTH == 12:
            tmpSnByteArray[self.SN_NUM_BYTES - 1] = tmpSnByteArray[self.SN_NUM_BYTES - 1] & self.NACK_12BIT_SN_LSB_BIT_MASK
            self.Sn = (int(tmpSnByteArray.hex(), 16)) >> self.NACK_12BIT_SN_LSB_BIT_OFFSET

    def parseSoStart(self):
        tmpSoStartByteArray = bytearray()
        if self.SN_BIT_LENGTH == 18:
            tmpSoStartByteArray = self.PduByteArray[self.SOSTART_BYTE_INDEX_18BIT_SN:self.SOEND_BYTE_INDEX_18BIT_SN]
        elif self.SN_BIT_LENGTH == 12:
            tmpSoStartByteArray = self.PduByteArray[self.SOSTART_BYTE_INDEX_12BIT_SN:self.SOEND_BYTE_INDEX_12BIT_SN]
        self.SoStart = int(tmpSoStartByteArray.hex(), 16)

    def parseSoEnd(self):
        tmpSoEndByteArray = bytearray()
        if self.SN_BIT_LENGTH == 18:
            tmpSoEndByteArray = self.PduByteArray[self.SOEND_BYTE_INDEX_18BIT_SN:self.NACKRANGE_BYTE_INDEX_18BIT_SN]
        elif self.SN_BIT_LENGTH == 12:
            tmpSoEndByteArray = self.PduByteArray[self.SOEND_BYTE_INDEX_12BIT_SN:self.NACKRANGE_BYTE_INDEX_12BIT_SN]
        self.SoEnd = int(tmpSoEndByteArray.hex(), 16)

    def parseNackRange(self):
        if self.SN_BIT_LENGTH == 18:
            self.NackRange = self.PduByteArray[self.NACKRANGE_BYTE_INDEX_18BIT_SN]
        elif self.SN_BIT_LENGTH == 12:
            self.NackRange = self.PduByteArray[self.NACKRANGE_BYTE_INDEX_12BIT_SN]

    def __str__(self):
        return  '{:d}-bit SN RLC AM ACK Fields \t: '.format(self.SN_BIT_LENGTH) \
                + 'E1 = ' + '0b{:b} '.format(self.E1) \
                + 'E2 = ' + '0b{:b} '.format(self.E2) \
                + 'E3 = ' + '0b{:b} '.format(self.E3) \
                + 'SN = ' + '0x{:02x} '.format(self.Sn)