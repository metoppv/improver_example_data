from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

try:
    __version__ = version("improver_example_data")
except PackageNotFoundError:
    # package is not installed
    pass

# Root directory for test data.
path = Path(__file__).resolve().parent
