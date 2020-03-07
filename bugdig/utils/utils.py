
def fib_gen(n):
    """
    Generates the fibonacci secuence up to n
    :type n: Positive Integer

    :returns: Fibonacci secuence numbers
    :rtype: Generator
    """
    a, b = 1, 2
    for _ in range(n):
        yield a
        a, b = b, a + b

