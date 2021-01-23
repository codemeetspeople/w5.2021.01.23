import unittest

from point import Point


class TestPoint(unittest.TestCase):
    def test_initializer(self):
        point = Point()

        self.assertEqual(point.x, 0.0)
        self.assertEqual(point.y, 0.0)

        point = Point(10.0, 1.5)

        self.assertEqual(point.x, 10.0)
        self.assertEqual(point.y, 1.5)

    def test_setters(self):
        point = Point()

        self.assertEqual(point.x, 0.0)
        self.assertEqual(point.y, 0.0)

        point.x = 5
        point.y = 10

        self.assertEqual(point.x, 5.0)
        self.assertEqual(point.y, 10.0)

        with self.assertRaises(TypeError):
            point.x = lambda x: x + 1

        with self.assertRaises(ValueError):
            point.x = 'test'

    def test_point_to_string(self):
        point = Point()

        self.assertEqual(str(point), '(0.0, 0.0)')
        self.assertEqual(repr(point), '(0.0, 0.0)')

    def test_point_comparison(self):
        p1 = Point()
        p2 = Point()
        p3 = Point(2, 4)

        self.assertTrue(p1 == p2)
        self.assertFalse(p1 != p2)
        self.assertTrue(p1 != p3)
        self.assertFalse(p1 == p3)

        with self.assertRaises(TypeError):
            p1 == 10

        with self.assertRaises(TypeError):
            p1 != 10


if __name__ == '__main__':
    unittest.main()
