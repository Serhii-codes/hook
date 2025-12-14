```python
from subprocess import run  
  
def test_hello():  
    result = run(["python3", "hello.py"], capture_output=True, text=True)  
    output = result.stdout  
    assert output == "Hello, Hello\n"


```
result = run(["python3", "hello.py"], capture_output=True, text=True)   -  якою командою запускаємо наш файл
`sys.stdin` - Наш ввод (input). This stream is used to receive input from the user or another process. By default, it's connected to the keyboard, but it can be redirected to read from a file or the output of another command in a shell. The `input()` function in Python reads from `sys.stdin`.

`sys.stdout` -  Показує наш вивід. This stream is used to display normal program output. By default, it's connected to the console or terminal, but it can be redirected to write to a file or serve as input for another command. The `print()` function in Python writes to `sys.stdout`. 

`sys.stderr` - Показує наші помилки. This stream is specifically designated for error messages and diagnostic output. It's also connected to the console by default, but separating error output from regular output allows for easier redirection and handling of errors independently. You can explicitly print to `sys.stderr` by using `print("Error message", file=sys.stderr)`



