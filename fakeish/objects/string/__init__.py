import random
import string


class RandomObject:

    @staticmethod
    def rand_string(s: [int, None] = 512):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(s))
