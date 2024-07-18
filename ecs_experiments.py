from tcod.ecs import Registry

from position import Position

import numpy as np

InLevel = "InLevel"

registry = Registry()

player = registry.new_entity(components={
    Position: Position(0,0)
})

level1 = registry.new_entity(components={
    int: 1,
})

player.relation_tag[InLevel] = level1

print(set(registry.Q.all_of(relations=[(InLevel, level1)])) == {player})
print(level1.components[int])