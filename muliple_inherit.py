class A:
    def __init__(self):
        super().__init__()
        print("A initialized")
        self.a = 1    
    def a_fun(self, x):
        print(f"a_fun {x}")    


class B:
    def __init__(self):
        super().__init__()
        #when method resolution order (MRO) is used (multiple class inheritage, you should use super.__init__() for each mother class
        self.b = 2
        print("B initialized")
    def b_fun(self):
        print("b_fun hah")    

class C(A, B):
    def __init__(self):
        super().__init__()  # This implicitly calls A.__init__(), followed by B.__init__ via MRO
        print("C initialized")
# print(C.__mro__)

c_class = C()

c_class.a_fun(1)
print(c_class.a)
print(c_class.b)
c_class.b_fun()