class MathUtils:
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * MathUtils.factorial(n-1)

print(MathUtils.factorial(3))