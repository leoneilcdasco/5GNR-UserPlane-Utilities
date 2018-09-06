class nrpdu:
    def __init__(self, byteStream=None):
        if byteStream==None:
            self.PduByteArray = bytearray()
        else:
            if isinstance(byteStream, str):
                self.PduByteList = bytearray.fromhex(byteStream)
                print(self.PduByteList)
            else:
                print("must be string")

