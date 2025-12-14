- `@pytest.mark.smoke` — позначка (декоратор)
- `pytest -m smoke -v` — вивести тести з маркою smoke

### Marker configuration file

warnings summary — прибрати їх потрібно ствроити файл *ini і внього вказати позначку для pytest  
Приклад:
```python
[pytest]  
markers =  
    smoke: use for smoke test  
    regression: regression test  
  
addopts =  
    -v   
    -qq   
    -s
    
```
addopts -  вказуэмо параметри видачі результатів наших тестів без додаткогового вводу при заупуску
Ось тут: [[Useful CLI Options]] можна глняути можливі варіанти CLI 