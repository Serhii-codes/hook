### Що таке база даних (БД)
База даних – це **структуроване сховище інформації**, яке дозволяє швидко зберігати, читати і обробляти дані.  
Приклади: MySQL, PostgreSQL, SQLite, MongoDB.
- **Таблиці** – зберігають дані у рядках і стовпцях.
- **Запити** – SQL (Structured Query Language) або API для отримання/зміни даних.
- **Відносини** – зв’язки між таблицями (наприклад, користувачі та їхні замовлення).
### Чому важливе тестування БД
Тести баз даних перевіряють, що:
- дані зберігаються правильно;
- логіка обробки даних працює коректно;
- зміни в коді не порушують структуру або цілісність даних.

### Основні підходи у тестах
1. **Тестування CRUD** – Create, Read, Update, Delete.
2. **Валідація схем** – чи є потрібні таблиці, поля, типи даних.
3. **Тестування транзакцій** – rollback працює правильно.
4. **Тестування через Pytest**:
    - Використовують **фікстури**, щоб створювати тимчасову тестову БД.
    - Можна підміняти справжню БД на **in-memory SQLite** для швидких тестів.
### Приклад Pytest + SQLite
```python
import sqlite3
import pytest

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")  # тимчасова БД в пам'яті
    yield conn
    conn.close()

def test_insert_user(db_connection):
    cur = db_connection.cursor()
    cur.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    cur.execute("INSERT INTO users VALUES (1, 'Alice')")
    cur.execute("SELECT name FROM users WHERE id=1")
    assert cur.fetchone()[0] == 'Alice'

```