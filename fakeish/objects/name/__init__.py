import random
from fakeish.objects import FIRST_NAMES_MALE, FIRST_NAMES_FEMALE, LAST_NAMES


class RandomObject:
    FIRST_NAMES_NONBINARY = FIRST_NAMES_MALE + FIRST_NAMES_FEMALE

    @classmethod
    def first_name(cls):
        return f"{random.sample(cls.FIRST_NAMES_NONBINARY, 1)[0]}"

    @staticmethod
    def first_name_male():
        return f"{random.sample(FIRST_NAMES_MALE, 1)[0]}"

    @staticmethod
    def first_name_female():
        return f"{random.sample(FIRST_NAMES_FEMALE, 1)[0]}"

    @staticmethod
    def last_name():
        return f"{random.sample(LAST_NAMES, 1)[0]}"

    @classmethod
    def name(cls):
        return f"{cls.first_name()} {cls.last_name()}"

    @classmethod
    def name_male(cls):
        return f"{cls.first_name_male()} {cls.last_name()}"

    @classmethod
    def name_female(cls):
        return f"{cls.first_name_female()} {cls.last_name()}"
