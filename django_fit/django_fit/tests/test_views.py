from django.test import TestCase


class AdditionTestCase(TestCase):
    def test_addition_works(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual(0 + 2, 2)


class MultiplicationTestCase(TestCase):
    def test_multiplication_works(self):
        self.assertEqual(3 * 3, 9)
        self.assertEqual(4 * 8, 32)


class SubstractionTestCase(TestCase):
    def test_substraction_works(self):
        self.assertEqual(3 - 3, 0)
        self.assertEqual(7 - 3, 4)


class DivisionTestCase(TestCase):
    def test_division_works(self):
        self.assertEqual(3 / 3, 1)
        self.assertEqual(4 / 2, 2)


class CalculationTestCase(TestCase):
    def test_addition_works(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual(0 + 2, 2)

    def test_multiplication_works(self):
        self.assertEqual(3 * 3, 9)
        self.assertEqual(4 * 8, 32)

    def test_substraction_works(self):
        self.assertEqual(3 - 3, 0)
        self.assertEqual(7 - 3, 4)

    def test_division_works(self):
        self.assertEqual(3 / 3, 1)
        self.assertEqual(4 / 2, 2)