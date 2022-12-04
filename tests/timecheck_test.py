import unittest
# import os,sys
# sys.path.append(os.path.join("..","speciallecture"))
from speciallecture.Timecheck import Timecheck

class TestTimecheck(unittest.TestCase):
    def __init__(self) -> None:
        self.timecheck = Timecheck()
        
    def test_read1(self):
        self.assertEqual("OK", self.timecheck.check(0, 0, 22))

    def test_read2(self):
        self.assertEqual("NG", self.timecheck.check(22, 0, 22))

    def test_read3(self):
        self.assertEqual("NG", self.timecheck.check(1, 2, 22))

    def test_read4(self):
        self.assertEqual("NG", self.timecheck.check(23, 2, 22))
    
    def test_read5(self):
        self.assertEqual("OK", self.timecheck.check(0, 22, 5))
    
    def test_read6(self):
        self.assertEqual("NG", self.timecheck.check(5, 22, 5))
    
    def test_read7(self):
        self.assertEqual("OK", self.timecheck.check(22, 22, 5))
    
    def test_read8(self):
        self.assertEqual("NG", self.timecheck.check(23, 22, 5))