## Описание
Приложение для электронной торговли

## Функционал проекта.

### Пакет src

#### Модуль utils
Содержит классы Product и Category и их инициализацию
1. Инициализация объекта товара:
```
def __init__(self, name: str, description: str, price: float, quantity: int):
```
2. Возврат цены товара:
```
@property
    def price(self) -> float:
```
3. Установка новой цены товара:
```
@price.setter
    def price(self, new_price: float) -> None:
```
4. Создание нового товара на основе словаря:
```
@classmethod
    def new_product(cls, product_data: dict, products_list: list["Product"] | None = None) -> "Product":
```
5. Инициализация объекта категории:
```
def __init__(self, name: str, description: str, products: list[Product]):
```
6. Возврат строкового представления всех товаров категории:
```
@property
    def products(self) -> str:
```
7. Добавление товара в категорию:
```
 def add_product(self, product: Product) -> None:
```

#### Модуль loader
Содержит функции для работы с JSON-файлом:
1. Функция чтения JSON-файла':
```
def read_json(path: str) -> list:
```
2. Функция создания объектов из JSON-данных:
```
def create_from_json(data: list) -> List[Category]:
```

### Пакет tests
Содержит модули conftest, test_utils, test_loader для тестирования соответствующих модулей.
Тесты написаны с использованием фикстур и параметризации.

# Установка:
**Клонируйте репозиторий:**
```
git@github.com:ts19830409/my_e-commerce.git
```
*Проект разработан в рамках домашней работы*