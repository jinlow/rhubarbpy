from .loopsum import loopsum
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("rhubarbpy")
except PackageNotFoundError:
    pass