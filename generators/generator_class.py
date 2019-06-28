

from lecture4.generator_prime_number import is_prime


class PrimeGenerator:

    def __init__(self, final):
        self.final = final
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 2:
            self.current = 3
            return 2
        elif self.current == 3:
            self.current += 2
            return 3
        elif is_prime(self.current):
            self.current += 2
            return self.current

        if self.current > self.final:
            raise StopIteration


for i in PrimeGenerator(1000):
    print(i, end=' ')
