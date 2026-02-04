import pytest

from src.utils import (Product, Category)

@pytest.fixture
def first_product():
	return Product(
	"phone",
	"dialer",
	100.00,
	10
	)


@pytest.fixture
def second_product():
	return Product(
	"TV",
	"watcher",
	200.00,
	20
	)

	