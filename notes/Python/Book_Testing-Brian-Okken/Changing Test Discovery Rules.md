## Standard Test Discovery Rules

Pytest finds tests according to the following rules:

1. **Starting directory:**
    - Discovery begins in one or more directories.
    - You can specify filenames or directory names on the command line.
    - If nothing is specified, the current directory is used.
2. **Recursive search:**  
    Pytest searches the directory and all subdirectories recursively.
3. **Test modules:**  
    A file is considered a test module if its name:
    - starts with `test_*.py`, or
    - ends with `*_test.py`.
4. **Test functions:**  
    Within test modules, pytest looks for **functions that start with `test_`**.
5. **Test classes:**
    - Pytest considers classes whose names start with `Test` as potential test classes.
    - The class **must not** have an `__init__()` method.
    - Pytest then looks for methods inside those classes that start with `test_`.

 These are the standard discovery rules — but they can be customized in `pytest.ini`.
 
 **Customizing Discovery Rules**
 ### `python_classes`
- By default, pytest treats a class as a test class if:
    - it starts with `Test`, and
    - it does **not** have an `__init__()` method.
- If you want to use other naming conventions, you can configure it like this:
  ``` bash
  [pytest]
  python_classes = *Test Test* *Suite
  ```
 
  This allows you to name your classes like:
```python
class DeleteSuite:
    def test_delete_1(self):
        ...

    def test_delete_2(self):
        ...
```

**`python_files`**
By default, pytest looks for test files that:
- start with `test_*`, or
- end with `*_test`.

If you use a custom naming convention (for example, `check_<something>.py`),  you can update `pytest.ini` like this:
```ini
[pytest]
python_files = test_* *_test check_*
```

Now pytest will recognize all files matching those patterns as test files.

**`python_functions`**

Works like the previous two settings but applies to test **function** and **method** names.
- The default pattern is `test_*`.

To also include functions starting with `check_`, add this line:
```ini
[pytest]
python_functions = test_* check_*
```
Now pytest will detect both `test_` and `check_` prefixed functions.

**Tip:**  
Pytest’s naming conventions are flexible.  
If you don’t like the defaults, you can change them — but do it for a good reason.  
For example, migrating hundreds of test files is definitely a valid one.

#sh03