from unittest import TestCase
from nruplane.nrrlc.rlcamnack import RlcAmNack

class TestRlcAmNack(TestCase):
    def setUp(self):
        print(' {:s} started '.format(self._testMethodName).center(50, '='))

    def tearDown(self):
        print(' {:s} ended '.format(self._testMethodName).center(50, '='))

    def test_NackInstance(self):
        self.iNrRlcAck = RlcAmNack(6)

        self.iNrRlcAck = RlcAmNack(12)
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 12)
        self.assertEqual(self.iNrRlcAck.E1, 0)
        self.assertEqual(self.iNrRlcAck.Sn, 0)
        print(str(self.iNrRlcAck))

        self.iNrRlcAck = RlcAmNack(18)
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 18)
        self.assertEqual(self.iNrRlcAck.E1, 0)
        self.assertEqual(self.iNrRlcAck.Sn, 0)
        print(str(self.iNrRlcAck))

        # Invalid Length
        testRlcAmPdu = "0FAABBBBFFFFFFFF"

        #self.iNrRlcAck = RlcAmNack(18, testRlcAmPdu)
        #self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 18)
        #self.assertEqual(self.iNrRlcAck.E1, 0)
        #self.assertEqual(self.iNrRlcAck.Sn, 0)
        #print(str(self.iNrRlcAck))
        # refer to self.test_AckParsing18Bit() for parsing test items

        #self.iNrRlcAck = RlcAmNack(12, testRlcAmPdu)
        #self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 12)
        #self.assertEqual(self.iNrRlcAck.E1, 0)
        #self.assertEqual(self.iNrRlcAck.Sn, 0)
        #print(str(self.iNrRlcAck))
        # refer to self.test_AckParsing12Bit() for parsing test items

    def test_NackParsing12Bit(self):
        testRlcAmPdu = "8FAABB"
        self.iNrRlcAck = RlcAmNack(12, testRlcAmPdu)
        expE1 = 1
        expE2 = 0
        expE3 = 1
        expSn = 0x8FA
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 12)
        self.assertEqual(self.iNrRlcAck.E1, expE1)
        self.assertEqual(self.iNrRlcAck.E2, expE2)
        self.assertEqual(self.iNrRlcAck.E3, expE3)
        self.assertEqual(self.iNrRlcAck.Sn, expSn)
        print(str(self.iNrRlcAck))

        testRlcAmPdu = "8AA17B"
        self.iNrRlcAck = RlcAmNack(12, testRlcAmPdu)
        expE1 = 0
        expE2 = 0
        expE3 = 0

        expSn = 0x8AA
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 12)
        self.assertEqual(self.iNrRlcAck.E1, expE1)
        self.assertEqual(self.iNrRlcAck.E2, expE2)
        self.assertEqual(self.iNrRlcAck.E3, expE3)
        self.assertEqual(self.iNrRlcAck.Sn, expSn)
        print(str(self.iNrRlcAck))

    def test_NackParsing18Bit(self):
        testRlcAmPdu = "FFFFFD"
        self.iNrRlcAck = RlcAmNack(18, testRlcAmPdu)
        expE1 = 0
        expSn = 0x3FFFF
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 18)
        self.assertEqual(self.iNrRlcAck.E1, expE1)
        self.assertEqual(self.iNrRlcAck.Sn, expSn)
        print(str(self.iNrRlcAck))

        testRlcAmPdu = "3F0F02"
        self.iNrRlcAck = RlcAmNack(18, testRlcAmPdu)
        expE1 = 1
        expSn = 0x03C3C0
        self.assertEqual(self.iNrRlcAck.SN_BIT_LENGTH, 18)
        self.assertEqual(self.iNrRlcAck.E1, expE1)
        self.assertEqual(self.iNrRlcAck.Sn, expSn)
        print(str(self.iNrRlcAck))
