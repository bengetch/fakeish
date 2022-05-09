import random


class RandomObject:

    @staticmethod
    def ssn(blank: float = 0):
        if blank > 0 and random.uniform(0, 1) < blank:
            return ""
        return f"{random.randint(100, 999)}-" \
               f"{random.randint(10, 99)}-" \
               f"{random.randint(1000, 9999)}"
