import random
import yaml
import os


class RandomObject:
    BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    FIRST_NAMES_MALE = yaml.safe_load(open(f"{BASE_PATH}/samples/first_male.yml").read())
    FIRST_NAMES_FEMALE = yaml.safe_load(open(f"{BASE_PATH}/samples/first_female.yml").read())
    FIRST_NAMES_NONBINARY = FIRST_NAMES_MALE + FIRST_NAMES_FEMALE
    LAST_NAMES = yaml.safe_load(open(f"{BASE_PATH}/samples/last.yml").read())

    @classmethod
    def first_name(cls):
        return f"{random.sample(cls.FIRST_NAMES_NONBINARY, 1)[0]}"

    @classmethod
    def first_name_male(cls):
        return f"{random.sample(cls.FIRST_NAMES_MALE, 1)[0]}"

    @classmethod
    def first_name_female(cls):
        return f"{random.sample(cls.FIRST_NAMES_FEMALE, 1)[0]}"

    @classmethod
    def last_name(cls):
        return f"{random.sample(cls.LAST_NAMES, 1)[0]}"

    @classmethod
    def name(cls):
        return f"{cls.first_name()} {cls.last_name()}"

    @classmethod
    def name_male(cls):
        return f"{cls.first_name_male()} {cls.last_name()}"

    @classmethod
    def name_female(cls):
        return f"{cls.first_name_female()} {cls.last_name()}"
