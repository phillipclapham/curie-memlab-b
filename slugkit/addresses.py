"""Turn the local part of an email address into a URL slug."""

from .errors import SlugError
from .slug import slugify

__all__ = ["slug_from_email"]


def slug_from_email(address: str, sep: str = "-") -> str:
    """Return the local part of ``address`` as a slug.

    The part before the ``@`` is slugified; a ``+tag`` suffix on the
    local part is dropped first ("Jane.Doe+news" -> "jane-doe").
    An address that is not of the form ``local@domain`` (no ``@``,
    more than one ``@``, or an empty local part or domain) raises
    :class:`SlugError`.
    """
    local, at, domain = address.partition("@")
    if not at or "@" in domain or not local or not domain:
        raise SlugError(f"not a local@domain address: {address!r}")
    if "+" in local:
        local = local.split("+", 1)[0]
    if not local:
        raise SlugError(f"local part is empty after dropping the +tag: {address!r}")
    return slugify(local, sep=sep)
