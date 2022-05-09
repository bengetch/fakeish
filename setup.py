from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fakeish",
    version="0.3.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pyyaml"],
    license="MIT",
    url="https://github.com/bengetch/fakeish",
    author="bengetch",
    author_email="bengetch@gmail.com",
    description="Faker but fast and dumb instead of slow and smart",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.5"
)
