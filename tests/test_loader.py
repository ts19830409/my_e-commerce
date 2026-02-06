from src.loader import create_from_json, read_json


def test_json_loading():
    data = read_json("data/products.json")
    categories = create_from_json(data)
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
