import pytest
from schemas.wine import Wine


@pytest.fixture(scope="session")
def data():
    example = {
        "points": 90,
        "title": "Castello San Donato in Perano 2009 Riserva  (Chianti Classico)",
        "description": "Made from a blend of 85% Sangiovese and 15% Merlot, this ripe wine delivers soft plum, black currants, clove and cracked pepper sensations accented with coffee and espresso notes. A backbone of firm tannins give structure. Drink now through 2019.",
        "taster_name": "Kerin O'Keefe",
        "taster_twitter_handle": "@kerinokeefe",
        "price": 30.0,
        "designation": "Riserva",
        "variety": "Red Blend",
        "region_1": "Chianti Classico",
        "region_2": "Monti del Chianti",
        "province": "Tuscany",
        "country": "Italy",
        "winery": "Castello San Donato in Perano",
        "id": 40825
    }
    return example


# Test pydantic schema validation for wine items
def test_wine_schema(data):
    wine = Wine(**data)
    assert isinstance(wine.country, str)
    assert isinstance(wine.points, int)
    assert -1 < wine.points < 101
    assert isinstance(wine.price, float)
    assert wine.price > 0
    assert isinstance(wine.id, int)
    assert all(
        isinstance(item, str)
        for item in [
            wine.country,
            wine.province,
            wine.description,
            wine.vineyard,
            wine.region_1,
            wine.region_2,
            wine.taster_name,
            wine.taster_twitter_handle,
            wine.title,
            wine.variety,
        ]
    )