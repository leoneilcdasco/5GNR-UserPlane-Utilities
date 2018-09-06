from unittest import TestCase
from nruplane.nrcommon.nrpdu import NrPdu


class TestNrpdu(TestCase):
    def setUp(self):
        self.iNrpdu = NrPdu()

    def test_Instance(self):
        self.iNrpdu = NrPdu('abcd')
        self.iNrpdu = NrPdu('0bcd')