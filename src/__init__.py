"""
# loggerlib
A template repository for building python packages. Please replace `$package` with the
package's name in `metadata.yml`.

## Usage
```py
>>> import loggerlib as log

>>> log.warning("hello")
WARNING:root:hello

>>> log.get_logger("here", log.DEBUG).debug("hello")
DEBUG:here:hello
```

## See Also
### Github repository
* https://github.com/Chitaoji/loggerlib/

### PyPI project
* https://pypi.org/project/loggerlib/

## License
This project falls under the BSD 3-Clause License.

"""

from typing import List

from . import core
from .__version__ import __version__
from .core import *

__all__: List[str] = []
__all__.extend(core.__all__)
