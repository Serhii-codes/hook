
The minversion setting enables you to specify a minimum pytest version you expect for your
tests. For instance, I like to use approx() when testing floating point numbers for “close enough”
equality in tests. But this feature didn’t get introduced into pytest until version 3.0. To avoid
confusion, I add the following to projects that use approx():
```bash
[pytest]
minversion = ​ 3.0
```
This way, if someone tries to run the tests using an older version of pytest, an error message
appears.