from fakeish.unique import ObjectLists
from fakeish.utils import check_weight_and_pop_sample


class RandomObject:

    @classmethod
    def ssn(cls, blank: float = 0) -> str:

        if not ObjectLists.SSNS_CONFIGURED:
            raise ValueError("Unique SSN sample list not yet configured.")

        if len(ObjectLists.SSNS_LIST) > 0:
            ssn = check_weight_and_pop_sample(ObjectLists.SSNS_LIST, blank_weight=blank)
            return ssn if ssn == "" else f"{str(ssn)[:3]}-{str(ssn)[3:5]}-{str(ssn)[5:9]}"
        else:
            raise ValueError("List of unique SSNs has been exhausted.")
