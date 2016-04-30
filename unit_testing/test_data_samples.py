import unittest
import data_samples

class DataTests(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(data_samples.get_integer_1(), 1)
        # each assert function has an optional message parm at the end
        self.assertEqual(data_samples.get_integer_1(), 1, "1 should equal 1")

    def test_not_equals(self):
        self.assertNotEquals(data_samples.get_integer_1(), 2)

    def test_true(self):
        self.assertTrue(data_samples.get_boolean_true())

    def test_false(self):
        self.assertFalse(data_samples.get_boolean_false())

    def test_is(self):
        self.assertIs(data_samples.get_string(), data_samples.get_string())

    def test_is_not(self):
        # not the same object, even though the same value
        self.assertIsNot(data_samples.get_string(), "This is a string")

    def test_is_none(self):
        self.assertIsNone(data_samples.get_none())

    def test_is_not_none(self):
        self.assertIsNotNone(data_samples.get_integer_1())

    def test_in(self):
        self.assertIn(1, data_samples.get_list_1())

    def test_not_in(self):
        self.assertNotIn(99, data_samples.get_list_1())

    def test_is_instance(self):
        instance = data_samples.SampleClass()
        self.assertIsInstance(instance, data_samples.SampleClass)

    def test_not_is_instance(self):
        instance = data_samples.SampleClass()
        self.assertNotIsInstance(instance, data_samples.SampleClass2)

    def test_raises_1(self):
        self.assertRaises(data_samples.CustomException, data_samples.get_custom_exception)

    def test_raises_2(self):
        with self.assertRaises(Exception) as context:
            data_samples.get_execption()

        self.assertIn('Whoops', context.exception)

    def test_raises_regexp(self):
        self.assertRaisesRegexp(data_samples.CustomException, 'Custom whoops', data_samples.get_custom_exception)

    def test_almost_equal(self):
        self.assertAlmostEqual(data_samples.get_long_floating_point_1(), data_samples.get_long_floating_point_2(), 1)

    def test_not_almost_equal(self):
        self.assertNotAlmostEqual(data_samples.get_long_floating_point_1(), data_samples.get_long_floating_point_2(), 2)

    def test_greater(self):
        self.assertGreater(data_samples.get_integer_2(), data_samples.get_integer_1())

    def test_greater_equal(self):
        self.assertGreaterEqual(data_samples.get_integer_1(), data_samples.get_integer_1())

    def test_less(self):
        self.assertLess(data_samples.get_integer_1(), data_samples.get_integer_2())

    def test_less_equal(self):
        self.assertGreaterEqual(data_samples.get_integer_1(), data_samples.get_integer_1())

    def test_regexp_matches(self):
        self.assertRegexpMatches(data_samples.get_string(), "^.*is a.*$")

    def test_not_regexp_matches(self):
        self.assertNotRegexpMatches(data_samples.get_string(), "^is a$")

    def test_items_equal(self):
        self.assertItemsEqual(data_samples.get_list_1(), data_samples.get_list_2())

if __name__ == '__main__':
    unittest.main()