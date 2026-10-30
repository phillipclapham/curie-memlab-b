"""Turn arbitrary text into URL slugs."""

import re
import unicodedata

from .errors import SlugError

__all__ = ["slugify"]

_NON_WORD = re.compile(r"[^a-z0-9]+")


def slugify(text: str, sep: str = "-", max_length: int | None = None) -> str:
    """Return a lowercase ASCII slug for ``text``.

    Accented letters are folded to their ASCII base ("Café" -> "cafe").
    Runs of anything that is not a letter or digit become one ``sep``.
    Leading and trailing separators are removed.

    When ``max_length`` is given, the slug is capped at that many
    characters: whole words are kept while they fit, a word longer than
    the limit is cut at the limit, and the result never ends in a
    separator. A ``max_length`` below 1 raises :class:`SlugError`.
    """
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = _NON_WORD.sub(sep, folded.lower()).strip(sep)
    if max_length is None:
        return slug
    if max_length < 1:
        raise SlugError(f"max_length must be at least 1, got {max_length}")
    if len(slug) <= max_length:
        return slug
    kept = ""
    for word in slug.split(sep):
        candidate = word if not kept else kept + sep + word
        if len(candidate) > max_length:
            break
        kept = candidate
    if not kept:
        return slug[:max_length]
    return kept
