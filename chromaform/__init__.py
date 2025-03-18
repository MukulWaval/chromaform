from .module1 import function1
from .module2 import Class1

__version__ = "0.1.0"  # Define the version
VERSION = __version__
VERSION_SHORT = __version__.split(".")[0]
__all__ = ["function1", "Class1"]
