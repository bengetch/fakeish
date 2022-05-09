from fakeish.factory import Factory
from fakeish.unique.email import ObjectLists
import random


UNIQUE_CONFIG_MAP = {
    "emails": ObjectLists.configure_emails_list,
    "first_names": ObjectLists.configure_first_names_list,
    "first_names_male": ObjectLists.configure_first_names_male_list,
    "first_names_female": ObjectLists.configure_first_names_female_list,
    "last_names": ObjectLists.configure_last_names_list,
    "names": ObjectLists.configure_names_list,
    "names_male": ObjectLists.configure_names_male_list,
    "names_female": ObjectLists.configure_names_female_list,
    "ssn": ObjectLists.configure_ssns_list,
    "ssns": ObjectLists.configure_ssns_list
}


class Unique:
    def __init__(self):
        self._factory = Factory("fakeish.unique")

    def __getattr__(self, attr):
        return getattr(self._factory, attr)


class Fakeish:
    def __init__(self):
        self._factory = Factory("fakeish.objects")
        self.unique = Unique()

    @staticmethod
    def seed(seed: [int, None]):
        random.seed(seed)

    def __getattr__(self, attr):
        return getattr(self._factory, attr)

    @staticmethod
    def configure_unique_samples_list(samples_type: str, num_samples: int = None, **kwargs):

        if UNIQUE_CONFIG_MAP.get(samples_type) is None:
            raise KeyError(
                f"Unrecognized samples type: '{samples_type}'. The following types are accepted: "
                f"{', '.join(k for k in UNIQUE_CONFIG_MAP.keys())}")
        else:
            UNIQUE_CONFIG_MAP[samples_type](num_rows=num_samples, **kwargs)
