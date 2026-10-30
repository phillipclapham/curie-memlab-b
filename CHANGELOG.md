# Changelog

## Unreleased

- Add `slug_from_email`, which slugifies the local part of an email address (dropping any `+tag` suffix) for profile URLs and refuses addresses that are not of the form `local@domain`.
- Add `SlugError`, the library's own error type (a `ValueError` subclass).

## 0.1.0

- Initial release: `slugify`.
