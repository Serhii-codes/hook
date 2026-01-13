cd Pytest includes a few helpful builtin markers: ***skip, skipif**,* and ***xfail.***

```python
@pytest.mark.skip(reason='misunderstood the API') - example skiping test with reason 
@pytest.mark.skipif(tasks.__version__ < '0.2.0',  
                    reason='not supported until version 0.2.0') - example intend to make that work in version 0.2.0 of the package
```
With the ***xfail*** marker, we are telling pytest to run a test function, but that we expect it to fail.

#sh01 
