import yaml
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
FIRST_NAMES_MALE = yaml.safe_load(open(f"{BASE_PATH}/_samples/first_male.yml").read())
FIRST_NAMES_FEMALE = yaml.safe_load(open(f"{BASE_PATH}/_samples/first_female.yml").read())
LAST_NAMES = yaml.safe_load(open(f"{BASE_PATH}/_samples/last.yml").read())
EMAIL_DOMAINS = yaml.safe_load(open(f"{BASE_PATH}/_samples/email_domains.yml").read())
FIRST_NAMES_NONBINARY = FIRST_NAMES_MALE + FIRST_NAMES_FEMALE
