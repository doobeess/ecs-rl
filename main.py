#!/usr/bin/env python3
import tcod

from engine import Engine

def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "font.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        
        map_width = 60
        map_height = 40

        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        engine = Engine(map_width, map_height)

        while True:
            root_console.print(x=1, y=1, string="@")

            context.present(root_console)
            engine.do_one_turn(root_console, context)
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()