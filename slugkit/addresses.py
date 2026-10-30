"""Turn email addresses into profile-URL slugs."""

from .errors import SlugError
from .slug import slugify

__all__ = ["slug_from_email"]


def slug_from_email(address: str, sep: str = "-") -> str:
    """Return a slug for the profile URL of ``address``.

    The local part (before the ``@``) is slugified, with any ``+tag``
    suffix dropped first ("Jane.Doe+news@example.com" -> "jane-doe").
    ``sep`` is passed through to :func:`slugify`.

    Raises :class:`SlugError` when ``address`` is not of the form
    ``local@domain`` (no ``@``, more than one ``@``, or an empty local
    part or domain).
    """
    if address.count("@") != 1:
        raise SlugError(f"not a valid email address: {address!r}")
    local, _, domain = address.partition("@")
    if not local or not domain:
        raise SlugError(f"not a valid email address: {address!r}")
    return slugify(local.split("+", 1)[0], sep=sep)
