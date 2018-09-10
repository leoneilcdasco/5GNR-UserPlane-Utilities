from unittest import TestCase
from nruplane.nrrlc.rlcampdu import NrRlcAmPdu

class TestNrRlcAmPdu(TestCase):
    def setUp(self):
        print(' {:s} started '.format(self._testMethodName).center(50, '='))

    def tearDown(self):
        print(' {:s} ended '.format(self._testMethodName).center(50, '='))

    def test_NrRlcAmPduInstance(self):
        self.iNrRlcAmPdu = NrRlcAmPdu(6)

        self.iNrRlcAmPdu = NrRlcAmPdu(12)
        self.assertEqual(self.iNrRlcAmPdu.SN_LENGTH, 12)
        self.assertEqual(self.iNrRlcAmPdu.Si, 0)
        self.assertEqual(self.iNrRlcAmPdu.So, 0)
        self.assertEqual(self.iNrRlcAmPdu.Sn, 0)
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, bytearray())

        self.iNrRlcAmPdu = NrRlcAmPdu(18)
        self.assertEqual(self.iNrRlcAmPdu.SN_LENGTH, 18)
        self.assertEqual(self.iNrRlcAmPdu.Si, 0)
        self.assertEqual(self.iNrRlcAmPdu.So, 0)
        self.assertEqual(self.iNrRlcAmPdu.Sn, 0)
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, bytearray())

        testRlcAmPdu = "0FAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(18, testRlcAmPdu)
        self.assertEqual(self.iNrRlcAmPdu.SN_LENGTH, 18)
        # refer to self.test_Parsing6Bit() for other test items
        self.iNrRlcAmPdu = NrRlcAmPdu(12, testRlcAmPdu)
        self.assertEqual(self.iNrRlcAmPdu.SN_LENGTH, 12)
        # refer to self.test_Parsing12Bit() for other test items

    def test_Parsing12Bit(self):
        testRlcAmPdu = "8FAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(12, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 0
        expSo = 0
        expSn = 0xFAA
        self.assertEqual(self.iNrRlcAmPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmPdu.P, expP)
        self.assertEqual(self.iNrRlcAmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmPdu.Sn, expSn)
        expData = bytearray.fromhex("BBBBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmPdu))

        testRlcAmPdu = "9FAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(12, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 1
        expSo = 0
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcAmPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmPdu.P, expP)
        self.assertEqual(self.iNrRlcAmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmPdu.Sn, expSn)
        expData = bytearray.fromhex("BBBBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmPdu))

        testRlcAmPdu = "EFAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(12, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 2
        expSo = 0xBBBB
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcAmPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmPdu.P, expP)
        self.assertEqual(self.iNrRlcAmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFFFF")
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmPdu))

        testRlcAmPdu = "FFAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(12, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 3
        expSo = 0xBBBB
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcAmPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmPdu.P, expP)
        self.assertEqual(self.iNrRlcAmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFFFF")
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmPdu))


    def test_Parsing18Bit(self):
        testRlcAmPdu = "8FAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 0
        expSo = 0
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmPdu.P, expP)
        self.assertEqual(self.iNrRlcAmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmPdu.Sn, expSn)
        expData = bytearray.fromhex("BBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmPdu))

        testRlcAmPdu = "9FAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 1
        expSo = 0x0
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmPdu.P, expP)
        self.assertEqual(self.iNrRlcAmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmPdu.Sn, expSn)
        expData = bytearray.fromhex("BBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmPdu))

        testRlcAmPdu = "EFAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 2
        expSo = 0xBBFF
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmPdu.P, expP)
        self.assertEqual(self.iNrRlcAmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFF")
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmPdu))

        testRlcAmPdu = "FFAABBBBFFFFFFFF"
        self.iNrRlcAmPdu = NrRlcAmPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 3
        expSo = 0xBBFF
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmPdu.P, expP)
        self.assertEqual(self.iNrRlcAmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFF")
        self.assertEqual(self.iNrRlcAmPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmPdu))
