from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import GuitarAPWorld

# all regions excluding the origin
REGIONS = [
    "Early Game Piece 1",
    "Early Game Piece 2",
    "Early Game Piece 3",
    "Early Game Piece 4",
    "Early Game Piece 5",
    "Early Game Piece 6",
    "Early Game Piece 7",
    "Early Game Piece 8",
    "Mid Game Piece 1",
    "Mid Game Piece 2".
    "Mid Game Piece 3".
    "Late Game Piece 1",
    "Late Game Piece 2",
]


def create_and_connect_regions(world: GuitarAPWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: GuitarAPWorld) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    # the number of pieces is to be randomized and chosen from a pool of pieces later
    # this serves as a placeholder with the minimum amount of pieces
    early_game_piece_1 = Region("Early Game Piece 1", world.player, world.multiworld)
    early_game_piece_2 = Region("Early Game Piece 2", world.player, world.multiworld)
    early_game_piece_3 = Region("Early Game Piece 3", world.player, world.multiworld)
    early_game_piece_4 = Region("Early Game Piece 4", world.player, world.multiworld)
    early_game_piece_5 = Region("Early Game Piece 5", world.player, world.multiworld)
    early_game_piece_6 = Region("Early Game Piece 6", world.player, world.multiworld)
    early_game_piece_7 = Region("Early Game Piece 7", world.player, world.multiworld)
    early_game_piece_8 = Region("Early Game Piece 8", world.player, world.multiworld)
    mid_game_piece_1 = Region("Mid Game Piece 1", world.player, world.multiworld)
    mid_game_piece_2 = Region("Mid Game Piece 2", world.player, world.multiworld)
    mid_game_piece_3 = Region("Mid Game Piece 3", world.player, world.multiworld)
    late_game_piece_1 = Region("Late Game Piece 1", world.player, world.multiworld)
    late_game_piece_2 = Region("Late Game Piece 2", world.player, world.multiworld)

    regions = [
        menu,
        early_game_piece_1,
        early_game_piece_2,
        early_game_piece_3,
        early_game_piece_4,
        early_game_piece_5,
        early_game_piece_6,
        early_game_piece_7,
        early_game_piece_8,
        mid_game_piece_1,
        mid_game_piece_2,
        mid_game_piece_3,
        late_game_piece_1,
        late_game_piece_2,
    ]

    world.multiworld.regions += regions


def connect_regions(world: GuitarAPWorld) -> None:
    menu = world.get_region("Menu")

    # every piece is accesible from the menu
    for region_name in REGIONS:
        region_object = world.get_region(region_name)
        menu.connect(region_object, "Menu to " + region_name)

# connection rules are currently contained in rules.py, but should arguably
# be moved here once the pieces are finalized
