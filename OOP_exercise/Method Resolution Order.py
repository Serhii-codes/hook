# We can get the MRO of a class. For this purpose, we can use either the mro attribute or the mro() method.
class A:
    def process(self):
        print(" In class A")

class B(A):
    def process(self):
        print(" In class B")

class C(B, A):
    def process(self):
        print(" In class C")

# Creating object of C class
C1 = C()
C1.process()
print(C.mro())
# In class C
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]