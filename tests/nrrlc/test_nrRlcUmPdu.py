from unittest import TestCase
from nruplane.nrrlc.rlcumpdu import NrRlcUmPdu

class TestNrRlcUmPdu(TestCase):
    def setUp(self):
        print(' {:s} started '.format(self._testMethodName).center(50, '='))

    def tearDown(self):
        print(' {:s} ended '.format(self._testMethodName).center(50, '='))

    def test_NrRlcUmPduInstance(self):
        self.iNrRlcUmPdu = NrRlcUmPdu(18)

        self.iNrRlcUmPdu = NrRlcUmPdu(6)
        self.assertEqual(self.iNrRlcUmPdu.SN_LENGTH, 6)
        self.assertEqual(self.iNrRlcUmPdu.Si, 0)
        self.assertEqual(self.iNrRlcUmPdu.So, 0)
        self.assertEqual(self.iNrRlcUmPdu.Sn, 0)
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, bytearray())

        self.iNrRlcUmPdu = NrRlcUmPdu(12)
        self.assertEqual(self.iNrRlcUmPdu.SN_LENGTH, 12)
        self.assertEqual(self.iNrRlcUmPdu.Si, 0)
        self.assertEqual(self.iNrRlcUmPdu.So, 0)
        self.assertEqual(self.iNrRlcUmPdu.Sn, 0)
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, bytearray())

        testRlcUmPdu = "0FAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        self.assertEqual(self.iNrRlcUmPdu.SN_LENGTH, 6)
        # refer to self.test_Parsing6Bit() for other test items
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        self.assertEqual(self.iNrRlcUmPdu.SN_LENGTH, 12)
        # refer to self.test_Parsing12Bit() for other test items

    def test_Parsing12Bit(self):
        testRlcUmPdu = "0FAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 0
        expSo = 0
        expSn = 0
        self.assertEqual(self.iNrRlcUmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcUmPdu.So, expSo)
        self.assertEqual(self.iNrRlcUmPdu.Sn, expSn)
        expData = bytearray.fromhex("AABBBBFFFFFFFF")
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, expData)
        print(str(self.iNrRlcUmPdu))

        testRlcUmPdu = "6FAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 1
        expSo = 0
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcUmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcUmPdu.So, expSo)
        self.assertEqual(self.iNrRlcUmPdu.Sn, expSn)
        expData = bytearray.fromhex("BBBBFFFFFFFF")
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, expData)
        print(str(self.iNrRlcUmPdu))

        testRlcUmPdu = "8FAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 2
        expSo = 0xBBBB
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcUmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcUmPdu.So, expSo)
        self.assertEqual(self.iNrRlcUmPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFFFF")
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, expData)
        print(str(self.iNrRlcUmPdu))

        testRlcUmPdu = "FFAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 3
        expSo = 0xBBBB
        expSn = 0x0FAA
        self.assertEqual(self.iNrRlcUmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcUmPdu.So, expSo)
        self.assertEqual(self.iNrRlcUmPdu.Sn, expSn)
        expData = bytearray.fromhex("FFFFFFFF")
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, expData)
        print(str(self.iNrRlcUmPdu))


    def test_Parsing6Bit(self):
        testRlcUmPdu = "0FAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        expSi = 0
        expSo = 0
        expSn = 0
        self.assertEqual(self.iNrRlcUmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcUmPdu.So, expSo)
        self.assertEqual(self.iNrRlcUmPdu.Sn, expSn)
        expData = bytearray.fromhex("AABBBBFFFFFFFF")
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, expData)
        print(str(self.iNrRlcUmPdu))

        testRlcUmPdu = "6FAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        expSi = 1
        expSo = 0
        expSn = 0x2F
        self.assertEqual(self.iNrRlcUmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcUmPdu.So, expSo)
        self.assertEqual(self.iNrRlcUmPdu.Sn, expSn)
        expData = bytearray.fromhex("AABBBBFFFFFFFF")
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, expData)
        print(str(self.iNrRlcUmPdu))

        testRlcUmPdu = "8FAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        expSi = 2
        expSo = 0xAABB
        expSn = 0x0F
        self.assertEqual(self.iNrRlcUmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcUmPdu.So, expSo)
        self.assertEqual(self.iNrRlcUmPdu.Sn, expSn)
        expData = bytearray.fromhex("BBFFFFFFFF")
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, expData)
        print(str(self.iNrRlcUmPdu))

        testRlcUmPdu = "FFAABBBBFFFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        expSi = 3
        expSo = 0xAABB
        expSn = 0x3F
        self.assertEqual(self.iNrRlcUmPdu.Si, expSi)
        self.assertEqual(self.iNrRlcUmPdu.So, expSo)
        self.assertEqual(self.iNrRlcUmPdu.Sn, expSn)
        expData = bytearray.fromhex("BBFFFFFFFF")
        self.assertEqual(self.iNrRlcUmPdu.DataByteArray, expData)
        print(str(self.iNrRlcUmPdu))

