from typing import Callable


# створює та повертає функцію fibonacci, яка використовує замикання для кешування результатів обчислень
def caching_fibonacci() -> Callable[[int], int]: 
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# створюємо екземпляр функції fibonacci з кешуванням
fib = caching_fibonacci()

# тестування функції
if __name__ == "__main__":
    print(fib(10))  # 55
    print(fib(15))  # 610