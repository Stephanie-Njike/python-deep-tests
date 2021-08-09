#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 Example of a unit test for the calculation of the median of a table
"""
import unittest
import random

def mediane(tab):
    """
    return the median element of this array
    """
    if len(tab) > 1:
        milieu = int(len(tab)/2)
    else:
        milieu = 0
    stab = sorted(tab)
    return stab[milieu]

class TestMediane(unittest.TestCase):
    """
     Test class to validate the proper functioning of mediane
    """

    def test_mediane(self):

        # List containing a single element
        tab = [random.randint(3, 17)]
        self.assertEqual(mediane(tab), tab[0],
                         "Your function applied to "+str(tab)+
                         " has returned "+str(mediane(tab))+" and not "+
                         str(tab[0]))
        # Liste triée contenant trois éléments
        for _ in range(10):
            median = random.randint(3, 19)
            tab = [median-random.randint(1, 5), median,
                   median+random.randint(3, 9)]
            random.shuffle(tab)
            self.assertEqual(mediane(tab), median,
                             "Your function applied to "+str(tab)+
                             " has returned "+str(mediane(tab))+" et non "+
                             str(median))

        # Sorted list containing five elements
        for _ in range(10):
            tab = [None] * 5
            tab[0] = random.randint(3, 19)
            for j in range(1, 5):
                tab[j] = tab[j-1]+random.randint(3, 19)
            median = tab[2]
            random.shuffle(tab)
            self.assertEqual(mediane(tab), median,
                             "Your function applied to "+str(tab)+
                             " has returned "+str(mediane(tab))+" et non "+
                             str(median))

if __name__ == '__main__':
    unittest.main()
