sdist stands for “source distribution.”

To install pytest-nice from myplugins:
​
``` bash
$ ​ pip​​ ​ install​​ ​ --no-index​​ ​ --find-links​​ ​ myplugins​​ ​ pytest-nice`
```

(138)The --no-index tells pip to not go out to PyPI to look for what you want to install. The --find-
links myplugins tells PyPI to look in myplugins for packages to install. And of course, pytest-
nice is what we want to install.
If you’ve done some bug fixes and there are newer versions in myplugins, you can upgrade by
adding --upgrade:  

``` bash
$ ​ pip​​ ​ install​​ ​ --upgrade​​ ​ --no-index​​ ​ --find-links​​ ​ myplugins​​ ​ pytest-nice
```

This is just like any other use of pip, but with the --no-index --find-links myplugins added.

#sh7