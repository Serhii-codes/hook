```python
import pytest  
  
@pytest.fixture(params = [1, 100, 0, 0.1]) #можна передавати дані, відрацьовує по циклу  
def positive_number(request):  
    return request.param  

def test_5(positive_number):  
    assert positive_number >= 0
  
@pytest.fixture(params = ['qaenv', 'devenv']) # параметрозовану фікстуру краще використовувати для інвайремнтів  
def positive_number(request):  
    return request.param

def test_5(positive_number):  
    assert positive_number.isalpha() # isalpha() - тут перевірка проходить по буквам, чи являэтся символ букою і вони повіні бути без "_". Тобто: 'qa_env' - 'qaenv' тоді тест пройде
```
isalpha() - тут перевірка проходить по буквам, чи являэтся символ букою і вони повіні бути без "_". Тобто: 'qa_env' - 'qaenv' тоді тест пройде



#sh14