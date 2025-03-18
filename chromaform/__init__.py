import logging

# Setup logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Import key functions/classes
from .module1 import function1
from .module2 import Class1

__version__ = "0.1.0"
__all__ = ["function1", "Class1"]
