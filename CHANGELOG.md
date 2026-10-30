# Changelog

## Unreleased

- Add `SlugError`, the library's own error type (a `ValueError` subclass).
- Add `slug_from_email`, which turns the local part of an email address into a slug, dropping a `+tag` suffix and refusing addresses that are not of the form `local@domain`.

## 0.1.0

- Initial release: `slugify`.
