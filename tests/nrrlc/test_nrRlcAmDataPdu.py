from unittest import TestCase
from nruplane.nrrlc.rlcamdatapdu import RlcAmDataPdu

class TestNrRlcAmDataPdu(TestCase):
    def setUp(self):
        print(' {:s} started '.format(self._testMethodName).center(50, '='))

    def tearDown(self):
        print(' {:s} ended '.format(self._testMethodName).center(50, '='))

    def test_DataPduInstance(self):
        self.iNrRlcAmDataPdu = RlcAmDataPdu(6)

        self.iNrRlcAmDataPdu = RlcAmDataPdu(12)
        self.assertEqual(self.iNrRlcAmDataPdu.SN_BIT_LENGTH, 12)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, 0)
        self.assertEqual(self.iNrRlcAmDataPdu.So, 0)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, 0)
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, bytearray())

        self.iNrRlcAmDataPdu = RlcAmDataPdu(18)
        self.assertEqual(self.iNrRlcAmDataPdu.SN_BIT_LENGTH, 18)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, 0)
        self.assertEqual(self.iNrRlcAmDataPdu.So, 0)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, 0)
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, bytearray())

        testRlcAmPdu = "0FAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(18, testRlcAmPdu)
        self.assertEqual(self.iNrRlcAmDataPdu.SN_BIT_LENGTH, 18)
        # refer to self.test_Parsing6Bit() for other test items
        self.iNrRlcAmDataPdu = RlcAmDataPdu(12, testRlcAmPdu)
        self.assertEqual(self.iNrRlcAmDataPdu.SN_BIT_LENGTH, 12)
        # refer to self.test_Parsing12Bit() for other test items

    def test_DataPduParsing12Bit(self):
        testRlcAmPdu = "8FAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(12, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 0
        expSo = 0
        expSn = 0xFAA
        self.assertEqual(self.iNrRlcAmDataPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmDataPdu.P, expP)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmDataPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, expSn)
        expData = bytearray.fromhex("BBBBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmDataPdu))

        testRlcAmPdu = "9FAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(12, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 1
        expSo = 0
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcAmDataPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmDataPdu.P, expP)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmDataPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, expSn)
        expData = bytearray.fromhex("BBBBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmDataPdu))

        testRlcAmPdu = "EFAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(12, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 2
        expSo = 0xBBBB
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcAmDataPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmDataPdu.P, expP)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmDataPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFFFF")
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmDataPdu))

        testRlcAmPdu = "FFAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(12, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 3
        expSo = 0xBBBB
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcAmDataPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmDataPdu.P, expP)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmDataPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFFFF")
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmDataPdu))


    def test_DataPduParsing18Bit(self):
        testRlcAmPdu = "8FAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 0
        expSo = 0
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmDataPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmDataPdu.P, expP)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmDataPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, expSn)
        expData = bytearray.fromhex("BBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmDataPdu))

        testRlcAmPdu = "9FAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 1
        expSo = 0x0
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmDataPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmDataPdu.P, expP)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmDataPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, expSn)
        expData = bytearray.fromhex("BBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmDataPdu))

        testRlcAmPdu = "EFAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 2
        expSo = 0xBBFF
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmDataPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmDataPdu.P, expP)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmDataPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFF")
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmDataPdu))

        testRlcAmPdu = "FFAABBBBFFFFFFFF"
        self.iNrRlcAmDataPdu = RlcAmDataPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 3
        expSo = 0xBBFF
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmDataPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmDataPdu.P, expP)
        self.assertEqual(self.iNrRlcAmDataPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmDataPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmDataPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFF")
        self.assertEqual(self.iNrRlcAmDataPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmDataPdu))
