from unittest import TestCase
from nruplane.nrrlc.rlcamctrlpdu import RlcAmCtrlPdu

class TestNrRlcAmCtrlPdu(TestCase):
    def setUp(self):
        print(' {:s} started '.format(self._testMethodName).center(50, '='))

    def tearDown(self):
        print(' {:s} ended '.format(self._testMethodName).center(50, '='))

    def test_CtrlPduInstance(self):
        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(6)

        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(12)
        self.assertEqual(self.iNrRlcAmCtrlPdu.SN_LENGTH, 12)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Si, 0)
        self.assertEqual(self.iNrRlcAmCtrlPdu.So, 0)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Sn, 0)
        self.assertEqual(self.iNrRlcAmCtrlPdu.DataByteArray, bytearray())

        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(18)
        self.assertEqual(self.iNrRlcAmCtrlPdu.SN_LENGTH, 18)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Si, 0)
        self.assertEqual(self.iNrRlcAmCtrlPdu.So, 0)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Sn, 0)
        self.assertEqual(self.iNrRlcAmCtrlPdu.DataByteArray, bytearray())

        testRlcAmPdu = "0FAABBBBFFFFFFFF"
        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(18, testRlcAmPdu)
        self.assertEqual(self.iNrRlcAmCtrlPdu.SN_LENGTH, 18)
        # refer to self.test_Parsing6Bit() for other test items
        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(12, testRlcAmPdu)
        self.assertEqual(self.iNrRlcAmCtrlPdu.SN_LENGTH, 12)
        # refer to self.test_Parsing12Bit() for other test items

    def test_CtrlPduParsing12Bit(self):
        testRlcAmPdu = "0FAABBBBFFFFFFFF"
        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(12, testRlcAmPdu)
        expDc = 0
        expP  = 0
        expSi = 0
        expSo = 0
        expSn = 0xFAA
        #self.assertEqual(self.iNrRlcAmCtrlPdu.Dc, expDc)
        #self.assertEqual(self.iNrRlcAmCtrlPdu.P, expP)
        #self.assertEqual(self.iNrRlcAmCtrlPdu.Si, expSi)
        #self.assertEqual(self.iNrRlcAmCtrlPdu.So, expSo)
        #self.assertEqual(self.iNrRlcAmCtrlPdu.Sn, expSn)
        #expData = bytearray.fromhex("BBBBFFFFFFFF")
        #self.assertEqual(self.iNrRlcAmCtrlPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmCtrlPdu))



    def test_CtrlPduParsing18Bit(self):
        testRlcAmPdu = "8FAABBBBFFFFFFFF"
        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 0
        expSo = 0
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmCtrlPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmCtrlPdu.P, expP)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmCtrlPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Sn, expSn)
        expData = bytearray.fromhex("BBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmCtrlPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmCtrlPdu))

        testRlcAmPdu = "9FAABBBBFFFFFFFF"
        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 0
        expSi = 1
        expSo = 0x0
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmCtrlPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmCtrlPdu.P, expP)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmCtrlPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Sn, expSn)
        expData = bytearray.fromhex("BBFFFFFFFF")
        self.assertEqual(self.iNrRlcAmCtrlPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmCtrlPdu))

        testRlcAmPdu = "EFAABBBBFFFFFFFF"
        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 2
        expSo = 0xBBFF
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmCtrlPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmCtrlPdu.P, expP)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmCtrlPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFF")
        self.assertEqual(self.iNrRlcAmCtrlPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmCtrlPdu))

        testRlcAmPdu = "FFAABBBBFFFFFFFF"
        self.iNrRlcAmCtrlPdu = RlcAmCtrlPdu(18, testRlcAmPdu)
        expDc = 1
        expP  = 1
        expSi = 3
        expSo = 0xBBFF
        expSn = 0x3AABB
        self.assertEqual(self.iNrRlcAmCtrlPdu.Dc, expDc)
        self.assertEqual(self.iNrRlcAmCtrlPdu.P, expP)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Si, expSi)
        self.assertEqual(self.iNrRlcAmCtrlPdu.So, expSo)
        self.assertEqual(self.iNrRlcAmCtrlPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFF")
        self.assertEqual(self.iNrRlcAmCtrlPdu.DataByteArray, expData)
        print(str(self.iNrRlcAmCtrlPdu))
