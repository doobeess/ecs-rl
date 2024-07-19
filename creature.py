from tcod import ecs
from position import Position
from graphic import Graphic

class Creature:
    def __init__(self, name: str=None, graphic: Graphic=Graphic("@", (255,255,255), (0,0,0)), hp: int=None):
        self.name = name
        self.graphic = graphic
        self.hp = hp

    def spawn(self, x, y, registry: ecs.Registry):
        entity =  registry.new_entity(
            components = {
                Position: Position(x,y),
                Graphic: self.graphic,
                ("name", str): self.name,
                ("hp", int): self.hp,
            }
        )

        self.modify_entity(entity)

    def modify_entity(self, entity):
        # By default nothing happens here; method overriden by subclasses 
        # for child-specific modifications
        pass 