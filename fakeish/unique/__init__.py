from fakeish import objects
from itertools import product
import random


class ObjectLists:

    EMAILS_LIST = []
    EMAILS_CONFIGURED = False

    FIRST_NAMES_NONBINARY_LIST = []
    FIRST_NAMES_NONBINARY_CONFIGURED = False

    FIRST_NAMES_MALE_LIST = []
    FIRST_NAMES_MALE_CONFIGURED = False

    FIRST_NAMES_FEMALE_LIST = []
    FIRST_NAMES_FEMALE_CONFIGURED = False

    LAST_NAMES_LIST = []
    LAST_NAMES_CONFIGURED = False

    NAMES_NONBINARY_LIST = []
    NAMES_NONBINARY_CONFIGURED = False

    NAMES_MALE_LIST = []
    NAMES_MALE_CONFIGURED = False

    NAMES_FEMALE_LIST = []
    NAMES_FEMALE_CONFIGURED = False

    SSNS_LIST = []
    SSNS_CONFIGURED = False

    @staticmethod
    def check_length_return_samples(samples_list: [list, range], requested_length: int = None):

        if requested_length is not None:
            if len(samples_list) < requested_length:
                raise ValueError(f"Number of rows requested exceeds total possible combinations ({len(samples_list)})")
        return random.sample(samples_list, requested_length)

    @classmethod
    def configure_emails_list(cls, num_rows: int = None, domains: list = None):

        all_samples = [
            f"{x[0]}{x[1]}@{x[2]}" for x
            in product(
                objects.FIRST_NAMES_NONBINARY, objects.LAST_NAMES,
                objects.EMAIL_DOMAINS if not domains else domains
            )
        ]

        cls.EMAILS_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.EMAILS_CONFIGURED = True

    @classmethod
    def configure_first_names_list(cls, num_rows: int = None):

        all_samples = objects.FIRST_NAMES_NONBINARY

        cls.FIRST_NAMES_NONBINARY_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.FIRST_NAMES_NONBINARY_CONFIGURED = True

    @classmethod
    def configure_first_names_male_list(cls, num_rows: int = None):

        all_samples = objects.FIRST_NAMES_MALE

        cls.FIRST_NAMES_MALE_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.FIRST_NAMES_MALE_CONFIGURED = True

    @classmethod
    def configure_first_names_female_list(cls, num_rows: int = None):

        all_samples = objects.FIRST_NAMES_FEMALE

        cls.FIRST_NAMES_FEMALE_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.FIRST_NAMES_FEMALE_CONFIGURED = True

    @classmethod
    def configure_last_names_list(cls, num_rows: int = None):

        all_samples = objects.LAST_NAMES

        cls.LAST_NAMES_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.LAST_NAMES_CONFIGURED = True

    @classmethod
    def configure_names_list(cls, num_rows: int = None):

        all_samples = [
            f"{name[0]} {name[1]}" for name
            in product(objects.FIRST_NAMES_NONBINARY, objects.LAST_NAMES)
        ]

        cls.NAMES_NONBINARY_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.NAMES_NONBINARY_CONFIGURED = True

    @classmethod
    def configure_names_male_list(cls, num_rows: int = None):

        all_samples = [
            f"{name[0]} {name[1]}" for name
            in product(objects.FIRST_NAMES_MALE, objects.LAST_NAMES)
        ]

        cls.NAMES_MALE_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.NAMES_MALE_CONFIGURED = True

    @classmethod
    def configure_names_female_list(cls, num_rows: int = None):

        all_samples = [
            f"{name[0]} {name[1]}" for name
            in product(objects.FIRST_NAMES_FEMALE, objects.LAST_NAMES)
        ]

        cls.NAMES_FEMALE_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.NAMES_FEMALE_CONFIGURED = True

    @classmethod
    def configure_ssns_list(cls, num_rows: int = None):

        all_samples = range(100000000, 999999999)

        cls.SSNS_LIST = cls.check_length_return_samples(all_samples, num_rows)
        cls.SSNS_CONFIGURED = True
