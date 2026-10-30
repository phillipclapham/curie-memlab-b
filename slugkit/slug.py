"""Turn arbitrary text into URL slugs."""

import re
import unicodedata

from .errors import SlugError

__all__ = ["slugify"]

_NON_WORD = re.compile(r"[^a-z0-9]+")


def _truncate(slug: str, sep: str, max_length: int) -> str:
    """Cut ``slug`` to at most ``max_length`` characters at a separator.

    The cut is at the last ``sep`` that fits so words stay whole; a word
    longer than the limit is cut mid-word. The result never ends on ``sep``.
    """
    if len(slug) <= max_length:
        return slug
    cut = slug.rfind(sep, 0, max_length + 1)
    if cut <= 0:
        return slug[:max_length]
    return slug[:cut]


def slugify(text: str, sep: str = "-", max_length: int | None = None) -> str:
    """Return a lowercase ASCII slug for ``text``.

    Accented letters are folded to their ASCII base ("Café" -> "cafe").
    Runs of anything that is not a letter or digit become one ``sep``.
    Leading and trailing separators are removed.
    With ``max_length`` the slug is capped at that many characters, cut
    at the last separator that fits so words stay whole.
    """
    if max_length is not None and max_length < 1:
        raise SlugError("max_length must be at least 1")
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = _NON_WORD.sub(sep, folded.lower()).strip(sep)
    if max_length is None:
        return slug
    return _truncate(slug, sep, max_length)
