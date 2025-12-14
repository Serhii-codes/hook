**norecursedirs** - tells pytest **which directories to skip** when searching for tests.  
**testpaths** - tells pytest **where to look** for tests.  
**testpaths** -  is a **list of directories (relative to the project root)** where pytest should look for tests. It’s only used if no directory, file, or nodeid is specified as a command-line argument.

```bash 
[pytest] 
norecursedirs = ​ .* venv src *.egg dist build

#put tests in testpaths:
[pytest]
testpaths = ​ tests
#pytest will only look in
tasks_proj/tests.
```
