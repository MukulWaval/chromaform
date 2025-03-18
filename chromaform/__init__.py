from .module1 import function1
from .module2 import Class1
import logging

# Setup logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = "0.1.0"  # Define the version
VERSION = __version__
VERSION_SHORT = __version__.split(".")[0]
__all__ = ["function1", "Class1"]
