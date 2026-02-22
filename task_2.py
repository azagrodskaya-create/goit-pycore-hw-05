import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    # аналізує текст та знаходить всі дійсні числа, що відокремлені пробілами.
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text): # знаходить всі збіги в тексті за допомогою регулярного виразу
        yield float(match.group()) # перетворює знайдені рядки на числа з плаваючою комою та повертає їх по одному


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # підсумовує всі знайдені числа від генератора
    total_sum = 0.0
    # Ітеруємося по генератору, який повертає func(text)
    for number in func(text):
        total_sum += number
    return total_sum


# Приклад використання:
if __name__ == "__main__": 
    text = ("Загальний дохід працівника складається з декількох частин: "
            "1000.01 як основний дохід, доповнений додатковими "
            "надходженнями 27.45 і 324.00 доларів.")
    
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  # Загальний дохід: 1351.46