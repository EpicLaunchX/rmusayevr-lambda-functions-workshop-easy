def filter_even_numbers(numbers: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, numbers))
