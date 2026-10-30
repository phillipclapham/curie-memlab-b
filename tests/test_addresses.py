"""Tests for slug_from_email."""

import unittest

from slugkit import SlugError, slug_from_email


class SlugFromEmailTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slug_from_email("jane.doe@example.com"), "jane-doe")

    def test_plus_tag_suffix_is_dropped(self):
        self.assertEqual(slug_from_email("Jane.Doe+news@example.com"), "jane-doe")

    def test_custom_separator(self):
        self.assertEqual(slug_from_email("jane.doe@example.com", sep="_"), "jane_doe")

    def test_invalid_addresses_raise(self):
        for address in ("no-at-sign", "two@@example.com", "jane.doe@not@example.com",
                        "@example.com", "jane.doe@"):
            with self.assertRaises(SlugError):
                slug_from_email(address)


if __name__ == "__main__":
    unittest.main()
