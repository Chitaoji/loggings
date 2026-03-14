# loggings
Provides more logging tools.

## Installation
```sh
$ pip install loggings
```

## Usage
```py
>>> import loggings

>>> loggings.warning("hello")
WARNING:root:hello

>>> loggings.get_logger("here", loggings.DEBUG).debug("hello")
DEBUG:here:hello
```

## See Also
### Github repository
* https://github.com/Chitaoji/loggings/

### PyPI project
* https://pypi.org/project/loggings/

## License
This project falls under the BSD 3-Clause License.

## History
### v0.0.6
* Updated core module docstring text to use the package name `loggings`.

### v0.0.5
* Added ANSI colorized output by log level for TTY streams.

### v0.0.4
* Updated the message logged by `log()` when `line_info` is True.

### v0.0.3
* New keyword-only argument `line_info` for `log()`, `debug()`, etc. 

### v0.0.2
* New function `log()`, which logs a message with the integer severity `level` on the module logger.

### v0.0.1
* Initial release.