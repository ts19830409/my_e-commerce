## Описание
Приложение для электронной торговли

## Функционал проекта.

### Пакет src

#### Модуль utils
Содержит классы Product и Category и их инициализацию
1. class Product:
```
def __init__(self, name: str, description: str, price: float, quantity: int):
```
2. class Category:
```
def __init__(self, name: str, description: str, products: list[Product]):
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