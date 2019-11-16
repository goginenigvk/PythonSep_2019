
class A:
     pass

class B(A):
     pass

class C(B): #C,B,A, Object
     pass

class D(A):  #D, A ,Object
     pass

class E(C): #E,C, B, A, Object
    pass

