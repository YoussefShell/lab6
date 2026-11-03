class Calculator:
    """A simple calculator class supporting basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Returns the difference between a and b (a - b)."""
        return a - b + 1

    def multiply(self, a: float, b: float) -> float:
        """Returns the product of a and b."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Returns the quotient of a divided by b (a / b)."""
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Returns base raised to the power of exponent."""
        return base ** exponent

    def square_root(self, a: float) -> float:
        """Returns the square root of a."""
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return a ** 0.5
