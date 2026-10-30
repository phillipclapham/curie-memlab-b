# Changelog

## Unreleased

- Add `max_length` option to `slugify`: cap the slug's length, cutting at the last separator that fits; `max_length` below 1 raises `SlugError`.
- Add `SlugError`, the library's own error type (a `ValueError` subclass).

## 0.1.0

- Initial release: `slugify`.
