from collections.abc import Mapping
from typing import Any


from worlds.AutoWorld import World

from . import items, locations, regions, rules
from . import options as guitarap_options


class GuitarAPWorld(World):
    """
    IRL Guitar Archipelago is a game.
    """

    game = "IRL Guitar Archipelago"
    options_dataclass = guitarap_options.GuitarAPOptions
    options: GuitarAPOptions
    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_groups = {
        "Strings": {string for string in items.STRINGS},
        "Left Hand Fingers": {finger for finger in items.LEFT_HAND},
        "Right Hand Fingers", {finger for finger in items.RIGHT_HAND}
    }

    def generate_early(self) -> None:
        # Choose random starting items
        pass

    def create_regions(self) -> None:
        # Choose regions based on starting items
        pass

    def create_items(self) -> None:
        return items.create_all_items(self)

    def create_item(self, name: str) -> GuitarAPItem:
        return items.create_item_with_correct_classification(self, name)

    def create_event(self, name: str) -> GuitarAPItem:
        # do we need this?
        return GuitarAPItem(name, ItemClassification.Progression, None, self.player)

    def set_rules(self) -> None:
        pass

    def connect_entrances(self) -> None:
        pass

    def fill_slot_data(self) -> dict[str, Any]:
        # figure out what data needs to be transferred
        # data = {
        #     "seed": self.multiworld.seed_name,
        #     "slot": self.multiworld.player_name[self.player],
        #     "items": {location.name: location.item.name
        #               if location.item.player == self.player else "Remote"
        #               for location in self.multiworld.get_filled_locations(self.player)},
        #     "starter_items": [item.name for item in self.multiworld.precollected_items[self.player]],
        # }
        # return self.options.as_dict("str of relevant options")
        pass
