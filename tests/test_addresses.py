import unittest

from slugkit import SlugError, slug_from_email


class SlugFromEmailTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slug_from_email("jane.doe@example.com"), "jane-doe")

    def test_plus_tag_dropped(self):
        self.assertEqual(slug_from_email("Jane.Doe+news@example.com"), "jane-doe")

    def test_custom_separator(self):
        self.assertEqual(slug_from_email("jane.doe@example.com", sep="_"), "jane_doe")

    def test_invalid_addresses_raise(self):
        invalid = [
            "noat",
            "two@ats@example.com",
            "@example.com",
            "jane@",
            "+tag@example.com",  # strips to an empty slug; refused like an empty local part
        ]
        for address in invalid:
            with self.subTest(address=address):
                with self.assertRaises(SlugError):
                    slug_from_email(address)


if __name__ == "__main__":
    unittest.main()
