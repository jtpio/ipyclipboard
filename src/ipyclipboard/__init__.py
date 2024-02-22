import importlib.metadata
import pathlib

import anywidget
from traitlets import Unicode

try:
    __version__ = importlib.metadata.version("ipyclipboard")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class Clipboard(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    value = Unicode("").tag(sync=True)
