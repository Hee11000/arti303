"""Text utility functions."""


def clean_name(raw):
    """Collapse whitespace and title-case a name."""
    return " ".join(raw.split()).title()
