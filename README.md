# loggerlib
Provides more logging tools.

## Installation
```sh
$ pip install loggerlib
```

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

## History
### v0.0.1
* Initial release.