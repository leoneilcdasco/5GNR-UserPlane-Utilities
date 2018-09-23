from nruplane.nrcommon.nrpdu import NrPdu
import math

class RlcAmAck(NrPdu):

    ACK_PARAM_BYTES = 3

    SN_BIT_LENGTH: int
    E1_BIT_LENGTH = 1

    E1_18BIT_SN_BIT_OFFSET = 1
    E1_18BIT_SN_MASK = 0x02
    E1_12BIT_SN_BIT_OFFSET = 7
    E1_12BIT_SN_MASK = 0x80

    # bit mask for SN MSB
    # same for 12-bit and 18-bit SN
    ACK_SN_MSB_BIT_MASK = 0x0F

    # bit mask and offset for 18-bit SN LSB
    ACK_18BIT_SN_LSB_BIT_MASK = 0xFC
    ACK_18BIT_SN_LSB_BIT_OFFSET = 0x2

    def __init__(self, lengthSn, byteStream=None):
        if (self.evalSnLength(lengthSn)):
            print("WRN : Unsupported SN Length")
            return

        NrPdu.__init__(self)

        self.SN_BIT_LENGTH = lengthSn
        self.SN_NUM_BYTES = math.ceil(self.SN_BIT_LENGTH / 8)

        self.Sn = 0
        self.E1 = 0

        if (byteStream != None):
            NrPdu.__init__(self, byteStream)
            if (len(self.PduByteArray) != self.ACK_PARAM_BYTES):
                print("WRN : Incorrect Length for ACK Parameter bytearray")
            else:
                self.initFields()


    def evalSnLength(self, lengthSn):
        return (lengthSn != 12 and lengthSn != 18)

    def initFields(self):
        self.parseE1()
        self.parseSn()

    def parseE1(self):
        print(hex(self.PduByteArray[self.ACK_PARAM_BYTES - 1]))
        print(hex(self.PduByteArray[self.ACK_PARAM_BYTES - 1] & self.E1_18BIT_SN_MASK))

        if self.SN_BIT_LENGTH == 18:
            self.E1 = (self.PduByteArray[self.ACK_PARAM_BYTES - 1] & self.E1_18BIT_SN_MASK) >> self.E1_18BIT_SN_BIT_OFFSET
        elif self.SN_BIT_LENGTH == 12:
            self.E1 = (self.PduByteArray[self.ACK_PARAM_BYTES - 1] & self.E1_12BIT_SN_MASK) >> self.E1_12BIT_SN_BIT_OFFSET

    def parseSn(self):
        tmpSnByteArray = self.PduByteArray[0:self.SN_NUM_BYTES]
        tmpSnByteArray[0] = tmpSnByteArray[0] & self.ACK_SN_MSB_BIT_MASK

        if self.SN_BIT_LENGTH == 18:
            tmpSnByteArray[self.SN_NUM_BYTES - 1] = tmpSnByteArray[self.SN_NUM_BYTES - 1] & self.ACK_18BIT_SN_LSB_BIT_MASK
            self.Sn = (int(tmpSnByteArray.hex(), 16)) >> self.ACK_18BIT_SN_LSB_BIT_OFFSET
        elif self.SN_BIT_LENGTH == 12:
            self.Sn = int(tmpSnByteArray.hex(), 16)

    def __str__(self):
        return  '{:d}-bit SN RLC AM ACK Fields \t: '.format(self.SN_BIT_LENGTH) \
                + 'E1 = ' + '0b{:b} '.format(self.E1) \
                + 'SN = ' + '0x{:02x} '.format(self.Sn)