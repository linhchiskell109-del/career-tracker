import requests
from bs4 import BeautifulSoup


URL = "https://careers.mastercard.com/us/en/search-results"


def get_page():

    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    response.raise_for_status()

    return response.text


def parse():

    html = get_page()

    soup = BeautifulSoup(html, "lxml")

    print(soup.title.text.strip())


if __name__ == "__main__":
    parse()
