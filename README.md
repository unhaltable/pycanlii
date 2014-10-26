pycanlii
========

Python API Wrapper for CanLII

## Installation

Install the package from PyPI:

    pip install pycanlii

## Usage

```python
from pycanlii import CanLII

canlii = CanLII('gHuBwvVx2VguA6meMfuXHGmy', language='en')

# Get the list of databases
databases = canlii.legislation_databases()
```
