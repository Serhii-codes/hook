Модуль `datetime` використовується для роботи з **датою та часом**. Він дуже часто зустрічається в тестах, особливо коли треба перевіряти:
- правильність збереження часу у базі;
- обробку часових інтервалів;
- логіку, що залежить від дати або часу (наприклад, терміни, дедлайни, відкладені дії).
### Основні класи та функції
1. datetime.date – працює тільки з датою (рік, місяць, день):
```python
from datetime import date
today = date.today()
print(today)  # 2025-08-18
```
 2. datetime.time – працює тільки з часом (години, хвилини, секунди, мікросекунди):
```python
from datetime import time
t = time(14, 30, 0)
print(t)  # 14:30:00 
```
 3. datetime.datetime  – поєднує дату та час: 
```python
 from datetime import datetime
now = datetime.now()  # поточний час і дата
print(now)  # 2025-08-18 23:10:05.123456
```
4. **`datetime.timedelta`** – для обчислень різниці між датами або часом:
```python
from datetime import timedelta
yesterday = now - timedelta(days=1)
print(yesterday)
```
5. Форматування та парсинг дат:
```python
# у рядок
date_str = now.strftime("%Y-%m-%d %H:%M:%S")
# з рядка у datetime
parsed = datetime.strptime("2025-08-18 12:00:00", "%Y-%m-%d %H:%M:%S")
```
### Використання у тестах
- Перевірка правильності формату дати при збереженні.
- Тестування логіки, що залежить від часу (`if now > deadline`).
- Використання **mock datetime** для стабільних тестів, щоб час не змінював результат.