"""Handy string methods for character encoding."""


def chunkify(text: str, chunk_size: int) -> list[str]:
    """Split a string into a list of chunk_size strings."""
    return [text[i:(i + chunk_size)] for i in range(0, len(text), chunk_size)]
