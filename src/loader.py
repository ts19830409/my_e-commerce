import json
import os
from typing import List

from src.utils import Category, Product


def read_json(path: str) -> list:
    """Функция чтения JSON-файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data  # type: ignore


def create_from_json(data: list) -> List[Category]:
    """Функция создания объектов из JSON-данных."""
    categories = []

    for category_data in data:
        products = []

        for product_data in category_data["products"]:
            # Создаём Product из словаря
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        category = Category(name=category_data["name"], description=category_data["description"], products=products)
        categories.append(category)

    return categories
