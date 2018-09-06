from unittest import TestCase
from nruplane.nrcommon.nrcommon import nrcommon

class TestNrcommon(TestCase):

    def setUp(self):
        self.iNrCommon = nrcommon()

    def test_appendZeroIfNotByteAligned(self):
        exp = 'FF'
        act = self.iNrCommon.appendZeroIfNotByteAligned('FF')
        self.assertEqual(act, exp)

        exp = '0F'
        act = self.iNrCommon.appendZeroIfNotByteAligned('F')
        self.assertEqual(act, exp)

    def test_hexStringToByteListBigEndian(self):
        testString = "12345678"
        exp = [0x12, 0x34, 0x56, 0x78]
        act = self.iNrCommon.hexStringToByteListBigEndian(testString)
        self.assertEqual(act, exp)

        testString = "1234567"
        exp = [0x01, 0x23, 0x45, 0x67]
        act = self.iNrCommon.hexStringToByteListBigEndian(testString)
        self.assertEqual(act, exp)

    def test_hexStringToByteListLittleEndian(self):
        testString = "12345678"
        exp = list(reversed([0x12, 0x34, 0x56, 0x78]))
        act = self.iNrCommon.hexStringToByteListLittleEndian(testString)
        self.assertEqual(act, exp)

        testString = "1234567"
        exp = list(reversed([0x01, 0x23, 0x45, 0x67]))
        act = self.iNrCommon.hexStringToByteListLittleEndian(testString)
        self.assertEqual(act, exp)
