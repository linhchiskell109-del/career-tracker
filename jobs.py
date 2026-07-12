import json
from pathlib import Path

CONFIG_FILE = Path("companies.json")


def load_companies():
    """Load all enabled companies from companies.json."""

    if not CONFIG_FILE.exists():
        raise FileNotFoundError("companies.json not found.")

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        companies = json.load(f)

    return [company for company in companies if company.get("enabled", True)]


def print_header():
    print("=" * 70)
    print("Career Tracker")
    print("=" * 70)


def print_companies(companies):
    print(f"\nMonitoring {len(companies)} companies:\n")

    for index, company in enumerate(companies, start=1):
        print(f"[{index}] {company['company']}")
        print(f"Platform : {company.get('platform', 'Unknown')}")
        print(f"URL      : {company['url']}")
        print()


def main():
    print_header()

    companies = load_companies()

    print_companies(companies)

    print("Configuration loaded successfully.")


if __name__ == "__main__":
    main()
