python-logging-keyword-filter
---

# What is this?

A filter to remove credentials for Python standard logging library.

# How to use

```
import logging
from logging_keyword_filter import KeywordFilter


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addFilter(KeywordFilter('password'))


D = {
    'username': 'John Doe',
    'password': 'p@assword'
}


logger.info("%s", D)
# INFO:__main__:{'username': 'John Doe', 'password': '***censored***'}
```

# TODO

- [ ] refactor directory structure
- [ ] register to PyPI
