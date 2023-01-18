from enum import IntEnum
from typing import Generator


class StandardGrid(IntEnum):
    SSB100M = 100
    SSB125M = 125
    SSB250M = 250
    SSB500M = 500
    SSB1KM = 1_000
    SSB5KM = 5_000
    SSB10KM = 10_000
    SSB25KM = 25_000
    SSB50KM = 50_000
    SSB100KM = 100_000
    SSB250KM = 250_000
    SSB500KM = 500_000

    @classmethod
    def get_sizes(cls) -> Generator[int, None, None]:
        return (int(grid) for grid in cls)
