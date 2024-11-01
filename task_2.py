import re
import typing as t
from typing import Callable


def generator_numbers(text: str) -> t.Iterator[float]:
    '''This function stends to parse the text, identify all real numbers 
    considered to be part of the returns, and return them as a generator.'''

    num_pattern = r"-?\d+\.?\d+"
    for item in re.finditer(num_pattern, text):
        yield float(item.group())


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


text = "Загальний .. частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
