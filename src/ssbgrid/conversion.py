import math

FALSE_EASTING = 2_000_000


def utm_to_id(easting: int, northing: int, grid_cell_size=1000) -> int:
    easting, northing = allign_to_grid(easting, northing, grid_cell_size)
    return 20_000_000_000_000 + (easting * 10_000_000) + northing


def id_to_utm(ssb_grid_id: int, grid_cell_size=1000) -> tuple[int, int]:
    easting = int(
        math.floor(ssb_grid_id * (10 ** (-7))) - (2 * (10**6)) + (grid_cell_size / 2)
    )
    northing = int(
        ssb_grid_id
        - (math.floor(ssb_grid_id * (10 ** (-7))) * (10**7))
        + (grid_cell_size / 2)
    )
    return easting, northing


def allign_to_grid(easting: int, northing: int, grid_cell_size=1000) -> tuple[int, int]:
    return (
        math.floor((easting + FALSE_EASTING) / grid_cell_size) * grid_cell_size
        - FALSE_EASTING,
        math.floor(northing / grid_cell_size) * grid_cell_size,
    )
