# -*- coding: utf-8 -*-
import unittest
import find_key

class TestFindKey(unittest.TestCase):

  def test_only_C(self):
    self.assertEqual(find_key.find_key(['C']),[['C', 'D', 'E', 'F', 'G', 'A', 'B'], ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'], ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'], ['F', 'G', 'A', 'A#', 'C', 'D', 'E'], ['G', 'A', 'B', 'C', 'D', 'E', 'F#'], ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'], ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']])

  def test_C_and_D(self):
    self.assertEqual(find_key.find_key(['C','D']),[['C', 'D', 'E', 'F', 'G', 'A', 'B'], ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'], ['F', 'G', 'A', 'A#', 'C', 'D', 'E'], ['G', 'A', 'B', 'C', 'D', 'E', 'F#'], ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']])

  def test_C_D_E(self):
    self.assertEqual(find_key.find_key(['C','D','E']),[['C', 'D', 'E', 'F', 'G', 'A', 'B'], ['F', 'G', 'A', 'A#', 'C', 'D', 'E'], ['G', 'A', 'B', 'C', 'D', 'E', 'F#']])

  def test_not_found(self):
    self.assertEqual(find_key.find_key(['C','C#','D']),[])

if __name__ == "__main__":
  unittest.main()
