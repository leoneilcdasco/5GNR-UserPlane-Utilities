class NrCommon:
    # def __init__(self) -> object
    def __init__(self):
        self.bDebugFlag = False

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
        byteHexStream = self.appendZeroIfNotByteAligned(byteHexStream)
        byteList = list(bytearray.fromhex(byteHexStream))
        self.printDebugByteListInHex(byteList)
        return byteList

    def hexStringToByteListLittleEndian(self, byteHexStream):
        byteList = self.hexStringToByteListBigEndian(byteHexStream)
        byteList.reverse()
        self.printDebugByteListInHex(byteList)
        return byteList
