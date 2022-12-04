import unittest
# import os,sys
# sys.path.append(os.path.join("..","speciallecture"))
from speciallecture.Timecheck import Timecheck

class TestTimecheck(unittest.TestCase):
    def test_read1(self):
        timecheck = Timecheck()
        self.assertEqual("OK", timecheck.check(0, 0, 22))

    def test_read2(self):
        timecheck = Timecheck()
        self.assertEqual("NG", timecheck.check(22, 0, 22))

    def test_read3(self):
        timecheck = Timecheck()
        self.assertEqual("NG", timecheck.check(1, 2, 22))

    def test_read4(self):
        timecheck = Timecheck()
        self.assertEqual("NG", timecheck.check(23, 2, 22))
    
    def test_read5(self):
        timecheck = Timecheck()
        self.assertEqual("OK", timecheck.check(0, 22, 5))
    
    def test_read6(self):
        timecheck = Timecheck()
        self.assertEqual("NG", timecheck.check(5, 22, 5))
    
    def test_read7(self):
        timecheck = Timecheck()
        self.assertEqual("OK", timecheck.check(22, 22, 5))
    
    def test_read8(self):
        timecheck = Timecheck()
        self.assertEqual("OK", timecheck.check(23, 22, 5))