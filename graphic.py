import attrs

from typing import Tuple

from tcod import console

@attrs.define
class Graphic:
    char: str
    fg: Tuple[int, int, int]
    bg: Tuple[int, int, int]

    def render(self, x, y, console: console.Console):
        console.print(x, y, self.char, self.fg, self.bg)