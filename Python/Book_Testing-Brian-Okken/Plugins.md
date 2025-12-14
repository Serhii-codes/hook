**Installing pytest Plugins**
- **pytest** plugins are installed via **pip**, just like any other Python package.
- There are several installation methods:

1. **Install from PyPI (default)**
- Latest stable version:
```bash
pip install pytest-cov
```

- Specific version:
```bash
pip install pytest-cov==2.4.0
```

2. **Install from a File (.tar.gz or .whl)**
- Useful if PyPI is blocked (e.g., firewalls, network restrictions).
- Download the file and install directly:
```bash
pip install pytest-cov-2.4.0.tar.gz
# or
pip install pytest_cov-2.4.0-py2.py3-none-any.whl
```

3. **Install from a Local Directory**
-  Keep plugins locally:
```bash
mkdir some_plugins
cp pytest_cov-2.4.0-py2.py3-none-any.whl some_plugins/
```
- Install without PyPI:
```bash
pip install --no-index --find-links=./some_plugins/ pytest-cov
```
- Specific version:
```bash
pip install --no-index --find-links=./some_plugins/ pytest-cov==2.4.0
```
- Handy for **CI/CD**, **tox**, or when working with custom/third-party plugins.

4. **Install from Git Repository**
- Directly from GitHub:
```bash
pip install git+https://github.com/pytest-dev/pytest-cov
```
- From a version tag:
```bash
pip install git+https://github.com/pytest-dev/pytest-cov@v2.4.0
```
- From a branch: 
```bash
pip install git+https://github.com/pytest-dev/pytest-cov@master
```
- Useful if you need the **latest version** not yet on PyPI, or for your **own Git-hosted plugins**.

**Summary:**
- Use **PyPI** for standard installs.
- **Files / local directories** for closed environments or CI setups.
- **Git** for the freshest code or private projects.