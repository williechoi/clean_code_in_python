# decorator_function_1.py

import logging
from functools import wraps

RETRIES_LIMIT = 3


class ControlledException(Exception):
    """ A generic exception on the program's domain."""


def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                logging.info("retrying %s", operation.__qualname__)
                last_raised = e

        raise last_raised

    return wrapped


@retry
def run_operation(task):
    """Run a particular task, simulating some failures on its exception."""
    return task.run()

# run_operation = retry(run_operation)
