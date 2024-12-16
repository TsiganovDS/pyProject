# Виджет банковских операций клиента.
# Описание проекта
###  Программа создана для фильтрации и сортировки банковских счетов по дате и оплате.
### Project dependencies:
### The program uses the version Python 3.12.4
### flake8 = "7.1.1"
### black = "24.10.0"
### isort = "5.13.2"
### mypy = "1.13.0"
## Функции, которые мы будем использовать:
## Модуль masks.py:
### get_mask_card_number: Принимает строку, содержащую тип и номер карты или счета. Возвращает строку с замаскированным номером карты/счета.
### get_mask_account: Функция маскировки номера счета.
## Модуль widget.py:
### mask_account_card: Функция обрабатывает информацию как о картах, так и о счетах.
### get_date: Принимает строку с датой в формате iso 8601. Возвращает строку с датой в формате ДД.ММ.ГГГГ.
## Модуль processing.py:
### filter_by_state: Принимает список словарей и опционально значение для ключа state. Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению (по умолчанию - "EXECUTED").
### sort_by_date: Принимает список словарей. Возвращает новый список, отсротированный по дате. По умолчанию сортировка идет по убыванию, чтобы изменить порядок - при вызове функции вторым аргументом необходимо передать булевое значение "False".
## Модуль generators.py:
### filter_by_currency: Принимает список словарей, представляющих транзакции. Возвращает по одному словарю из списка, в котором валюта операции соответствует заданной (по умолчанию USD, для изменения вторым аргументом надо передать буквенный код интересующей валюты, например "RUB".
### transaction_descriptions: Принимает список словарей, представляющих транзакции. Возвращает описания (description) каждой операции из списка по одному.
### card_number_generator: Генерирует 16-значные номера карт в рамках заданнного диапазона. При вызове генератора первым аргументом передаем начальное значение генерации диапазона, вторым аргументом передаем конечное значение диапазона (включительно). То есть, если передать в качестве аргументов значения 1 и 5, то будут сгенерированы номера карт: "0000 0000 0000 0001", "0000 0000 0000 0002" и далее пока не дойдет до "0000 0000 0000 0005" На вход может принимать как данные в формате int, так и в формате string.
## Инструкция по установке:
### 1.Скачать репозиторий: git clone https://github.com/TsiganovDS/pyProject
### 2. 2.Установить необходимые зависимости: pip install -r requirements
## Тестирование
### Этот проект использует для тестирования фреймворк pytest.
### Покрыт тестами code coverage. Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующей командой:
### poetry run pytest --cov
