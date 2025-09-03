# Provides the present version of VowpalWabbit

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("vowpalwabbit")
except PackageNotFoundError:
    __version__ = "unknown"
