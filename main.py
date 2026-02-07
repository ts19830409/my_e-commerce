from dotenv import load_dotenv

from src.loader import create_from_json, read_json
from src.utils import Category, LawnGrass, Product, Smartphone


def main_page() -> None:
    """Функция главной страницы"""

    """Основа для будущего меню пользователя"""
    print("*" * 16)
    print("ИНТЕРНЕТ МАГАЗИН")
    print("*" * 16)

    print("=" * 5)
    print("ПРАЙС")
    print("-" * 5)

    load_dotenv()

    json_data = read_json("data/products.json")
    data = create_from_json(json_data)

    for category in data:
        print(f"\n{category.name}:")
        for i, product in enumerate(category._Category__products, 1):
            print(f"{i}. {product.name} - {product.price} руб. (осталось: {product.quantity})")

    print("\n" + "-" * 28)
    print("СТАТИСТИКА МАГАЗИНА" + "\n")
    print(f"Загружено категорий: {len(data)}")
    print(f"Всего товаров в магазине: {Category.product_count}")
    print("-" * 28)

    """Проверка домашнего задания 1"""

    print("\n" + "=" * 40)
    print("ДЕМОНСТРАЦИЯ ДЗ")
    print("=" * 40)

    # 1. Геттер
    print("\n1. Геттер products (формат из ТЗ):")
    print(data[0].products)

    # 2. add_product (Задание 1)
    print("\n2. Метод add_product():")
    new_prod = Product("Новый товар", "Добавлен через add_product", 9999, 3)
    data[0].add_product(new_prod)
    print(f"Добавлен: {new_prod.name}")

    # 3. new_product
    print("\n3. Класс-метод new_product():")
    prod_data = {"name": "Созданный", "description": "Через new_product", "price": 5000, "quantity": 2}

    all_products = []
    for category in data:
        all_products.extend(category._Category__products)

    new_prod2 = Product.new_product(prod_data, all_products)  # ← ВТОРОЙ АРГУМЕНТ ДОБАВЛЕН
    print(f"Создан: {new_prod2.name}, цена: {new_prod2.price}")

    # 4. Сеттер цены
    print("\n4. Сеттер цены (защита от ≤ 0):")
    test = Product("Тест", "", 1000, 1)
    print(f"Было: {test.price}")
    test.price = -500  # Сообщение об ошибке
    print(f"После -500: {test.price} (не изменилась)")

    # 5. Проверка приватности
    print("\n5. Проверка приватного атрибута:")
    try:
        print(data[0].__products)
    except AttributeError:
        print("Приватный атрибут __products защищён")

    # 6. Демо понижения цены
    print("\n6. Подтверждение понижения цены (доп. задание):")
    print("(Следом будет запрос 'Подтвердите (y/n):' - введи y или n)")
    test_product = Product("Демо", "Для теста", 2000, 5)
    test_product.price = 1500  # ← Вызовет input() запрос

    """Проверка домашнего задания 2"""

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    print("1. Цикл for по category1:")
    for product in category1:  # ← ВОТ ОНО! Используем итератор
        print(f"{product}")

    print("\n2. Преобразование в список:")
    product_list = list(category1)
    print(f"Всего товаров в списке: {len(product_list)}")

    print("\n3. Ручная итерация:")
    iterator = iter(category1)
    try:
        while True:
            product = next(iterator)
            print(f"{product.name} за {product.price} руб.")
    except StopIteration:
        print("Список закончился")

    print("\n4. Суммирование цен через итератор:")
    total_value = 0
    for product in category1:
        total_value += product.price * product.quantity
    print(f"Общая стоимость всех товаров: {total_value} руб.")

    """Проверка домашнего задания 3"""

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])
    print(f"Создана категория: {category_grass.name}")

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")


if __name__ == "__main__":
    main_page()
