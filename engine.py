from tcod import ecs, console, context
from numpy import ndarray

from game_map import generate_game_map

from position import Position
from graphic import Graphic

from tags import IsPlayer, CanSee

from player import Player

def getplayer(registry: ecs.Registry):
    return registry.Q.all_of(tags=[IsPlayer])

class Engine:
    def __init__(self, map_width, map_height) -> None:
        self.registry = ecs.Registry()

        self.game_map = generate_game_map(self.registry, map_width, map_height)

        Player(name="David", hp=10).spawn(1,1, self.registry)

    def render(self, console: console.Console, context: context.Context):

        # Render the tilemap onto the screen at a position based on offset
        console.rgb[
            0:self.game_map.components[("width", int)],
            0:self.game_map.components[("height", int)]
        ] = self.game_map.components[ndarray]["dark"]

        # Render all entities with "visible" tag
        for e in self.registry.Q.all_of(
            relations=[(getplayer(self.registry), CanSee, None)]
        ):
            x = e.components[Position].x
            y = e.components[Position].y
            e.components[Graphic].render(x, y, console)

        # Present the new console to the screen
        context.present(console)

    def do_player_turn(self):
        pass

    def do_enemy_turns(self):
        pass

    def do_one_turn(self, console: console.Console, context: context.Context):
        self.render(console, context)
        self.do_player_turn()
        self.do_enemy_turns()
        
