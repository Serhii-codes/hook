```python
@pytest.mark.parametrize('a', [3, 4, 5 ])  
@pytest.mark.parametrize('b', [10, 100, 1000])  
def test_6(a, b):  
    print(a, b)  
    assert True

```
#sh01 