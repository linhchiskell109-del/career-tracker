import json
from pathlib import Path

import requests

CONFIG_FILE = Path("companies.json")


def load_companies():
    """Load all enabled companies."""

    if not CONFIG_FILE.exists():
        raise FileNotFoundError("companies.json not found.")

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        companies = json.load(f)

    return [company for company in companies if company.get("enabled", True)]


def print_header():
    print("=" * 80)
    print("Career Tracker")
    print("=" * 80)


def test_connection(company):
    """Test whether the career website is reachable."""

    print(f"Company : {company['company']}")
    print(f"Platform: {company.get('platform', 'Unknown')}")
    print(f"URL     : {company['url']}")

    try:
        response = requests.get(
            company["url"],
            timeout=15,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/137.0 Safari/537.36"
                )
            },
        )

        print(f"Status  : {response.status_code}")
        print(f"Size    : {len(response.text):,} characters")

        if response.status_code == 200:
            print("Result  : Success")
        else:
            print("Result  : Failed")

    except Exception as e:
        print(f"Error   : {e}")

    print("-" * 80)


def main():
    print_header()

    companies = load_companies()

    print(f"\nLoaded {len(companies)} companies.\n")

    for company in companies:
        test_connection(company)

if __name__ == "__main__":
    main()
