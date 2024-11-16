from dataclasses import dataclass
import requests

@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str | None
    address_1: str
    address_2: str | None
    address_3: str | None
    city: str | None
    state_province: str | None
    postal_code: str | None
    country: str | None
    longitude: float | None
    latitude: float | None
    phone: int | None
    website_url: str | None
    state: str | None
    street:str | None


if __name__ == "__main__":
    count = 20
    url = f"https://api.openbrewerydb.org/v1/breweries?per_page={count}"

    response = requests.get(url).json()

    breweries: list[Brewery] = []
    for obj in response:
        print(obj)
        obj["latitude"] = float(obj["latitude"]) if obj["latitude"] is not None else None
        obj["longitude"] = float(obj["longitude"]) if obj["longitude"] is not None else None
        obj["phone"] = int(obj["phone"]) if obj["phone"] is not None else None

        breweries.append(Brewery(**obj))

    for brewery in breweries:
        print(brewery)