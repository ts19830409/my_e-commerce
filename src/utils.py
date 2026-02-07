class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация объекта товара"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возврат цены товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Установка новой цены товара"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): ")
            if answer.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, products_list: list["Product"] | None = None) -> "Product":
        """Создание нового товара на основе словаря"""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if products_list:
            for existing_product in products_list:
                if existing_product.name.lower() == name.lower():
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product

        return cls(name, description, price, quantity)

    def __str__(self):
        """Добавление строкового отображения для класса Product"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Получение полной стоимости всех товаров"""
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация объекта категории"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        """Возврат строкового представления всех товаров категории"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str

    def add_product(self, product: Product) -> None:
        """Добавление товара в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self):
        """Строковое отображение для класса Category"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity

        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return CategoryIter(self)


class CategoryIter:
    """Реализация магических методов __iter__, __next__"""

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        products = self.category._Category__products

        if self.index < len(products):
            product = products[self.index]
            self.index += 1
            return product

        raise StopIteration
