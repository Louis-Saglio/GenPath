import unittest

from point import Point, Path


class TestPoint(unittest.TestCase):

    def test_equals(self):
        self.assertEqual(Point(1, 2), Point(1, 2))

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash(Point(1, 2)))


class TestPath(unittest.TestCase):

    def test_distance_between(self):
        self.assertEqual(5, Path.distance_between(Point(0, 0), Point(3, 4)))
        self.assertEqual(0, Path.distance_between(Point(3, 4), Point(3, 4)))

    def test_total_length(self):
        points = [
            Point(0, 0),
            Point(1, 0),
            Point(2, 0),
            Point(3, 0),
            Point(4, 0),
            Point(6, 0),
        ]
        self.assertEqual(6, Path(points).total_length())
        self.assertEqual(5, Path((Point(4, 5), Point(9, 5))).total_length())

    def test_similarity(self):
        path1 = Path([Point(0, 0), Point(0, 1), Point(0, 0), Point(7, 2)])
        path2 = Path([Point(0, 0), Point(0, 1), Point(0, 1), Point(7, 2)])
        self.assertEqual(0.75, Path.similarity(path1, path2))


if __name__ == '__main__':
    unittest.main()
