`@pytest.fixture(scope="function")` — як часто перезапускається тест
В одній фікстурі можна викликати декілька фікстур:

```python
@pytest.fixture()  
def db_with_3_tasks(tasks_db, tasks_just_a_few):  
    """Connected db with 3 tasks, all unique."""  
    for t in tasks_just_a_few:  
        tasks.add(t)
```



| Scope      | Description                                      |
| ---------- | ------------------------------------------------ |
| `function` | Виконується **для кожного окремого тесту**       |
| `class`    | Виконується **один раз для всіх тестів у класі** |
| `module`   | Виконується один раз **на весь файл**            |
| `package`  | Для всього пакету                                |
| `session`  | Один раз за запуск усіх тестів                   |
[[Parametrize Fixture]]



