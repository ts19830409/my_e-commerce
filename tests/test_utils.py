from src.utils import Product, Category
import pytest


def test_product_initialization(first_product):
	"""Тест создания продукта."""
	assert first_product.name == "phone"
	assert first_product.description == "dialer"
	assert first_product.price == 100.00
	assert first_product.quantity == 10


def test_category_initialization(first_product, second_product):
	"""Тест создания категории."""
	category = Category(
		"Electronics",
		"Tech stuff",
		[first_product, second_product]
	)
	
	assert category.name == "Electronics"
	assert category.description == "Tech stuff"
	
	products_str = category.products
	assert "phone" in products_str
	assert "TV" in products_str
	
	lines = [line for line in products_str.split('\n') if line.strip()]
	assert len(lines) == 2


def test_category_counter(first_product):
	"""Тест счётчика категорий."""
	Category.category_count = 0
	Category.product_count = 0
	
	initial_count = Category.category_count
	
	Category("Cat1", "Desc1", [first_product])
	Category("Cat2", "Desc2", [first_product])
	
	assert Category.category_count == initial_count + 2


def test_product_counter(first_product, second_product):
	"""Тест счётчика товаров."""
	
	Category.category_count = 0
	Category.product_count = 0
	
	initial_products = Category.product_count
	
	Category("Cat1", "Desc1", [first_product, second_product])
	Category("Cat2", "Desc2", [first_product])
	
	assert Category.product_count == initial_products + 3


# НОВЫЕ ТЕСТЫ ДЛЯ НОВОЙ ФУНКЦИОНАЛЬНОСТИ

def test_product_price_getter_setter():
	"""Тест геттера и сеттера цены."""
	product = Product("Test", "Desc", 100, 5)
	assert product.price == 100
	
	product.price = 150
	assert product.price == 150
	
	product.price = -50
	assert product.price == 150


def test_new_product_classmethod():
	"""Тест создания товара через класс-метод."""
	product_data = {
		'name': 'Ноутбук',
		'description': 'Игровой',
		'price': 50000,
		'quantity': 3
	}
	product = Product.new_product(product_data)
	assert product.name == 'Ноутбук'
	assert product.price == 50000
	assert product.quantity == 3


def test_new_product_with_duplicate():
	"""Тест new_product с дубликатом (доп. задание)."""
	existing_product = Product("Товар", "Описание", 100, 3)
	
	new_data = {
		'name': 'Товар',
		'description': 'Новое описание',
		'price': 150,
		'quantity': 2
	}
	
	result = Product.new_product(new_data, [existing_product])
	
	assert result is existing_product
	assert existing_product.quantity == 5
	assert existing_product.price == 150


def test_category_add_product():
	"""Тест добавления товара в категорию."""
	category = Category("Электроника", "Техника", [])
	product = Product("Мышь", "Беспроводная", 2000, 10)
	
	initial_count = Category.product_count
	category.add_product(product)
	
	assert "Мышь, 2000 руб. Остаток: 10 шт." in category.products
	assert Category.product_count == initial_count + 1


def test_category_products_getter_format():
	"""Тест формата вывода геттера products."""
	category = Category("Тест", "Описание", [])
	p1 = Product("Товар1", "Описание1", 100, 5)
	p2 = Product("Товар2", "Описание2", 200, 3)
	
	category.add_product(p1)
	category.add_product(p2)
	
	output = category.products
	lines = [line for line in output.split('\n') if line.strip()]
	
	assert len(lines) == 2
	assert "Товар1, 100 руб. Остаток: 5 шт." in output
	assert "Товар2, 200 руб. Остаток: 3 шт." in output


def test_private_attributes_access():
	"""Тест приватности атрибутов."""
	category = Category("Test", "Desc", [])
	product = Product("Test", "Desc", 100, 5)
	
	
	with pytest.raises(AttributeError):
		_ = category.__products
	
	with pytest.raises(AttributeError):
		_ = product.__price
