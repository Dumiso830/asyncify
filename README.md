# asyncify

A Python library that wraps any sync function with automatic async support.

[![CI](https://github.com/dumiso-mshanga/asyncify/workflows/CI/badge.svg)](https://github.com/dumiso-mshanga/asyncify/actions)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Installation

```bash
pip install asyncify
```

### Usage

```python
from asyncify import asyncify

@asyncify
def sync_function(x):
    return x + 1

# Now you can use sync_function as if it were an async function
```

### Examples

See the `examples/` directory for more detailed examples.
