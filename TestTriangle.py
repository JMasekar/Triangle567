# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self):
        """ testing right triangles """
        self.assertEqual(classifyTriangle(3, 4, 5), "Right Triangle")
        self.assertEqual(classifyTriangle(5, 3, 4), "Right Triangle")

    def testEquilateralTriangle(self):
        """ testing equilateral triangles """
        self.assertEqual(classifyTriangle(1, 1, 1), "Equilateral Triangle")
        self.assertEqual(classifyTriangle(2, 2, 2), "Equilateral Triangle")
        self.assertEqual(classifyTriangle(5, 5, 5), "Equilateral Triangle")

    def testScaleneTriangle(self):
        """ testing scalene triangles """
        self.assertEqual(classifyTriangle(3, 5, 7), "Scalene Triangle")

    def testIsoscelesTriangle(self):
        """ testing isosceles triangles """
        self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral Triangle")
        self.assertEqual(classifyTriangle(3, 4, 5), "Right Triangle")
        self.assertEqual(classifyTriangle(3, 4, 3), "Isosceles Triangle")

    def testRandom1(self):
        """ testing invalid values """
        self.assertEqual(classifyTriangle(2.5, 5, 8), "Error")
        self.assertEqual(classifyTriangle(650, 800, 33), "Error")

    def testRandom2(self):
        """ testing invalid values """
        self.assertEqual(classifyTriangle(-5, 8, 12), "Error")
        self.assertEqual(classifyTriangle(0, 2, 6), "Error")

    def testRandom3(self):
        """ invalid output testing """
        self.assertNotEqual(classifyTriangle(3, 4, 2), "Equilateral Triangle")
        self.assertNotEqual(classifyTriangle(3, 3, 6), "Right Triangle")

    def testRandom4(self):
        """ invalid output testing """
        with self.assertRaises(TypeError):
            classifyTriangle("a", 3, 5)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)


