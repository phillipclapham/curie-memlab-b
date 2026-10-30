import unittest

from slugkit import SlugError, slug_from_email


class SlugFromEmailTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slug_from_email("jane.doe@example.com"), "jane-doe")

    def test_plus_tag_dropped(self):
        self.assertEqual(slug_from_email("Jane.Doe+news@example.com"), "jane-doe")

    def test_custom_separator(self):
        self.assertEqual(slug_from_email("jane.doe@example.com", sep="_"), "jane_doe")


class SlugFromEmailErrorTest(unittest.TestCase):
    def _assert_refused(self, address):
        with self.assertRaises(SlugError) as ctx:
            slug_from_email(address)
        self.assertTrue(str(ctx.exception), "expected a non-empty error message")

    def test_no_at(self):
        self._assert_refused("example.com")

    def test_two_ats(self):
        self._assert_refused("a@b@c")

    def test_empty_local(self):
        self._assert_refused("@example.com")

    def test_empty_domain(self):
        self._assert_refused("jane@")


if __name__ == "__main__":
    unittest.main()
