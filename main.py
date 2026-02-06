from dotenv import load_dotenv

from src.loader import create_from_json, read_json
from src.utils import Category, Product


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

    """Проверка домашнего задания"""

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
    print("   (Следом будет запрос 'Подтвердите (y/n):' - введи y или n)")
    test_product = Product("Демо", "Для теста", 2000, 5)
    test_product.price = 1500  # ← Вызовет input() запрос

if __name__ == "__main__":
    main_page()
