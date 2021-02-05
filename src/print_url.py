"""Prints a URL for querying the Coronavirus in the UK API.

For more information about this API, see:
<https://coronavirus.data.gov.uk/details/developers-guide>.
"""
import json
from urllib import parse

BASE_URL = "https://api.coronavirus.data.gov.uk/v1/data"

FILTERS = {
    "areaType": "overview",
}

STRUCTURE = {
    "areaType": "areaType",
    "areaName": "areaName",
    "date": "date",
    "newDeaths28DaysByPublishDate": "newDeaths28DaysByPublishDate",
    "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
}


def _filters() -> str:
    return ";".join(f"{k}={v}" for k, v in FILTERS.items())


def _structure() -> str:
    return json.dumps(STRUCTURE)


def make_url() -> str:
    params = parse.urlencode(
        {
            "filters": _filters(),
            "structure": _structure(),
        }
    )
    return f"{BASE_URL}?{params}"


if __name__ == "__main__":
    print(make_url())
