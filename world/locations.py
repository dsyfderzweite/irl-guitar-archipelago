from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items, regions

if TYPE_CHECKING:
    from .world import GuitarAPWorld

LOCATIONS = [
    "Early Game Check 1",
    "Early Game Check 2",
    "Early Game Check 3",
    "Early Game Check 4",
    "Early Game Check 5",
    "Early Game Check 6",
    "Early Game Check 7",
    "Early Game Check 8",
    "Mid Game Check 1",
    "Mid Game Check 2",
    "Mid Game Check 3",
    "Mid Game Check 4",
    "Mid Game Check 5",
    "Mid Game Check 6",
    "Late Game Check 1",
    "Late Game Check 2",
    "Late Game Check 3",
    "Late Game Check 4",
]

LOCATION_NAME_TO_ID = {
    "Early Game Check 1": 1,
    "Early Game Check 2": 2,
    "Early Game Check 3": 3,
    "Early Game Check 4": 4,
    "Early Game Check 5": 5,
    "Early Game Check 6": 6,
    "Early Game Check 7": 7,
    "Early Game Check 8": 8,
    "Mid Game Check 1": 9,
    "Mid Game Check 2": 10,
    "Mid Game Check 3": 11,
    "Mid Game Check 4": 12,
    "Mid Game Check 5": 13,
    "Mid Game Check 6": 14,
    "Late Game Check 1": 15,
    "Late Game Check 2": 16,
    "Late Game Check 3": 17,
    "Late Game Check 4": 18,
}


class GuitarAPLocation(Location):
    game = "GuitarAP"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: GuitarAPWorld) -> None:
    # early game locations
    # need to be very careful with this hard coded slicing
    for early_game_piece_name, i in zip(regions.REGIONS[0:8], range(0, 8)):
        early_game_piece_object = world.get_region(early_game_piece_name)
        early_game_piece_locations = get_location_names_with_ids(LOCATIONS[i:i+1])
        early_game_piece_object.add_locations(early_game_piece_locations, GuitarAPLocation)

    # mid and late game locations
    # again, need to be careful with the slices
    for latter_game_piece_name, i in zip(regions.REGIONS[8:13], range(8, 18, 2)):
        latter_game_piece_object = world.get_region(early_game_piece_name)
        latter_game_piece_locations = get_location_names_with_ids(LOCATIONS[i:i+2])
        latter_game_piece_object.add_locations(latter_game_piece_locations, GuitarAPLocation)        

    # event locations (clearing pieces)
    for piece_name in regions.REGIONS:
        piece_object = world.get_region(piece_name)
        piece_object.add_event(
            "Piece Clear Event", "Piece Clear", location_type=GuitarAPLocation, item_type=GuitarAPItem
        )
