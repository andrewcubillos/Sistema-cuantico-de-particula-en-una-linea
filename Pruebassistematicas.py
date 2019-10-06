from Sistemacuanticodeparticulaenunalinea import *
import unittest

class PruebasFunciones(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(0.05263157894736842,
                         
                         position([(-3,-1),
                                   (0,-2),
                                   (0,1),
                                   (2,0)],     2))
                         
    def test2(self):
        self.assertEqual((0,-0.9999999999999998),
                         
                         transition([(0,-1),
                                     (1,0)],    [(1,0),
                                                 (0,-1)]))

    def test3(self):
        self.assertEqual((0,1.0000000000000002),
                         
                         transition([(0,(2**(1/2))/2),
                                     (-(2**(1/2))/2,0)],    [((2**(1/2))/2,0),
                                                            (0,-(2**(1/2))/2)]))    





if __name__ == '__main__':
    unittest.main()
