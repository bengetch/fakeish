from fakeish.unique import ObjectLists
from fakeish.utils import check_weight_and_pop_sample


class RandomObject:

    @classmethod
    def first_name(cls, blank: float = 0) -> str:

        if not ObjectLists.FIRST_NAMES_NONBINARY_CONFIGURED:
            raise AttributeError("Unique first names list not yet configured.")

        if len(ObjectLists.FIRST_NAMES_NONBINARY_LIST) > 0:
            return check_weight_and_pop_sample(ObjectLists.FIRST_NAMES_NONBINARY_LIST, blank_weight=blank)
        else:
            raise ValueError("List of unique first names has been exhausted.")

    @classmethod
    def first_name_male(cls, blank: float = 0) -> str:

        if not ObjectLists.FIRST_NAMES_MALE_CONFIGURED:
            raise AttributeError("Unique male first names list not yet configured.")

        if len(ObjectLists.FIRST_NAMES_MALE_LIST) > 0:
            return check_weight_and_pop_sample(ObjectLists.FIRST_NAMES_MALE_LIST, blank_weight=blank)
        else:
            raise ValueError("List of unique male first names has been exhausted.")

    @classmethod
    def first_name_female(cls, blank: float = 0) -> str:

        if not ObjectLists.FIRST_NAMES_FEMALE_CONFIGURED:
            raise AttributeError("Unique female first names list not yet configured.")

        if len(ObjectLists.FIRST_NAMES_FEMALE_LIST) > 0:
            return check_weight_and_pop_sample(ObjectLists.FIRST_NAMES_FEMALE_LIST, blank_weight=blank)
        else:
            raise ValueError("List of unique female first names has been exhausted.")

    @classmethod
    def last_name(cls, blank: float = 0) -> str:

        if not ObjectLists.LAST_NAMES_CONFIGURED:
            raise AttributeError("Unique last names list not yet configured.")

        if len(ObjectLists.LAST_NAMES_LIST) > 0:
            return check_weight_and_pop_sample(ObjectLists.LAST_NAMES_LIST, blank_weight=blank)
        else:
            raise ValueError("List of unique last names has been exhausted.")

    @classmethod
    def name(cls, blank: float = 0) -> str:

        if not ObjectLists.NAMES_NONBINARY_CONFIGURED:
            raise AttributeError("Unique names list not yet configured.")

        if len(ObjectLists.NAMES_NONBINARY_LIST) > 0:
            return check_weight_and_pop_sample(ObjectLists.NAMES_NONBINARY_LIST, blank_weight=blank)
        else:
            raise ValueError("List of unique names has been exhausted.")

    @classmethod
    def name_male(cls, blank: float = 0) -> str:

        if not ObjectLists.NAMES_MALE_CONFIGURED:
            raise AttributeError("Unique male names list not yet configured.")

        if len(ObjectLists.NAMES_MALE_LIST) > 0:
            return check_weight_and_pop_sample(ObjectLists.NAMES_MALE_LIST, blank_weight=blank)
        else:
            raise ValueError("List of unique male names has been exhausted.")

    @classmethod
    def name_female(cls, blank: float = 0) -> str:

        if not ObjectLists.NAMES_FEMALE_CONFIGURED:
            raise AttributeError("Unique female names list not yet configured.")

        if len(ObjectLists.NAMES_FEMALE_LIST) > 0:
            return check_weight_and_pop_sample(ObjectLists.NAMES_FEMALE_LIST, blank_weight=blank)
        else:
            raise ValueError("List of unique female names has been exhausted.")
