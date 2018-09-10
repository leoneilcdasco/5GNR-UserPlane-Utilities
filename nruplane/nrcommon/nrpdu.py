class NrPdu:
    def __init__(self, byteStream=None):
        if byteStream==None:
            self.PduByteArray = bytearray()
        else:
            if isinstance(byteStream, str):
                self.PduByteArray = bytearray.fromhex(byteStream)
            else:
                print("must be string")

