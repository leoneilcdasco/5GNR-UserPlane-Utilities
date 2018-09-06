from unittest import TestCase
from nruplane.nrrlc.rlcumpdu import NrRlcUmPdu

class TestNrRlcUmPdu(TestCase):
    def setUp(self):
        self.iNrRlcUmPdu = NrRlcUmPdu(18)

    def test_Instance(self):
        self.iNrRlcUmPdu = NrRlcUmPdu(6)
        self.iNrRlcUmPdu = NrRlcUmPdu(12)

        testRlcUmPdu = "12FFFFFF"
        self.iNrRlcUmPdu = NrRlcUmPdu(12, testRlcUmPdu)
        expSi = 0
        act = self.iNrRlcUmPdu.Si
        self.assertEqual(act, expSi)

    #def test_initFieldsEmpty(self):
    #    self.fail()

    #def test_getNumHeaderBytes(self):
    #    self.fail()

    #def test_initFields(self):
    #    self.fail()
