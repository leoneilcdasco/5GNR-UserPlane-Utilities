from nruplane.nrcommon.nrpdu import NrPdu
import math


class AckParams(NrPdu):

    E1_BIT_LENGTH = 1
    E1_BIT_OFFSET = 7
    E1_BIT_MASK = 0x80

    CPT_BIT_LENGTH = 3
    CPT_BIT_OFFSET = 6
    CPT_BIT_MASK = 0x70

    P_LENGTH = 1
    P_BIT_OFFSET = 6
    P_BIT_MASK = 0x40

    SI_LENGTH = 2
    SI_BIT_OFFSET = 4
    SI_BIT_MASK = 0x30

    SO_LENGTH = 16
    SO_NUM_BYTES = 2

    # bit masks to extract the most significant bits of SN
    ACK_SN_MSB_BIT_MASK = 0x0F

    ACK_18BIT_SN_LSB_BIT_MASK = 0xFC
    ACK_18BIT_SN_LSB_BIT_OFFSET = 0xFC

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
        self.Dc = 0
        self.Cpt = 0
        self.Ack = bytearray()
        self.AckSn = 0
        self.Nacks = []
        self.NackSns = 0
        self.P = 0
        self.Si = 0
        self.Sn = 0
        self.So = 0

        if (byteStream != None):
            NrPdu.__init__(self, byteStream)
            self.initFields()

    def initFields(self):
        self.parseDc()

class RlcAmCtrlPdu(NrPdu):

    DC_BIT_LENGTH = 1
    DC_BIT_OFFSET = 7
    DC_BIT_MASK = 0x80

    CPT_BIT_LENGTH = 3
    CPT_BIT_OFFSET = 6
    CPT_BIT_MASK = 0x70

    P_LENGTH = 1
    P_BIT_OFFSET = 6
    P_BIT_MASK = 0x40

    SI_LENGTH = 2
    SI_BIT_OFFSET = 4
    SI_BIT_MASK = 0x30

    SO_LENGTH = 16
    SO_NUM_BYTES = 2

    # bit masks to extract the most significant bits of SN
    SN_MSB_MASK_12BIT = 0x0F
    SN_MSB_MASK_18BIT = 0x03

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
        self.Dc = 0
        self.Cpt = 0
        self.Ack = bytearray()
        self.AckSn = 0
        self.Nacks = []
        self.NackSns = 0
        self.P = 0
        self.Si = 0
        self.Sn = 0
        self.So = 0

        if (byteStream != None):
            NrPdu.__init__(self, byteStream)
            self.initFields()

    def evalSnLength(self, lengthSn):
        return (lengthSn != 12 and lengthSn != 18)

    def initFields(self):
        self.parseDc()
        if (self.Dc == 0b1):
            self.parseDataPdu()
        else:
            self.parseControlPdu()

    def parseDataPdu(self):
        self.parsePSi()
        self.HEADER_NUM_BYTES = self.getNumHeaderBytes()
        self.HeaderByteArray = self.PduByteArray[0:self.HEADER_NUM_BYTES]
        self.DataByteArray = self.PduByteArray[self.HEADER_NUM_BYTES:]
        self.parseSo()
        self.parseSn()

    def getNumHeaderBytes(self):
        headerBits = self.DC_BIT_LENGTH + self.P_LENGTH + self.SI_LENGTH + self.SN_LENGTH
        if self.Si > 0b01:
            headerBits += self.SO_LENGTH
        return math.ceil(headerBits / 8)

    def parseDc(self):
        self.Dc = (self.PduByteArray[0] & self.DC_BIT_MASK) >> self.DC_BIT_OFFSET

    def parseCpt(self):
        self.Cpt = (self.PduByteArray[0] & self.CPT_BIT_MASK) >> (self.CPT_BIT_OFFSET - self.CPT_BIT_LENGTH + 1)

    def parsePSi(self):
        self.P  = (self.PduByteArray[0] & self.P_BIT_MASK) >> self.P_BIT_OFFSET
        self.Si = (self.PduByteArray[0] & self.SI_BIT_MASK) >> self.SI_BIT_OFFSET

    def parseSo(self):
        if self.Si > 0b01:
            self.So = int(self.HeaderByteArray[self.HEADER_NUM_BYTES - self.SO_NUM_BYTES :].hex(), 16)

    def parseSn(self):
        tmpSnByteArray = self.HeaderByteArray[0:self.SN_NUM_BYTES]
        if self.SN_LENGTH == 18:
            tmpSnByteArray[0] = tmpSnByteArray[0] & self.SN_MSB_MASK_18BIT
        elif self.SN_LENGTH == 12:
            tmpSnByteArray[0] = tmpSnByteArray[0] & self.SN_MSB_MASK_12BIT

        self.Sn = int(tmpSnByteArray.hex(), 16)

    def parseControlPdu(self):
        print("Parse Control PDU")

    def __str__(self):
        return  '{:d}-bit SN RLC AM PDU \n'.format(self.SN_LENGTH) \
                + 'Header\t: D/C = ' + '0b{:b} '.format(self.Dc) \
                + 'P = ' + '0b{:b} '.format(self.P) \
                + 'SI = ' + '0b{:02b} '.format(self.Si) \
                + 'SN = ' + '0x{:02x} '.format(self.Sn) \
                + 'SO = ' + '0x{:02x}'.format(self.So) \
                + '\nData\t: ' + '0x{:s}'.format(self.DataByteArray.hex())


