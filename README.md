# fakeish
[faker](https://github.com/joke2k/faker) but fast and dumb instead of slow and smart

### Usage

To generate random but possibly overlapping data:
```python
from fakeish import Fakeish

f = Fakeish()
rand_ssn = f.ssn()
```


In order to generate data that is both random and non-overlapping, however, some light configuration is needed. The 
following code will 

```python
f = Fakeish()
f.configure_unique_samples_list("ssn", 50)

non_overlapping_ssns = [f.unique.ssn() for i in range(50)]
```

Configuration sample type can also be any of the following: emails, first_names, first_names_male, first_names_female, 
last_names, names, names_male, names_female. 

In order to generate the same random data each time, the `Fakeish` object can be seeded:

```python
f = Fakeish()
f.seed(<int>)
# configure / generate data here
```