from fakeish.unique import ObjectLists
from fakeish.utils import check_weight_and_pop_sample


class RandomObject:

    @classmethod
    def email(cls, blank: float = 0) -> str:

        if not ObjectLists.EMAILS_CONFIGURED:
            raise ValueError("Unique emails sample list not yet configured.")

        if len(ObjectLists.EMAILS_LIST) > 0:
            return check_weight_and_pop_sample(ObjectLists.EMAILS_LIST, blank_weight=blank)
        else:
            raise ValueError("List of unique emails has been exhausted.")
