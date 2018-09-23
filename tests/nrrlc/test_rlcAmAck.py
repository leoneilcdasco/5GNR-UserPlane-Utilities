from unittest import TestCase
from nruplane.nrrlc.rlcamack import RlcAmAck

class TestRlcAmAck(TestCase):
    def setUp(self):
        print(' {:s} started '.format(self._testMethodName).center(50, '='))

    def tearDown(self):
        print(' {:s} ended '.format(self._testMethodName).center(50, '='))

    def test_AckInstance(self):
        self.iNrRlcAck = RlcAmAck(6)

        self.iNrRlcAck = RlcAmAck(12)
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 12)
        self.assertEqual(self.iNrRlcAck.E1, 0)
        self.assertEqual(self.iNrRlcAck.Sn, 0)
        print(str(self.iNrRlcAck))

        self.iNrRlcAck = RlcAmAck(18)
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 18)
        self.assertEqual(self.iNrRlcAck.E1, 0)
        self.assertEqual(self.iNrRlcAck.Sn, 0)
        print(str(self.iNrRlcAck))

        # Invalid Length
        testRlcAmPdu = "0FAABBBBFFFFFFFF"

        self.iNrRlcAck = RlcAmAck(18, testRlcAmPdu)
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 18)
        self.assertEqual(self.iNrRlcAck.E1, 0)
        self.assertEqual(self.iNrRlcAck.Sn, 0)
        print(str(self.iNrRlcAck))
        # refer to self.test_AckParsing18Bit() for parsing test items

        self.iNrRlcAck = RlcAmAck(12, testRlcAmPdu)
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 12)
        self.assertEqual(self.iNrRlcAck.E1, 0)
        self.assertEqual(self.iNrRlcAck.Sn, 0)
        print(str(self.iNrRlcAck))
        # refer to self.test_AckParsing12Bit() for parsing test items

    def test_AckParsing12Bit(self):
        testRlcAmPdu = "8FAABB"
        self.iNrRlcAck = RlcAmAck(12, testRlcAmPdu)
        expE1 = 1
        expSn = 0xFAA
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 12)
        self.assertEqual(self.iNrRlcAck.E1, expE1)
        self.assertEqual(self.iNrRlcAck.Sn, expSn)
        print(str(self.iNrRlcAck))

        testRlcAmPdu = "8AAF7B"
        self.iNrRlcAck = RlcAmAck(12, testRlcAmPdu)
        expE1 = 0
        expSn = 0xAAF
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 12)
        self.assertEqual(self.iNrRlcAck.E1, expE1)
        self.assertEqual(self.iNrRlcAck.Sn, expSn)
        print(str(self.iNrRlcAck))

    def test_AckParsing18Bit(self):
        testRlcAmPdu = "FFFFFD"
        self.iNrRlcAck = RlcAmAck(18, testRlcAmPdu)
        expE1 = 0
        expSn = 0x3FFFF
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 18)
        self.assertEqual(self.iNrRlcAck.E1, expE1)
        self.assertEqual(self.iNrRlcAck.Sn, expSn)
        print(str(self.iNrRlcAck))

        testRlcAmPdu = "3F0F02"
        self.iNrRlcAck = RlcAmAck(18, testRlcAmPdu)
        expE1 = 1
        expSn = 0x03C3C0
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 18)
        self.assertEqual(self.iNrRlcAck.E1, expE1)
        self.assertEqual(self.iNrRlcAck.Sn, expSn)
        print(str(self.iNrRlcAck))

