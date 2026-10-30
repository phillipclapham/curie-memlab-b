import unittest

from slugkit import SlugError, slugify


class SlugErrorTest(unittest.TestCase):
    def test_is_a_value_error(self):
        with self.assertRaises(ValueError):
            raise SlugError("bad input")


class SlugifyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_accents_fold_to_ascii(self):
        self.assertEqual(slugify("Café déjà vu"), "cafe-deja-vu")

    def test_runs_collapse(self):
        self.assertEqual(slugify("a  --  b"), "a-b")

    def test_custom_separator(self):
        self.assertEqual(slugify("Hello World", sep="_"), "hello_world")


class SlugifyMaxLengthTest(unittest.TestCase):
    def test_fits_unchanged(self):
        self.assertEqual(slugify("hello world", max_length=20), "hello-world")

    def test_cut_at_last_separator(self):
        self.assertEqual(slugify("the quick brown fox", max_length=12), "the-quick")

    def test_single_word_cut_at_limit(self):
        self.assertEqual(slugify("extraordinary", max_length=5), "extra")

    def test_no_trailing_separator(self):
        self.assertEqual(slugify("ab cd", max_length=3), "ab")

    def test_rejects_max_length_below_one(self):
        with self.assertRaises(SlugError) as ctx:
            slugify("hello", max_length=0)
        self.assertIsInstance(ctx.exception, ValueError)

    def test_passthrough_when_no_limit(self):
        self.assertEqual(slugify("hello world"), "hello-world")
        self.assertEqual(slugify("hello world", max_length=None), "hello-world")
        self.assertEqual(slugify("hello world", max_length=100), "hello-world")


if __name__ == "__main__":
    unittest.main()
