`setup_method(self)` — метод сетапу. Всі налаштування які ми робимо до теста!
```python
def setup_method(self):
    print("connection to database")
    self.data = 10

```

`teardown_method(self)` — метод тердаун. Налаштування які ми робимо після тесту!

```python
def teardown_method(self):
    print("close database")


```
- `@pytest.fixture` — фікстура об’єднує setup та teardown, зберігати у файлі **conftest.py**
- `yield` — все до yield → setup, все після yield → teardown. Те що пишемо у `yield` повернеться після fixture

**атомарні тести — один тест одна перевірка**
