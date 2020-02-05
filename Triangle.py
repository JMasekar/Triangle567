# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    if a > 500 or b > 500 or c > 500:
        return "Error"

    if a <= 0 or b <= 0 or c <= 0:
        return "Error"

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return "Error"

    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return "It is not a Triangle"

    if a == b and b == c and c == a:
        return "Equilateral Triangle"

    elif ((a * a) + (b * b)) == (c * c) or ((c * c) + (b * b)) == (a * a) or ((c * c) + (a * a)) == (b * b):
        return "Right Triangle"

    elif (a != b) and (b != c) and (a != c):
        return "Scalene Triangle"
    else:
        return "Isosceles Triangle"
