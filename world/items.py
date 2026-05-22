from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import GuitarAPWorld

STRINGS = [
    "1st String (e')",
    "2nd String (b)",
    "3rd String (g)",
    "4th String (d)",
    "5th String (A)",
    "6th String (E)",
    ]

LEFT_HAND = [
    "Left Hand Index Finger (1)",
    "Left Hand Middle Finger (2)",
    "Left Hand Ring Finger (3)",
    "Left Hand Pinky Finger (4)",
    ]

RIGHT_HAND = [
    "Right Hand Thumb (p)",
    "Right Hand Index Finger (i)",
    "Right Hand Middle Finger (m)",
    "Right Hand Ring Finger (a)",
    ]

ITEM_NAME_TO_ID = {
    "1st String (e')": 1,
    "2nd String (b)": 2,
    "3rd String (g)": 3,
    "4th String (d)": 4,
    "5th String (A)": 5,
    "6th String (E)": 6,
    "Left Hand Index Finger (1)": 7,
    "Left Hand Middle Finger (2)": 8,
    "Left Hand Ring Finger (3)": 9,
    "Left Hand Pinky Finger (4)": 10,
    "Right Hand Thumb (p)": 11,
    "Right Hand Index Finger (i)": 12,
    "Right Hand Middle Finger (m)": 13,
    "Right Hand Ring Finger (a)": 14,
    "Encouragement": 15,
    "Lick Trap": 16,
    }

DEFAULT_ITEM_CLASSIFICATION = {
    "1st String (e')": ItemClassification.progression,
    "2nd String (b)": ItemClassification.progression,
    "3rd String (g)": ItemClassification.progression,
    "4th String (d)": ItemClassification.progression,
    "5th String (A)": ItemClassification.progression,
    "6th String (E)": ItemClassification.progression,
    "Left Hand Index Finger (1)": ItemClassification.progression,
    "Left Hand Middle Finger (2)": ItemClassification.progression,
    "Left Hand Ring Finger (3)": ItemClassification.progression,
    "Left Hand Pinky Finger (4)": ItemClassification.progression,
    "Right Hand Thumb (p)": ItemClassification.progression,
    "Right Hand Index Finger (i)": ItemClassification.progression,
    "Right Hand Middle Finger (m)": ItemClassification.progression,
    "Right Hand Ring Finger (a)": ItemClassification.progression,
    "Encouragement": ItemClassification.filler,
    "Lick Trap": ItemClassification.trap,
    }


class GuitarAPItem(Item):
    game = "GuitarAP"


def get_random_filler_item_name(world: APQuestWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        return "Lick Trap"
    return "Encouragement"

def create_item_with_correct_classification(world: APQuestWorld, name: str) -> APQuestItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return APQuestItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: GuitarAPWorld) -> None:
    itempool: list[Item] = [world.create_item(item) for item in STRINGS + LEFT_HAND + RIGHT_HAND]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
