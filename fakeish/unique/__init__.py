import random
from itertools import product
from fakeish import objects

class RandomObject:
    def __init__(self, num_rows: int):
        self.email_list = [''.join(x) for x in product(objects.FIRST_NAMES_NONBINARY, objects.LAST_NAMES, ['@'], objects.EMAIL_DOMAINS)]
        if len(self.email_list) < num_rows:
            raise ValueError("Not enough values in fakeish to generate " + str(num_rows) + " unique emails")
        random.shuffle(self.email_list)
        self.email_list = self.email_list[:num_rows]

        self.counter = 0
        self.max_rows = num_rows
    
    def email(self, blank: float = 0) -> str:
        if blank > 0 and random.uniform(0, 1) < blank:
            return ""
        if len(self.email_list) > 0:
            return self.email_list.pop()
        else:
            return 0