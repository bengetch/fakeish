import random
from fakeish.objects import FIRST_NAMES_MALE, FIRST_NAMES_FEMALE, LAST_NAMES, EMAIL_DOMAINS


class RandomObject:
    FIRST_NAMES_NONBINARY = FIRST_NAMES_MALE + FIRST_NAMES_FEMALE

    @classmethod
    def email(cls, domain: [str, None] = None):

        if domain:
            return f"{random.sample(cls.FIRST_NAMES_NONBINARY, 1)[0]}" \
                   f"{random.sample(LAST_NAMES, 1)[0]}@{domain}".lower()
        else:
            return f"{random.sample(cls.FIRST_NAMES_NONBINARY, 1)[0]}" \
                   f"{random.sample(LAST_NAMES, 1)[0]}@{random.sample(EMAIL_DOMAINS, 1)[0]}".lower()
