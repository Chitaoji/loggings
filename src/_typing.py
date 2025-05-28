"""
Contains typing classes.

NOTE: this module is not intended to be imported at runtime.

"""

import logging

logging.getLogger(__name__).warning(
    "importing from '%s' - this module is not intended to be imported at runtime, "
    "as unexpected errors may occur",
    __name__,
)
