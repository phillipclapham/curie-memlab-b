"""Slug generation from email addresses."""

from slugkit.errors import SlugError
from slugkit.slug import slugify

__all__ = ["slug_from_email"]


def slug_from_email(address: str, sep: str = "-") -> str:
    """Turn the local part of an email address into a slug.

    The part before the ``@`` is lowercased, and every run of characters
    that is not a letter or digit (including ``.`` and ``_``) becomes one
    ``sep``. A ``+tag`` suffix on the local part is dropped:

    >>> slug_from_email("jane.doe@example.com")
    'jane-doe'
    >>> slug_from_email("Jane.Doe+news@example.com")
    'jane-doe'

    Raises :class:`slugkit.SlugError` when ``address`` is not of the form
    ``local@domain`` — that is, when it has no ``@``, more than one ``@``,
    or an empty local part or domain.
    """
    if address.count("@") != 1:
        raise SlugError(f"not a valid email address: {address!r}")
    local, domain = address.split("@")
    if not local or not domain:
        raise SlugError(f"not a valid email address: {address!r}")
    local = local.lower().split("+", 1)[0]
    return slugify(local, sep)
