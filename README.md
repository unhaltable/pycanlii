pycanlii [![Travis CI][travis-badge]][travis] [![Code Health][landscape-badge]][landscape]
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

# Get the list of case databases
databases = canlii.cases_databases()
```

## Development Progress



Component | Status
----------|--------
legislationBrowse | Working
caseBrowse | Working
Search | NYI
caseCitatorTease| NYI


[travis-badge]:    http://img.shields.io/travis/sherlocke/pycanlii.svg?style=flat
[travis]:          https://travis-ci.org/sherlocke/pycanlii
[landscape-badge]: https://landscape.io/github/sherlocke/pycanlii/master/landscape.png?style=flat
[landscape]:       https://landscape.io/github/sherlocke/pycanlii/master
