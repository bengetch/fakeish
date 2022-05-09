from fakeish.utils import check_weight_and_return_sample
import random


class RandomObject:

    @staticmethod
    def ssn(blank: float = 0):
        return check_weight_and_return_sample(
            f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}",
            blank_weight=blank
        )

