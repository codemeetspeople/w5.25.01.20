import unittest
from point.point import Point


class TestPointClass(unittest.TestCase):
    def _test_point(self, point, x, y):
        self.assertEqual(point.x, x)
        self.assertEqual(point.y, y)

        self.assertTrue(isinstance(point.x, float))
        self.assertTrue(isinstance(point.y, float))


    def test_point_default_constructor(self):
        self._test_point(Point(), 0, 0)

    def test_point_constructor(self):
        x, y = 5, 7
        self._test_point(Point(x, y), x, y)

    def test_point_setters(self):
        point = Point()
        self._test_point(point, 0, 0)

        point.x = 42
        point.y = 20

        self._test_point(point, 42, 20)

    def test_point_cmp_methods(self):
        p1 = Point(2, 5)
        p2 = Point(2, 5)
        p3 = Point(10, 9)

        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

        self.assertTrue(p1 != p3)
        self.assertFalse(p1 != p2)


    def test_str_representation(self):
        point = Point()

        self.assertEqual(str(point), '(0.0, 0.0)')


    def test_point_distance(self):
        p1 = Point(2, 5)
        p2 = Point(2, 5)
        p3 = Point(10, 9)

        self.assertEqual(p1.distance(p2), 0.0)
        self.assertEqual(p1.distance(p3), round(8.94427190999916, 2))


    def test_point_exceptions(self):
        with self.assertRaises(ValueError):
            point = Point('invalid', 'value')


if __name__ == '__main__':
    unittest.main()
