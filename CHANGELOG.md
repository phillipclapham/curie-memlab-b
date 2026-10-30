# Changelog

## Unreleased

- Add `max_length` option to `slugify`: cap the slug at a maximum length, cutting at word boundaries and refusing values below 1 with `SlugError`.
- Add `SlugError`, the library's own error type (a `ValueError` subclass).

## 0.1.0

- Initial release: `slugify`.
