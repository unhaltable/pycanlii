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

# Get the list of legislation in a database
legislations = canlii.legislations(database=databases[0])
# OR
legislations = canlii.legislations(database_id=databases[0]['databaseId'])

# Get metadata for a given legislation
legislation = canlii.legislation(legislation=legislations[0])
# OR
legislation = canlii.legislation(legislation_id=legislations[0]['legislationId'])
```
