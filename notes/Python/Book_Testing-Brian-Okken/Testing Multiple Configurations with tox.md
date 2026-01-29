**tox** is a command-line tool that lets you run your full test suite across multiple environments.

Most commonly this means multiple **Python versions**, but tox can also test:
- different dependency combinations
- different OS-level configurations
- different tool versions

## Mental model of how tox works
For each environment listed in `tox.ini`, tox:
1. creates a virtual environment inside `.tox/`
2. `pip install`s required test dependencies
3. `pip install`s your package (from an sdist built via `setup.py`)
4. runs the test command (usually `pytest`)
After all environments finish, tox prints a summary.

## Project setup
Place `tox.ini` in the **same directory** as `setup.py` (top level of the project).  
You can move settings from `pytest.ini` into `tox.ini` to reduce the number of config files.
Example project tree:

```arduino
project/
├── setup.py
├── tox.ini
├── src/
│   └── tasks/
└── tests/
    ├── conftest.py
    ├── func/
    └── unit/
```

**Example** `tox.ini`
```ini
[tox]
envlist = py27,py36

[testenv]
deps = pytest
commands = pytest

[pytest]
addopts = -rsxX -l --tb=short --strict
markers =
    smoke: Run smoke test functions
    get: Run test functions that test tasks.get()
```
### Explanation

|Section|Meaning|
|---|---|
|`[tox] envlist`|list of Python environments to test|
|`[testenv] deps`|what packages tox installs into each venv|
|`[testenv] commands`|the test command to execute in each environment|
|`[pytest]`|pytest configuration (same as in pytest.ini)|
**Running tox**
```bash
pip install tox
```
Then run:
```bash
cd /path/to/project
tox
```
tox will:
- create `.tox/py27/`, `.tox/py36/` etc.
- install dependencies
- run pytest in each environment
- show a combined report
You get a final summary like:
```markdown
_____________________ summary ______________________
py27: commands succeeded
py36: commands succeeded
congratulations :)
```
## Key idea
tox is extremely useful if:
- your package needs to run on multiple Python versions
- you want repeatable test environments
- you want to test different dependency matrices
It is basically reproducible CI-matrix testing — locally.