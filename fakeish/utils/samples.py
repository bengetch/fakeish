import random


def validate_blank_weight(weight: float):
    """
    Validate that the blank weight is between 0 and 1 inclusive
    """

    if not 0 <= weight <= 1:
        raise ValueError("Blank weight must be between 0 and 1 inclusive.")


def check_weight_and_return_sample(sample_value, blank_value="", blank_weight: float = 0):
    """
    Return either a blank value or a sample value with respect to some probability
    indicated by the blank_weight value
    """

    validate_blank_weight(blank_weight)
    return blank_value if random.uniform(0, 1) < blank_weight else sample_value


def check_weight_and_pop_sample(samples_list: list, blank_value="", blank_weight: float = 0) -> [str, int]:
    """
    Return either a blank value or the value of the next element in samples_list
    with respect to some probability indicated by the blank_weight value
    """

    validate_blank_weight(blank_weight)
    return blank_value if random.uniform(0, 1) < blank_weight else samples_list.pop()
