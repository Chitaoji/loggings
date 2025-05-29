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
### v0.0.1
* Initial release.
