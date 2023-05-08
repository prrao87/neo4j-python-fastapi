import os
import sys

from src.api.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_search():
    with TestClient(app) as client:
        response = client.get("/v1/rest/search?terms=chardonnay&max_price=100")
        assert response.status_code == 200
        sample = response.json()[0]
        assert isinstance(sample["wineID"], int)
        assert isinstance(sample["price"], float)
        assert isinstance(sample["points"], int)
        assert "country" in sample
        assert sample["price"] <= 100.0


def test_top_by_country():
    with TestClient(app) as client:
        response = client.get("/v1/rest/top_by_country?country=new%20zealand")
        assert response.status_code == 200
        first_sample = response.json()[0]
        last_sample = response.json()[-1]
        assert isinstance(first_sample["wineID"], int)
        assert isinstance(first_sample["price"], float)
        assert isinstance(first_sample["points"], int)
        assert first_sample["country"] == "New Zealand"
        # Test sorting
        assert first_sample["points"] >= last_sample["points"]


def test_top_by_province():
    with TestClient(app) as client:
        response = client.get("/v1/rest/top_by_province?province=oregon")
        assert response.status_code == 200
        first_sample = response.json()[0]
        last_sample = response.json()[-1]
        assert isinstance(first_sample["wineID"], int)
        assert isinstance(first_sample["price"], float)
        assert isinstance(first_sample["points"], int)
        assert first_sample["province"] == "Oregon"
        assert first_sample["country"] == "US"
        # Test sorting
        assert first_sample["points"] >= last_sample["points"]


def test_most_by_variety():
    with TestClient(app) as client:
        response = client.get("/v1/rest/most_by_variety?variety=pinot%20noir&points=85")
        assert response.status_code == 200
        assert len(response.json()) > 0
        first_sample = response.json()[0]
        last_sample = response.json()[-1]
        # Test sorting
        assert first_sample["wineCount"] >= last_sample["wineCount"]
