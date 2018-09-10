from unittest import TestCase
from nruplane.nrrlc.rlcumpdu import NrRlcUmPdu

class TestNrRlcUmPdu(TestCase):
    def setUp(self):
        self.iNrRlcUmPdu = NrRlcUmPdu(18)

    def test_Instance(self):
        self.iNrRlcUmPdu = NrRlcUmPdu(6)
        self.assertEqual(self.iNrRlcUmPdu.SN_LENGTH, 6)
        self.iNrRlcUmPdu = NrRlcUmPdu(12)
        self.assertEqual(self.iNrRlcUmPdu.SN_LENGTH, 12)

        testRlcUmPdu = "02AAAAFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 0
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

        testRlcUmPdu = "7EAAAAFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 1
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

        testRlcUmPdu = "8EAAAAFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 2
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

        testRlcUmPdu = "CEAAAAFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 3
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

        testRlcUmPdu = "02AAAAFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        expSi = 0
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

        testRlcUmPdu = "7EAAAAFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        expSi = 1
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

        testRlcUmPdu = "8EAAAAFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        expSi = 2
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

        testRlcUmPdu = "CEAAAAFFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(6, testRlcUmPdu)
        expSi = 3
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

    #def test_initFieldsEmpty(self):
    #    self.fail()

    #def test_getNumHeaderBytes(self):
    #    self.fail()

    #def test_initFields(self):
    #    self.fail()
