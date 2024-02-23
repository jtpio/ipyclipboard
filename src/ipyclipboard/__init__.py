import pathlib

import anywidget
from traitlets import Unicode

from .__about__ import __version__


class Clipboard(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    value = Unicode("").tag(sync=True)
