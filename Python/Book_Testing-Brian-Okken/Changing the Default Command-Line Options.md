```bash 
[pytest]
addopts = ​ -rsxX -l --tb=short --strict
```

The -rsxX tells pytest to report the reasons for all tests that skipped, xfailed, or xpassed. The -l
tells pytest to report the local variables for every failure with the stacktrace. The --tb=short
removes a lot of the stack trace. It leaves the file and line number, though. The --strict option
disallows markers to be used if they aren’t registered in a config file.