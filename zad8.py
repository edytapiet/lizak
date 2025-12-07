import requests
import argparse
from typing import Optional


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street: Optional[str],
        city: str,
        state: Optional[str],
        postal_code: Optional[str],
        country: Optional[str],
        phone: Optional[str],
        website_url: Optional[str]
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (
            f"Brewery: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"City: {self.city}\n"
            f"Street: {self.street}\n"
            f"Website: {self.website_url}\n"
            f"{'-'*40}"
        )


def fetch_breweries(city: Optional[str]):
    base_url = "https://api.openbrewerydb.org/v1/breweries"

    if city:
        url = f"{base_url}?by_city={city}&per_page=20"
    else:
        url = f"{base_url}?per_page=20"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    parser = argparse.ArgumentParser(description="Fetch brewery data.")
    parser.add_argument("--city", type=str, help="City to filter breweries")
    args = parser.parse_args()

    data = fetch_breweries(args.city)

    breweries = [
        Brewery(
            id=item.get("id"),
            name=item.get("name"),
            brewery_type=item.get("brewery_type"),
            street=item.get("street"),
            city=item.get("city"),
            state=item.get("state"),
            postal_code=item.get("postal_code"),
            country=item.get("country"),
            phone=item.get("phone"),
            website_url=item.get("website_url"),
        )
        for item in data
    ]

    for brewery in breweries:
        print(brewery)


if __name__ == "__main__":
    main()
