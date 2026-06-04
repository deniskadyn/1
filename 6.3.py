import sys
import unittest


def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        """Тест: факториал 0 должен быть равен 1"""
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        """Тест: факториал 1 должен быть равен 1"""
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_number(self):
        """Тест: факториал положительного числа"""
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(7), 5040)

    def test_factorial_of_small_numbers(self):
        """Тест: факториал небольших чисел"""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(6), 720)

    def test_factorial_raises_error_for_negative(self):
        """Тест: отрицательное число должно вызывать ValueError"""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_raises_error_for_too_large(self):
        """Тест: слишком большое число должно вызывать ValueError"""
        with self.assertRaises(ValueError):
            factorial(20)

    def test_factorial_returns_int(self):
        """Тест: результат должен быть целым числом"""
        result = factorial(10)
        self.assertIsInstance(result, int)


# Запуск тестов
if __name__ == "__main__":
    unittest.main(verbosity=2)