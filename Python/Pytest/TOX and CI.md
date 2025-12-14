```python
[tox]  
envlist = py36, py37, py38, py39, py310     #говориш який тобі Python потрібен  
isolated_bild = True  
skip_missing_interpreters = True  
  
[testenv]  
deps =  
    pytest  
    requests  
commands = pytest -v

```
файл зберігається в *ini format
envlist = py36, py37, py38, py39, py310  - вказуэш на яких інвайрементах тобі ранити тест
isolated_bild = True - ти ізолюєш свій білд


dep = - вказуєш що ті треба встановити. Ранить всі тести що розміщені в папці

 [[yml file fo CI(github actions)]]
