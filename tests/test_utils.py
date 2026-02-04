from src.utils import Product, Category


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
	assert len(category.products) == 2
	assert category.products[0].name == "phone"
	assert category.products[1].name == "TV"


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
