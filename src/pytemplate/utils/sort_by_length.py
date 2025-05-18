def sort_by_length(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda s: len(s))
