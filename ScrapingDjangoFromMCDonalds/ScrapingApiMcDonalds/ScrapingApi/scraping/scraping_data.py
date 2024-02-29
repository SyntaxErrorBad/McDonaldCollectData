import requests
from bs4 import BeautifulSoup
import json

from django.conf import settings

from ScrapingApi.scraping.scraping_items import scraping_take_items


def write_context_str(data_for_str):
    return "{} {}".format(data_for_str["value"], data_for_str["uom"])


def write_data_to_dict(data, product_id, product_data):
    try:
        item = product_data["item"]
        nutrient_facts = item["nutrient_facts"]["nutrient"]
        data[item["item_name"]] = {
            "description": item["description"],
            "nutrient_facts": {
                "calories": write_context_str(nutrient_facts[2]),
                "fats": write_context_str(nutrient_facts[3]),
                "carbs": write_context_str(nutrient_facts[5]),
                "proteins": write_context_str(nutrient_facts[7]),
                "unsaturated_fats": write_context_str(nutrient_facts[4]),
                "sugar": write_context_str(nutrient_facts[6]),
                "salt": write_context_str(nutrient_facts[8]),
                "portion": write_context_str(nutrient_facts[0])
            }
        }

    except Exception as e:
        data["error"] = {
            product_id: product_data["error"]["description"]
        }

    return data


def scraping_take_data(data_items):
    data = {}
    for item in data_items:
        product_id = item.get("data-product-id")
        product_data_response = requests.get((settings.URL_FOR_DATA).format(product_id))
        json_data = json.loads(product_data_response.content)
        write_data_to_dict(data = data, product_data = json_data, product_id = product_id)

    return data


def write_scraping_data():
    data = scraping_take_data(data_items = scraping_take_items())
    with open(settings.NAME_OF_JSON_FILE, "w", encoding = "utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False)
