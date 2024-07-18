from creature import Creature

from tcod.ecs.entity import Entity

from tags import IsPlayer, CanSee

class Player(Creature):
    def modify_entity(self, entity: Entity):
        entity.tags.add(IsPlayer)
        entity.relation_tag[CanSee] = entity