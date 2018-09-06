from unittest import TestCase
from nruplane.nrcommon.nrpdu import nrpdu


class TestNrpdu(TestCase):
    def setUp(self):
        self.iNrpdu = nrpdu()

    def test_Instance(self):
        self.iNrpdu = nrpdu('abcd')
        print(self.iNrpdu)