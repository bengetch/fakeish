import random
import string


class RandomObject:

    @staticmethod
    def rand_string(s: [int, None] = 512, blank: float = 0):
        if blank > 0 and random.uniform(0, 1) < blank:
            return ""
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(s))
