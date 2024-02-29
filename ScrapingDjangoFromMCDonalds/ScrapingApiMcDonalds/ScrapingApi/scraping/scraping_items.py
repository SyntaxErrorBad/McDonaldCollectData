import requests
from bs4 import BeautifulSoup
from django.conf import settings


def scraping_take_items():
    response = requests.get(settings.URL_FOR_SCRAPING)
    soup = BeautifulSoup(response.content, "lxml")
    items = soup.select(".cmp-category__row .cmp-category__item")
    return items