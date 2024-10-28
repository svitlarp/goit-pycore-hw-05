import re

def generator_numbers(text: str):

    num_pattern = r"^-?\d+(.\d+)?$"
    (yield float(w) if "." in w else int(w) for w in text.split() if re.match(num_pattern, w))

def sum_profit(text: str, func: Callable):
    pass




text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")