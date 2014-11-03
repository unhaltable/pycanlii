pycanlii [![Travis CI][travis-badge]][travis] [![Code Health][landscape-badge]][landscape] [![Documentation Status][readthedocs-badge]][readthedocs]
========

Python API Wrapper for CanLII

## Installation

Install the package from PyPI:

    pip install pycanlii

## Usage

```python
from pycanlii import CanLII

canlii = CanLII('gHuBwvVx2VguA6meMfuXHGmy', language='en')

# Get the list of legislation databases
databases = canlii.legislation_databases()

# Print the title of all the legislation in the 5th database
for legislation in databases[4]:
    print(legislation.title)
    
# Get the list of case databases
cases = canlii.cases_databases()

# Get the 5th case in the 6th database
case = cases[5][4]

# Print the HTML content of that case
print(case.content)

# Search CanLII for a specfic case
case = canlii.search("Haldimand War Memorial Hospital", 1)[0]

# Get a list of the cases cited
cited_cases = case.citedCases()

# Print out the names of those cases
for case in cited_cases:
    print(case.title)
```


[travis-badge]:      http://img.shields.io/travis/sherlocke/pycanlii.svg?style=flat
[travis]:            https://travis-ci.org/sherlocke/pycanlii
[landscape-badge]:   https://landscape.io/github/sherlocke/pycanlii/master/landscape.png?style=flat
[landscape]:         https://landscape.io/github/sherlocke/pycanlii/master
[readthedocs-badge]: https://readthedocs.org/projects/pycanlii/badge/?version=latest
[readthedocs]:       https://readthedocs.org/projects/pycanlii/?badge=latest
