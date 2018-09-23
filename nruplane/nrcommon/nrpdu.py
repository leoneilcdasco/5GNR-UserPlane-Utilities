class NrPdu:
    def __init__(self, byteStream=None):
        if byteStream==None:
            self.PduByteArray = bytearray()
        else:
            if isinstance(byteStream, str):
                self.PduByteArray = bytearray.fromhex(byteStream)
            else:
                if hasattr(byteStream, 'decode'):
                    self.PduByteArray = byteStream
                    print(self.PduByteArray)
                else:
                    print("argument must be hex string or bytearray")

