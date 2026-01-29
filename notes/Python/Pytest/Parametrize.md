```python
@pytest.mark.parametrize('first_number, second_number, result', (
    (2, 3, 5),
    (-1, 3, 2)
))

```
`pytest.param(2, 3, 5, id='positive number')` — задаємо назву тесту та його унікальний ідентифікатор

**Using keywords**
Можна зберігати як key word і при необхідності параметрайзери імпортувати з іншого файлу. Використовувати при великій кількості параметрів в тестах 
```python
OUP_TEST_DATA = {
    'ids': ['positive', 'zero','zero and negative'],    # id names of test
    'argnames':'one, two, result',                      # arguments for parametrize 
    'argvalues': [(5, 3, 8), (0, 0, 0), (-10, 0, -10)]  # values for parametrize
}

@pytest.mark.parametrize(**OUP_TEST_DATA) # using our parametrize for test **key_word
def test_add(one, two, result):
    assert add(one, two) == result
```

[[Багатовимірна parametrize]]
