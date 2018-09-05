
class nrcommon:
    # def __init__(self) -> object
    def __init__(self):
        self.bDebugFlag = True

    def printDebug(self, printArg):
        if (self.bDebugFlag):
            print(printArg)

    def printDebugByteListInHex(self, byteList):
        if (self.bDebugFlag):
            self.prinByteListInHex(byteList)

    def flagWarning(self, id, message):
        print("WARNING!!!", id, ":", message)

    def appendZeroIfNotByteAligned(self, byteHexStream):
        if (len(byteHexStream) % 2 == 0):
            return byteHexStream
        else:
            self.flagWarning("WRN_000", "Hex byte stream string not byte aligned! Appended '0' to align byte stream.")
            return "0" + byteHexStream

    def prinByteListInHex(self, byteList):
        print ('[{}]'.format(', '.join(hex(byte) for byte in byteList)))

    def hexStringToByteListBigEndian(self, byteHexStream):
        self.printDebug(len(byteHexStream))
        byteHexStream = self.appendZeroIfNotByteAligned(byteHexStream)
        byteList = []
        numCharPerByte = 2
        for i in range(0, len(byteHexStream), numCharPerByte):
            self.printDebug('0x{:02x}'.format(int(byteHexStream[i:i + numCharPerByte], 16)))
            byteList.append(int(byteHexStream[i:i + numCharPerByte], 16))
        self.printDebugByteListInHex(byteList)
        return byteList

    def hexStringToByteListLittleEndian(self, byteHexStream):
        self.printDebug(len(byteHexStream))
        byteHexStream = self.appendZeroIfNotByteAligned(byteHexStream)
        byteList = []
        numCharPerByte = 2
        for i in range(len(byteHexStream) - 1, 0, -numCharPerByte):
            self.printDebug('0x{:02x}'.format(int(byteHexStream[i - 1:i - 1 + numCharPerByte], 16)))
            byteList.append(int(byteHexStream[i - 1:i - 1 + numCharPerByte], 16))
        self.printDebugByteListInHex(byteList)
        return byteList