from unittest import TestCase
from nruplane.nrcommon.nrpdu import NrPdu


class TestNrpdu(TestCase):

    def setUp(self):
        print(' {:s} started '.format(self._testMethodName).center(50, '='))
        self.iNrpdu = NrPdu()

    def tearDown(self):
        print(' {:s} ended '.format(self._testMethodName).center(50, '='))

    def test_NrPduInstance(self):
        self.iNrpdu = NrPdu('abcd')
        self.iNrpdu = NrPdu('0bcd')

        tmp = bytearray.fromhex('0bcd')
        self.iNrpdu = NrPdu(tmp)
        self.iNrPdu = NrPdu(0xF78787878787)