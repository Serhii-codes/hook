**What is `mock`?**
The **`mock`** package allows you to _replace parts of your system_ to isolate the code under test.  
Mock objects are also known as:
- **test doubles**
- **stubs**
- **spies**
- **fakes**
They let you **focus on one piece of code** without depending on databases, APIs, or external services.

**Available Tools**
`unittest.mock`                Built-in since Python 3.3

`pytest-mock`                     Pytest plugin that simplifies using mocks

`monkeypatch`                     Built-in pytest fixture for simple replacement of attributes and                                                                   environment variables

Between `pytest-mock` and `monkeypatch`, you can handle nearly all mocking needs. 

**Why Use Mocks in the Tasks Project?**
- The **Tasks CLI** (`cli.py`) was _not covered by tests_.
- Full CLI testing isn’t necessary since **functionality is already tested** via `api.py`.
- Instead, we mock the **API layer** while testing the **CLI layer**.
Goal: Verify that CLI commands (like `tasks list`)  
→ call the API correctly and  
→ display correct output.

**Strategy for Testing `list` Command**
- **Replace** the real database context manager (`_tasks_db`) with a **stub** that does nothing.
- **Mock** the API function (`tasks.list_tasks`) so we can check how it was called.
- Use **Click’s `CliRunner`** to simulate CLI commands.
- **Assert** that:
    - The right API calls are made.
    - The printed output is correct.

**Example Stub**
```python
from contextlib import contextmanager

@contextmanager
def stub_tasks_db():
    yield
```
This replaces the real `_tasks_db()` context manager to avoid real DB calls.

**Using `pytest-mock`**
The `mocker` fixture (provided by `pytest-mock`) simplifies mocking.

**Example: test that API is called correctly**
```python
def test_list_no_args(mocker):
    mocker.patch.object(tasks.cli, '_tasks_db', new=stub_tasks_db)
    mocker.patch.object(tasks.cli.tasks, 'list_tasks', return_value=[])
    runner = CliRunner()
    runner.invoke(tasks.cli.tasks_cli, ['list'])
    tasks.cli.tasks.list_tasks.assert_called_once_with(None)
```
🔹 `patch.object()` replaces the original function or object.  
🔹 `return_value` sets what the mock should return.  
🔹 `assert_called_once_with()` checks how the mock was used.

**Checking CLI Output**
```python
@pytest.fixture()
def no_db(mocker):
    mocker.patch.object(tasks.cli, '_tasks_db', new=stub_tasks_db)

def test_list_print_empty(no_db, mocker):
    mocker.patch.object(tasks.cli.tasks, 'list_tasks', return_value=[])
    runner = CliRunner()
    result = runner.invoke(tasks.cli.tasks_cli, ['list'])
    expected_output = (
        " ID owner done summary\n"
        " -- ----- ---- -------\n"
    )
    assert result.output == expected_output
```
Here, the test compares the actual printed output to `expected_output`.

**More Example:

Multiple Items
```python
def test_list_print_many_items(no_db, mocker):
    many_tasks = (
        Task('write chapter', 'Brian', True, 1),
        Task('edit chapter', 'Katie', False, 2),
        Task('modify chapter', 'Brian', False, 3),
        Task('finalize chapter', 'Katie', False, 4),
    )
    mocker.patch.object(tasks.cli.tasks, 'list_tasks', return_value=many_tasks)
    runner = CliRunner()
    result = runner.invoke(tasks.cli.tasks_cli, ['list'])
    ...
```

Command-line Options
```python
def test_list_dash_o(no_db, mocker):
    mocker.patch.object(tasks.cli.tasks, 'list_tasks')
    runner = CliRunner()
    runner.invoke(tasks.cli.tasks_cli, ['list', '-o', 'brian'])
    tasks.cli.tasks.list_tasks.assert_called_once_with('brian')
```

Test Results
```bash
$ pytest -v tests/unit/test_cli.py
tests/unit/test_cli.py::test_list_no_args PASSED
tests/unit/test_cli.py::test_list_print_empty PASSED
tests/unit/test_cli.py::test_list_print_many_items PASSED
tests/unit/test_cli.py::test_list_dash_o PASSED
tests/unit/test_cli.py::test_list_dash_dash_owner PASSED
```
All tests pass, confirming correct CLI–API integration.

**Key Takeaways**
- **Mocks isolate dependencies** (DBs, APIs, external services).
- Use **`pytest-mock`** for a cleaner interface to `unittest.mock`.
- **CLI testing** can rely on **mocked APIs** instead of full integration tests.
- **`CliRunner`** from Click simulates command-line usage.
- Separate tests for:
    - ✅ Correct API call
    - ✅ Correct CLI output
