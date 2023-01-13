import pytest

import ssbgrid

known_places = [
    # Galdhøpiggen 1km
    ((145_996, 6_851_887), 21450006851000, {"grid_cell_size": 1_000}),
    # Galdhøpiggen 5km
    ((145_996, 6_851_887), 21450006850000, {"grid_cell_size": 5_000}),
]

known_grids = [
    # Galdhøpiggen grid 1km
    (21450006851000, (145_000, 6_851_000), {"grid_cell_size": 1_000}),
    (21450006851000, (145_500, 6_851_500), {"grid_cell_size": 1_000, "centroid": True}),
    # Galdhøpiggen grid 5km
    (21450006850000, (145_000, 6_850_000), {"grid_cell_size": 5_000}),
    (21450006850000, (147_500, 6_852_500), {"grid_cell_size": 5_000, "centroid": True}),
]


@pytest.mark.parametrize("utm, id, keyword_arguments", known_places)
def test_utm_to_id(utm, id, keyword_arguments):
    assert id == ssbgrid.utm_to_id(*utm, **keyword_arguments)


@pytest.mark.parametrize("id, utm, keyword_arguments", known_grids)
def test_id_to_utm(id, utm, keyword_arguments):
    assert utm == ssbgrid.id_to_utm(id, **keyword_arguments)
