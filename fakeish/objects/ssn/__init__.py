import random


class RandomObject:

    @staticmethod
    def ssn():
        return f"{random.randint(100, 999)}-" \
               f"{random.randint(10, 99)}-" \
               f"{random.randint(1000, 9999)}"
