- pytest.ini: This is the primary pytest configuration file that allows you to change default
behavior. Since there are quite a few configuration changes you can make. 

- conftest.py: This is a local plugin to allow hook functions and fixtures for the directory
where the conftest.py file exists and all subdirectories.

- __init__.py: When put into every test subdirectory, this file allows you to have identical
test filenames in multiple test directories.

**TOX**
- tox.ini: This file is similar to pytest.ini, but for tox. However, you can put your pytest
configuration here instead of having both a tox.ini and a pytest.ini file, saving you one
configuration file.

**Python package**
- setup.cfg: This is a file that’s also in ini file format and affects the behavior of setup.py.
It’s possible to add a couple of lines to setup.py to allow you to run python setup.py test
and have it run all of your pytest tests. If you are distributing a package, you may already
have a setup.cfg file, and you can use that file to store pytest configuration.

Pytest configuration files

pytest.ini — The main configuration file for pytest.
It allows you to customize the default testing behavior, such as test discovery paths, markers, logging, and runtime options.

conftest.py — A local pytest plugin that defines fixtures, hooks, and shared test logic for the current directory and all its subdirectories.
It doesn’t need to be imported manually.

__init__.py — Marks a directory as a Python package.
Including it in each test subdirectory allows you to use identical test filenames in multiple directories without naming conflicts.

Tox

tox.ini — The configuration file for tox, a tool that automates testing in multiple environments.
It can also include a [pytest] section, so you can store your pytest settings here instead of having a separate pytest.ini file.

```bash 
Python package setup
```

setup.cfg — A configuration file (in .ini format) that controls the behavior of setup.py.
You can also include pytest settings here and run your tests with:

#sh14